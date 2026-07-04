from pathlib import Path
import pandas as pd
import yaml

def csv_reader(file_path: Path, seperator: str) -> pd.DataFrame:
    """This reads a csv file into a pandas dataframe"""
    df = pd.read_csv(file_path, sep= seperator)
    return df

def yaml_reader(file_path: Path) -> dict[str: dict]:
    """Safely loads a YAML file."""
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data
