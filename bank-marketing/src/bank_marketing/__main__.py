from bank_marketing.utils.get_entities import load_data


def main():
    dataframes = load_data()
    print(dataframes.keys())


if __name__ == "__main__":
    main()