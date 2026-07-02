import pandas as pd
from utilies import *

DATA_ROOT_PATH = PROJECT_ROOT_PATH / "src" / "data"

dataframes = {}

data_entities = yaml_loader(PROJECT_ROOT_PATH / "src" / "dataEntities.yaml").get('dataEntities', [])



for entity in data_entities:
    entity_details = get_entity_details(entity)

    if entity_details.get('format') == 'csv':
        dataframes[entity] = csv_loader(entity_details.get('location'))
    else:
        dataframes[entity] = 'entity'

print(dataframes.keys())