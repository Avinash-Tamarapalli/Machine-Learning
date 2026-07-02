from pathlib import Path
import pandas as pd
import yaml


PROJECT_ROOT_PATH = Path(__file__).resolve().parent.parent.parent


def csv_loader(file_path):
    # The separator for the bank data is ';', not ','
    dataframe = pd.read_csv(file_path, sep=";")
    return dataframe

def yaml_loader(file_path):
    """Safely loads a YAML file."""
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data