from typing import ClassVar
import torch
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
import pytorch_lightning as pl
import numpy as np

from typing import Union, List, Dict, Any, Optional, cast


def split_data(
        X : np.array, 
        y : np.array,
        test_size : float = 0.1,
        X_test : Optional[np.array] = None,
        y_test : Optional[np.array] = None,
        random_state : int = 0
):
    """
    batch_size : Size of each batch.
    X, y : Data and label for your experiment
    
    test_size : split ratio of the data.  (# train : # val : # test = 1-2* test_size : test_size : test_size) if (X_test, y_test) = (None, None)
                                          (# train : # val = 1-test_size : test_size) if X_test and y_test are specified.
    random_state : random_state in splitting the data.
    """
    if (X_test is None and y_test is not None) or (X_test is not None and y_test is None):
        raise ValueError("X_test and y_test should both be specified as a certain np.array object, or else all be NoneType objects.")

    elif X_test is None and y_test is None:
        X_train, X_test, y_train, y_test = train_test_split(
                X,
                y, 
                test_size=test_size, 
                random_state=random_state, 
                stratify=y
            ) 
    else:
        X_train, y_train = X, y

    X_predict_tensor = torch.Tensor(X_train)
    y_predict_tensor = torch.Tensor(y_train)
    X_test_tensor = torch.Tensor(X_test)
    y_test_tensor = torch.Tensor(y_test)

   
    X_train, X_val, y_train, y_val = train_test_split(
        X_train,
        y_train,
        random_state=0,
        stratify=y_train
    )
    
    
    X_train_tensor = torch.Tensor(X_train)
    y_train_tensor = torch.Tensor(y_train)
    X_val_tensor = torch.Tensor(X_val)
    y_val_tensor = torch.Tensor(y_val)

    return X_train_tensor, y_train_tensor, X_val_tensor, y_val_tensor, X_predict_tensor, y_predict_tensor, X_test_tensor, y_test_tensor 


class DataModule(pl.LightningDataModule):
    def __init__(
        self,
        batch_size : int, 
        X : np.array, 
        y : np.array,
        X_val : Optional["np.ndarray"] = None,
        y_val : Optional["np.ndarray"] = None,
        X_test : Optional["np.ndarray"] = None,
        y_test : Optional["np.ndarray"] = None,
        test_size : float = 0.1,
        random_state : int = 0
    ) -> None:

        """
        batch_size : Size of each batch.
        X, y : Data and label for your experiment
        X_test, y_test : Separate dataset for testing define this only if there is a pre-defined test set. (default = None)
        test_size : split ratio of the data. (# train : # val : # test = 1-2* test_size : test_size : test_size)
        random_state : random_state
        """
        super(DataModule, self).__init__()

        self.X = X
        self.y = y
        self.X_val = X_val
        self.y_val = y_val
        self.X_test = X_test
        self.y_test = y_test
        self.batch_size = batch_size
        self.test_size = test_size
        self.random_state = random_state

    def setup(self, stage):
        if self.X_val is not None and self.y_val is not None and self.X_test is not None and self.y_test is not None:
            self.X_train_tensor = torch.Tensor(self.X)
            self.X_val_tensor = torch.Tensor(self.X_val)
            self.X_test_tensor = torch.Tensor(self.X_test)
            self.y_train_tensor = torch.Tensor(self.y)
            self.y_val_tensor = torch.Tensor(self.y_val)
            self.y_test_tensor = torch.Tensor(self.y_test)
            self.X_predict_tensor = torch.Tensor(np.concatenate([self.X, self.X_val]))
            self.y_predict_tensor = torch.Tensor(np.concatenate([self.y, self.y_val]))
        else:
            self.X_train_tensor, self.y_train_tensor, self.X_val_tensor, self.y_val_tensor, self.X_predict_tensor, self.y_predict_tensor, self.X_test_tensor, self.y_test_tensor = split_data(
            X=self.X, 
            y=self.y,
            X_test=self.X_test,
            y_test=self.y_test,
            test_size=self.test_size,
            random_state=self.random_state
            )
        self.train_dataset = TensorDataset(self.X_train_tensor, self.y_train_tensor)
        self.val_dataset = TensorDataset(self.X_val_tensor, self.y_val_tensor)
        self.test_dataset = TensorDataset(self.X_test_tensor, self.y_test_tensor)
        self.predict_dataset = TensorDataset(self.X_predict_tensor, self.y_predict_tensor)
    
    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.batch_size, num_workers=8)
    
    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=self.batch_size, num_workers=8)
        
    def test_dataloader(self):
        return DataLoader(self.test_dataset, batch_size=self.batch_size, num_workers=8)

    def predict_dataloader(self):
        return DataLoader(self.predict_dataset, batch_size=self.batch_size, num_workers=8)






