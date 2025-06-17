import requests
import logging
from abc import ABC, abstractmethod


class CvmRequest(ABC):
    @abstractmethod
    def get_cvm_data(self, **kwargs) -> requests.Response:
        pass


class CvmRequestListedCompanies(CvmRequest):
    def __init__(self, year: int, is_annual: bool):
        self.year = year
        self.is_annual = is_annual
        self.base_url = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC"

    def get_cvm_data(self, **kwargs) -> requests.Response:
        year = self.year
        is_annual = self.is_annual
        url = self.base_url + f"/DFP/DADOS/dfp_cia_aberta_{year}.zip" if is_annual else self.base_url + f"/ITR/DADOS/itr_cia_aberta_{year}.zip"

        try:
            response = requests.get(url)

            if response.status_code != 200:
                logging.error(
                    f"Request on {url} failed - Status code: {response.status_code}"
                )


        except requests.exceptions.RequestException as e:

            raise RuntimeError(f"Request on {url} failed - {e}")

        return response