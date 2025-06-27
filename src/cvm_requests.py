import requests
import logging
from abc import ABC, abstractmethod


class CvmRequest(ABC):
    @abstractmethod
    def get_cvm_data(self, **kwargs) -> requests.Response:
        pass


class GetItrDfpBovespa(CvmRequest):
    def __init__(self, year: int):
        self.year = year
        self.url = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC"
        self.params = {
            "dfp" : self.url + f"/DFP/DADOS/dfp_cia_aberta_{self.year}.zip",
            "itr" :self.url + f"/ITR/DADOS/itr_cia_aberta_{self.year}.zip"
        }
    

    def get_dfp(self):
        return self.get_cvm_data(self.params["dfp"])


    def get_itr(self):
        return self.get_cvm_data(self.params["itr"])
    

    def get_cvm_data(self, url):
        try:
            response = requests.get(url)
            if response.status_code != 200:
                logging.error(f"Request on {url} failed - Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Request on {url} failed - {e}")

        return response._content