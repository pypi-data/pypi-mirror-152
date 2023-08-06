import linecache
from typing import *
from functools import cached_property, partial
from itertools import chain 
import inspect
import warnings 
import pathlib

import pandas as pd 
import torch
import numpy as np
import scanpy as sc 
import pytorch_lightning as pl 

from scipy.sparse import issparse 
from torch.utils.data import Dataset, DataLoader, ConcatDataset
from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_class_weight

class CSVData(Dataset):
    """
    Defines a PyTorch Dataset for a CSV too large to fit in memory. 
    """
    def __init__(
        self, 
        filename: str,
        labelname: str,
        class_label: str,
        indices: Iterable[int]=None,
        skip=3,
        cast=True,
        sep=',',
        index_col=None,
        columns: List[any]=None,
        **kwargs, # To handle extraneous inputs
    ):
        """
        Initialization method for CSVData

        :param filename: Path to csv data file, where rows are samples and columns are features
        :type filename: str
        :param labelname: Path to label file, where column '# labels' defines classification labels
        :type labelname: str
        :param class_label: Label to train on, must be in labelname file
        :type class_label: str
        :param indices: List of indices to use in dataset. If None, all indices given in labelname are used., defaults to None
        :type indices: Iterable[int], optional
        :param skip: number of lines to skip in datafile csv, since header lines are often unneeded, defaults to 3
        :type skip: int, optional
        :param cast: cast sample to float32, defaults to True
        :type cast: bool, optional
        :param index_col: column in labelfile that contains numerical indices of datafiles, defaults to 'cell'
        :type index_col: str, optional
        :param sep: separator for labelfile and datafile, defaults to ','
        :type sep: str, optional
        """

        self.filename = filename
        self.labelname = labelname # alias 
        self.class_label = class_label
        self.index_col = index_col 
        self.skip = skip
        self.cast = cast
        self.indices = indices
        self.sep = sep
        self._cols = columns

        if indices is None:
            self._labeldf = pd.read_csv(labelname, sep=self.sep).reset_index(drop=True)
        else:
            self._labeldf = pd.read_csv(labelname, sep=self.sep).loc[indices, :].reset_index(drop=True)

    def __getitem__(self, idx: int):
        """Get sample at index

        :param idx: Numerical index between 0, len(self) -1 
        :type idx: int
        :raises ValueError: Errors in the case of unbounded slicing, which is normally supported in this method 
        :return: Returns a data, label sample
        :rtype: Tuple[torch.Tensor, Any]
        """        
        # Handle slicing 
        if isinstance(idx, slice):
            if idx.start is None or idx.stop is None:
                raise ValueError(
                    f"Error: Unlike other iterables, {self.__class__.__name__} does not support unbounded slicing since samples are being read as needed from disk, which may result in memory errors."
                )

            step = (1 if idx.step is None else idx.step)
            idxs = range(idx.start, idx.stop, step)
            return [self[i] for i in idxs]

        # The actual line in the datafile to get, corresponding to the number in the self.index_col values, if we need to
        data_index = (self._labeldf.loc[idx, self.index_col] if self.index_col is not None else idx)

        # get gene expression for current cell from csv file
        # We skip some lines because we're reading directly from 
        line = linecache.getline(self.filename, data_index + self.skip)
        
        if self.cast:
            data = torch.from_numpy(np.array(line.split(self.sep), dtype=np.float32)).float()
        else:
            data = np.array(line.split(self.sep))

        label = self._labeldf.loc[idx, self.class_label]

        return data, label

    def __len__(self):
        return len(self._labeldf) # number of total samples 

    @cached_property
    def columns(self): # Just an alias...
        return self.features

    @cached_property # Worth caching, since this is a list comprehension on up to 50k strings. Annoying. 
    def features(self):
        if self._cols is not None:
            return self._cols 
        else:
            data = linecache.getline(self.filename, self.skip - 1)
            data = [x.split('|')[0].upper().strip() for x in data.split(self.sep)]
            return data

    @cached_property
    def labels(self):
        return self._labeldf.loc[:, self.class_label].unique()

    @property
    def shape(self):
        return (self.__len__(), len(self.features))
    
    @cached_property 
    def class_weights(self):
        labels = self._labeldf.loc[:, self.class_label].values

        return compute_class_weight(
            class_weight='balanced',
            classes=np.unique(labels),
            y=labels
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(filename={self.filename}, labelname={self.labelname})"

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(filename={self.filename}, "
            f"labelname={self.labelname}, "
            f"skip={self.skip}, "
            f"cast={self.cast}, "
            f"indices={self.indices})"
        )

class NumpyStream(Dataset):
    def __init__(self,
        matrix: np.ndarray,
        labels: List[any]=None,
        labelfile: str=None, 
        class_label: str=None,
        index_col=None,
        sep=',',
        columns: List[any]=None,
        *args,
        **kwargs,
    ) -> None:
        super().__init__()

        # Make sure labels and labelfile aren't both passed 
        if labels is not None and labelfile is not None:
            raise ValueError("Either a list of labels may be passed or a .csv file to read from, but not both.")

        # Make sure neither labels nor labelfile isn't passed 
        if labels is None and labelfile is None:
            raise ValueError("One of labels or labelfile must be passed.")

        # If labelfile is passed, then we need an associated column to pull the class_label from 
        if labelfile is not None and class_label is None:
            raise ValueError(f"If labelfile is passed, column to corresponding class must be passed in class_label. Got {class_label = }.")

        # If we're using labels but the user passes a class label, just warn 
        if labels is not None and class_label is not None:
            warnings.warn(f"{class_label = } but labels passed, using labels and ignoring class_label. To silence this warning remove the class_labels positional or keyword argument.")

        if columns is None:
            warnings.warn(f"{self.__class__.__name__} initialized without columns. This will error if training with multiple Datasets with posssibly columns.")

        self.data = matrix
        self.labelfile = labelfile
        self.class_label = class_label
        self.index_col = index_col
        self.sep = sep
        self.columns = columns

        # We have a labelfile and some specified indices 
        if labelfile is not None:
            self.labels = pd.read_csv(labelfile, sep=self.sep).reset_index(drop=True).loc[:, class_label].values 
        else:
            self.labels = labels 

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            step = (1 if idx.step is None else idx.step)
            idxs = range(idx.start, idx.stop, step)
            return [self[i] for i in idxs]

        data = self.data[idx]

        # If matrix is sparse, then densify it for training
        if issparse(data):
            data = data.todense()

        return (
            torch.from_numpy(data), 
            self.labels[idx]
        )
    
    def __len__(self):
        return len(self.data)

class CollateLoader(DataLoader):
    def __init__(
        self,
        dataset: Type[Dataset],
        refgenes: List[str]=None,
        currgenes: List[str]=None,
        transpose: bool=False, 
        normalize: bool=False,
        *args,
        **kwargs,
    ) -> None:
        """
        Initializes a CollateLoader for efficient numerical batch-wise transformations

        :param dataset: CSVDataset to create DataLoader from
        :type dataset: Type[Dataset]
        :param refgenes: Optional, list of columns to take intersection with , defaults to None
        :type refgenes: List[str], optional
        :param currgenes: Optional, list of current dataset columns, defaults to None
        :type currgenes: List[str], optional
        :param transpose: Boolean indicating whether to tranpose the batch data , defaults to False
        :type transpose: bool, optional
        :param normalize: Boolean indicating whether to normalize the batch data, defaults to False
        :type normalize: bool, optional
        :raises ValueError: If refgenes are passed, currgenes also have to be passed otherwise we dont know what to align with
        """

        if refgenes is None and currgenes is not None or refgenes is not None and currgenes is None:
            raise ValueError("If refgenes is passed, currgenes must be passed too. If currgenes is passed, refgenes must be passed too.")
        
        # Create collate_fn via a partial of the possible collators, depending on if columns intersection is being calculated
        if refgenes is not None:
            collate_fn = partial(
                _collate_with_refgenes, 
                refgenes=refgenes, 
                currgenes=currgenes, 
                transpose=transpose, 
                normalize=normalize
            )
        else:
            collate_fn = partial(
                _standard_collate, 
                normalize=normalize, 
                transpose=transpose
            )

        # This is awkward, but Dataloader init doesn't handle optional keyword arguments
        # So we have to take the intersection between the passed **kwargs and the DataLoader named arguments
        allowed_args = inspect.signature(super().__init__).parameters
        new_kwargs = {}

        for key in allowed_args:
            name = allowed_args[key].name
            if name in kwargs:
                new_kwargs[key] = kwargs[key]

        # Finally, initialize the DataLoader
        super().__init__(
            dataset=dataset,
            collate_fn=collate_fn,
            **new_kwargs,
        )

class SequentialLoader:
    """
    Class to sequentially stream samples from an arbitrary number of DataLoaders.

    :param dataloaders: List of DataLoaders or DataLoader derived class, such as the CollateLoader from above 
    :type dataloaders: List[Union[DataLoader, SequentialLoader]]
    """
    def __init__(self, dataloaders):
        self.dataloaders = dataloaders

    def __len__(self):
        return sum([len(dl) for dl in self.dataloaders])

    def __iter__(self):
        yield from chain(*self.dataloaders)

def _collate_with_refgenes(
    sample: List[tuple], 
    refgenes: List[str], 
    currgenes: List[str],
    transpose: bool,
    normalize: bool,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Collate minibatch of samples where we're intersecting the columns between refgenes and currgenes,

    :param sample: List of samples from CSVData object
    :type sample: List[tuple]
    :param refgenes: List of reference genes
    :type refgenes: List[str]
    :param currgenes: List of current columns from sample 
    :type currgenes: List[str]
    :param transpose: boolean, indicates if we should transpose the minibatch (in the case of incorrectly formatted .csv data)
    :type transpose: bool
    :param normalize: boolean, indicates if we should normalize the minibatch
    :type normalize: bool
    :return: Two torch.Tensors containing the data and labels, respectively
    :rtype: Tuple[torch.Tensor, torch.Tensor]
    """

    data = clean_sample(torch.stack([x[0] for x in sample]), refgenes, currgenes)
    labels = torch.tensor([x[1] for x in sample])

    return _transform_sample(data, normalize, transpose), labels 

def _standard_collate(
    sample: List[tuple],
    normalize: bool,
    transpose: bool,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Collate minibatch of samples, optionally normalizing and transposing. 

    :param sample: List of CSVData items to collate
    :type sample: List[tuple]
    :param normalize: boolean, indicates if we should transpose the minibatch (in the case of incorrectly formatted .csv data)
    :type normalize: bool
    :param transpose: boolean, indicates if we should normalize the minibatch
    :type transpose: bool
    :return: Collated samples and labels, respectively
    :rtype: Tuple[torch.Tensor, torch.Tensor]
    """    
    data = torch.stack([x[0] for x in sample])
    labels = torch.tensor([x[1] for x in sample])

    return _transform_sample(data, normalize, transpose), labels 

def _transform_sample(
    data: torch.Tensor, 
    normalize: bool, 
    transpose: bool
) -> torch.Tensor:
    """
    Optionally normalize and tranpose a torch.Tensor

    :param data: Input sample
    :type data: torch.Tensor
    :param normalize: To normalize sample or not 
    :type normalize: bool
    :param transpose: to transpose sample or not 
    :type transpose: bool
    :return: Modified sample 
    :rtype: torch.Tensor
    """    
    if transpose:
        data = data.T

    if normalize:
        data = torch.nn.functional.normalize(data)

    return data 

def clean_sample(
    sample: torch.Tensor, 
    refgenes: List[str], 
    currgenes: List[str],
) -> torch.Tensor:
    # currgenes and refgenes are already sorted
    # Passed from calculate_intersection
    """
    Remove uneeded gene columns for given sample.

    :param sample: n samples to clean
    :type sample: torch.Tensor
    :param refgenes: list of reference genes from helper.generate_intersection(), contains the genes we want to keep
    :type refgenes: List[str]
    :param currgenes: list of reference genes for the current sample
    :type currgenes: List[str]
    :return: Sample reordered and intersected with the list of refgenes
    :rtype: torch.Tensor
    """
    intersection = np.intersect1d(currgenes, refgenes, return_indices=True)
    indices = intersection[1] # List of indices in currgenes that equal refgenes 
    
    axis = (1 if sample.ndim == 2 else 0)
    sample = np.sort(sample, axis=axis)
    sample = np.take(sample, indices, axis=axis)

    return torch.from_numpy(sample)

def generate_datasets(
    datafiles: List[str],
    labelfiles: List[str],
    class_label: str,
    test_prop: float=0.2,
    combine=False,
    *args,
    **kwargs,
) -> Tuple[Dataset, Dataset]:
    """
    Generates the COMBINED train/val/test datasets with stratified label splitting. 
    This means that the proportion of each label is the same in the training, validation and test set. 

    :param datafiles: List of absolute paths to csv files under data_path/ that define cell x expression matrices
    :type datafiles: List[str]
    :param labelfiles: ist of absolute paths to csv files under data_path/ that define cell x class matrices
    :type labelfiles: List[str]
    :param class_label: Column in label files to train on. Must exist in all datasets, this should throw a natural error if it does not. 
    :type class_label: str
    :param test_prop: Proportion of data to use as test set , defaults to 0.2
    :type test_prop: float, optional
    :param combine: Whether to join Datasets into ConcatDataset, defaults to False
    :type combine: bool, optional
    :raises ValueError: Errors if user requests to combine datasets but there is only one. This is probability misinformed and should raise an error.
    :return: Training, validation and test datasets, respectively
    :rtype: Tuple[Dataset, Dataset]
    """    
    if combine and len(datafiles) == 1:
        raise ValueError('Cannot combine datasets when number of datafiles == 1.')

    if len(datafiles) == 1:
        return generate_single_dataset(
            datafiles[0],
            labelfiles[0],
            class_label,
            test_prop,
            *args,
            **kwargs,
        )

    train_datasets, val_datasets, test_datasets = [], [], []

    for datafile, labelfile in zip(datafiles, labelfiles):
        train, val, test = generate_single_dataset(
            datafile,
            labelfile,
            class_label,
            test_prop,
            *args,
            **kwargs,
        )

        train_datasets.append(train)
        val_datasets.append(val)
        test_datasets.append(test)

    # Flexibility to generate single stratified dataset from a single file 
    # Just in generate_single_dataset
    if combine:
        train_datasets = ConcatDataset(train_datasets)
        val_datasets = ConcatDataset(val_datasets)
        test_datasets = ConcatDataset(test_datasets)

    return train_datasets, val_datasets, test_datasets

def generate_single_dataset(
    datafile: str,
    labelfile: str,
    class_label: str,
    test_prop=0.2,
    sep=',',
    *args,
    **kwargs,
) -> Tuple[Dataset, Dataset, Dataset]:
    """
    Generate a train/test split for the given datafile and labelfile.

    :param datafile: Path to dataset csv file
    :type datafile: str
    :param labelfile: Path to label csv file 
    :type labelfile: str
    :param class_label: Column (label) in labelfile to train on 
    :type class_label: str
    :param test_prop: Proportion of dataset to use in val/test, defaults to 0.2
    :type test_prop: float, optional
    :return: train, val, test Datasets
    :rtype: Tuple[Dataset, Dataset, Dataset]
    """    
    current_labels = pd.read_csv(labelfile, sep=sep).loc[:, class_label]
    suffix = pathlib.Path(datafile).suffix

    # Make stratified split on labels
    trainsplit, valsplit = train_test_split(current_labels, stratify=current_labels, test_size=test_prop)
    trainsplit, testsplit = train_test_split(trainsplit, stratify=trainsplit, test_size=test_prop)

    if suffix == '.h5ad' or suffix == '.h5':
        data = (
            sc.read_h5ad(datafile) if suffix == '.h5ad' else sc.read_h5(datafile)
        )
        train, val, test = (
            NumpyStream(
                matrix=data.X[split.index],
                labels=split.values,
                class_label=class_label,
                *args,
                **kwargs,
            )
            for split in [trainsplit, valsplit, testsplit]
        )
    else:
        if suffix != '.csv' or suffix != '.tsv':
            warnings.warn(f'Interpreting {suffix = } for {datafile = } as delimited text file')

        train, val, test = (
            CSVData(
                filename=datafile,
                labelname=labelfile,
                class_label=class_label,
                indices=indices,
                *args,
                **kwargs,
            )
            for indices in [trainsplit, valsplit, testsplit]  
        )

    return train, val, test 

def generate_single_dataloader(
    *args,
    **kwargs,
) -> Tuple[CollateLoader, CollateLoader, CollateLoader]:
    """
    Generates a train, val, test CollateLoader

    :return: train, val, test loaders
    :rtype: Tuple[CollateLoader, CollateLoader, CollateLoader]
    """

    train, val, test = generate_single_dataset(
        *args,
        **kwargs,
    )

    loaders = (
        CollateLoader(
                dataset=dataset, 
                *args,
                **kwargs,
            )
        for dataset in [train, val, test]
    )

    return loaders 

def generate_dataloaders(
    datafiles: List[str], 
    labelfiles: List[str],
    collocate: bool=True, 
    *args,
    **kwargs,
) -> Union[Tuple[List[CollateLoader], List[CollateLoader], List[CollateLoader]], Tuple[SequentialLoader, SequentialLoader, SequentialLoader]]:
    """
    Generates DataLoaders for training, either as a combined list from each datafile or a SequentialLoader to allow sequentially sampling between DataLoaders or DataLoader derived classes.

    :param datafiles: List of absolute paths to datafiles
    :type datafiles: List[str]
    :param labelfiles: List of absolute paths to labelfiles
    :type labelfiles: List[str]
    :param collocate: Whether to combine DataLoaders into one SequentialLoader to allow sequential sampling from all continuously, defaults to True
    :type collocate: bool, optional
    :raises ValueError: Errors if num(labelfiles) != num(datafiles)
    :raises ValueError: Errors if user requests to collocate but only one loader is passed -- probably misinformed 
    :return: Either lists containing train, val, test or SequentialLoader's for train, val, test 
    :rtype: Union[Tuple[List[CollateLoader], List[CollateLoader], List[CollateLoader]], Tuple[SequentialLoader, SequentialLoader, SequentialLoader]]
    """
    
    if len(datafiles) != len(labelfiles):
        raise ValueError("Must have same number of datafiles and labelfiles")
    
    if not collocate and len(datafiles) > 1:
        warnings.warn(f"{collocate =}, so multiple files will return multiple DataLoaders and cannot be trained sequentially with PyTorch-Lightning")

    train, val, test = [], [], []
    for datafile, labelfile in zip(datafiles, labelfiles):
        trainloader, valloader, testloader = generate_single_dataloader(
            datafile=datafile,
            labelfile=labelfile,
            *args,
            **kwargs,
        )

        train.append(trainloader)
        val.append(valloader)
        test.append(testloader)

    if len(datafiles) == 1:
        train = train[0]
        val = val[0]
        test = test[0]

    if collocate and len(datafiles) > 1:
        # Join these together into sequential loader if requested, shouldn't error if only one training file passed, though
        train, val, test = SequentialLoader(train), SequentialLoader(val), SequentialLoader(test)

    return train, val, test 

def calculate_intersection(*lists: List[Any]):
    """
    Calculate set intersection of input lists

    :param lists: Arbitrary number of list-like to calculate intersection from
    """

    if len(lists) == 1:
        return lists
    else:
        res = set(lists[0]).intersection(lists[1:])
        return sorted(list(res))