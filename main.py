from src.handler import EarningsExtractLoad
from src.cvm_requests import ItrRequest, DfpRequest


def main(year):
    handler = EarningsExtractLoad(bucket="cvmearningsdata")

    for doc_type in [ItrRequest, DfpRequest]:
        doc_type = doc_type(year)
        handler.extract_load(doc_type)

if __name__ == "__main__":
    for i in range(2010, 2023):
        main(i)
        print(i, "concluded")