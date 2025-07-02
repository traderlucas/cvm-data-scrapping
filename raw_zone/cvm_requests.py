import requests
import logging
from abc import ABC, abstractmethod
from typing import Literal


class CvmRequest(ABC):
    base_url = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC"

    def __init__(self, year: int):
        self.year = year

    @abstractmethod
    def get_document_type(self) -> Literal["DFP", "ITR"]:
        pass

    def get_url(self) -> str:
        doc_type = self.get_document_type()
        return f"{self.base_url}/{doc_type}/DADOS/{doc_type.lower()}_cia_aberta_{self.year}.zip"

    def get_cvm_data(self) -> bytes:
        url = self.get_url()
        try:
            response = requests.get(url)
            if response.status_code != 200:
                logging.error(f"Request to {url} failed - Status code: {response.status_code}")
                return b""
            return response.content
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Request to {url} failed - {e}")


class DfpRequest(CvmRequest):
    def get_document_type(self) -> Literal["DFP"]:
        return "DFP"


class ItrRequest(CvmRequest):
    def get_document_type(self) -> Literal["ITR"]:
        return "ITR"
