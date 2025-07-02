from handler import EarningsExtractLoad
from cvm_requests import ItrRequest, DfpRequest


def main(year):
    handler = EarningsExtractLoad(bucket="cvmearningsdata")

    for doc_type in [ItrRequest, DfpRequest]:
        doc_type = doc_type(year)
        handler.extract_load(doc_type)
        print(year, "concluded")


if __name__ == "__main__":
    start = int(input())
    end = int(input())
    for i in range(start, end):
        main(i)