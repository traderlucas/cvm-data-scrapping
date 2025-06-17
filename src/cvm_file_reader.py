import io
import logging
import pandas as pd
import zipfile
from abc import ABC, abstractmethod

from src.cvm_requests import CvmRequest


class CvmFileReader(ABC):
    @abstractmethod
    def exctract_cvm_files(self, cvm_request: CvmRequest) -> pd.DataFrame:
        pass


class CvmFileReaderDre(CvmFileReader):
    def __init__(self, cvm_request: CvmRequest):
        self.cvm_request = cvm_request

    def exctract_cvm_files(self, cvm_request: CvmRequest) -> pd.DataFrame:
        response = cvm_request.get_cvm_data()
        year = cvm_request.year
        prefix = "dfp" if cvm_request.is_annual else "itr"
        files = [
            f"{prefix}_cia_aberta_DRE_con_{year}.csv",
            f"{prefix}_cia_aberta_DRE_ind_{year}.csv",
        ]

        with io.BytesIO(response.content) as zip_buffer:
            df_cvm_dre = _read_zip_csv_content(zip=zipfile.ZipFile(zip_buffer, "r"), files=files, sort_columns=["CNPJ_CIA", "DT_REFER", "VERSAO", "DT_INI_EXERC"], drop_duplicates_subset=["CNPJ_CIA", "DT_REFER", "CD_CONTA"])

        return df_cvm_dre
    

def _read_zip_csv_content(zip: zipfile.ZipFile, files: list, sort_columns: list, drop_duplicates_subset: list) -> pd.DataFrame:
    try:
        df_list = [
            pd.read_csv(
                zip.open(file),
                sep=";",
                encoding="ISO-8859-1"
            )
            .sort_values(sort_columns)
            .drop_duplicates(
                subset=drop_duplicates_subset,
                keep="last"
            )
            for file in files
        ]

    except Exception as e:

        logging.error(f"Error reading csv files in zip file: {e}")


    df = pd.concat(df_list, ignore_index=True)

    return df