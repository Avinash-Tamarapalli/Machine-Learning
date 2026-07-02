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

def get_entity_details(entity):
    data_entities_details = yaml_loader(PROJECT_ROOT_PATH / "src" / "dataEntities.yaml").get('dataEntitiesDetails', {})
    entity_details = data_entities_details.get(entity)

    format = entity_details.get('format', '')
    location = PROJECT_ROOT_PATH / entity_details.get('loc','')

    return {'format': format, 'location': location}
