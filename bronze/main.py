from raw_to_bronze import RawToBronze


def main(year):
    transform = RawToBronze()

    for doc_type in ["ITR", "DFP"]:
        transform.raw_to_bronze(doc_type, year)


if __name__ == "__main__":
    # start = int("start year", input())
    # end = int("end year" input())
    # for i in range(2011, 2024):
        main(2024)