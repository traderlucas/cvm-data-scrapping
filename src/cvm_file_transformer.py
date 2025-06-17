import logging
import pandas as pd
from abc import ABC, abstractmethod

class CvmFileTransformer(ABC):
    @abstractmethod
    def rename_cvm_file_columns(self, df_cvm_file: pd.DataFrame) -> pd.DataFrame:
        pass

class CvmFileTransformerDre(CvmFileTransformer):
        def __init__(self, column_mapping: dict, keep_columns: list):
             self.column_mapping = column_mapping
             self.keep_columns = keep_columns


        def rename_cvm_file_columns(self, df_cvm_file: pd.DataFrame) -> pd.DataFrame:
            column_mapping = self.column_mapping
            keep_columns = self.keep_columns

            df_cvm_file_transformed = df_cvm_file.rename(columns=column_mapping)[keep_columns]
            

            return df_cvm_file_transformed