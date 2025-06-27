from src.cvm_requests import GetItrDfpBovespa


def main():
    extractor = GetItrDfpBovespa(2024)
    itr = extractor.get_itr()
    dfp = extractor.get_dfp()




if __name__ == "__main__":
    main()