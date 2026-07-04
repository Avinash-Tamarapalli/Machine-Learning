from bank_marketing.utils.utilities import yaml_reader, csv_reader
from bank_marketing.utils.configs import PROJECT_ROOT_PATH, PACKAGE_ROOT_PATH, EntityDetails
import pandas as pd

DATA_ENTITIES_PATH = PACKAGE_ROOT_PATH / 'conf'/ 'data_entities.yaml'
DATA_ENTITIES_DETAILS_PATH = PACKAGE_ROOT_PATH / 'conf'/ 'data_entities_details.yaml'

def get_entity_list() -> list[str]:

    data = yaml_reader(DATA_ENTITIES_PATH)
    entity_list = data.get('dataEntities', [])

    return entity_list

def get_entity_details(entity) -> EntityDetails:

    data = yaml_reader(DATA_ENTITIES_DETAILS_PATH)
    entities = data.get('dataEntitiesDetails', {})

    entity_config = entities.get(entity)
    if entity_config is None:
        raise KeyError(f"Entity '{entity}' not found in {DATA_ENTITIES_DETAILS_PATH.name}")

    details = EntityDetails(**entity_config)
    details.path = PROJECT_ROOT_PATH / details.path

    return details

def read_entity(entity) -> pd.DataFrame:
    entity_details = get_entity_details(entity)
    path = entity_details.path

    df = csv_reader(file_path= path, seperator= entity_details.sep)

    return df

def load_data() -> dict[str, pd.DataFrame]:
    dataframes = {}
    entity_list = get_entity_list()

    for entity in entity_list:
        dataframes[entity] = read_entity(entity)

    return dataframes


