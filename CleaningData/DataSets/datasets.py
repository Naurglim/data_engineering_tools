import pandas as pd
import json
import os

BASE_PATH = 'CleaningData/DataSets/'

#recibe dataset por parámetro y devuelve el json del mismo nombre:
def get_dataset(dataset_name, dataset_version = '1'):
    """
    ----
    Get dataset with matching name and version from the available .json files.
    If dataset does not exist return an empty dataframe. 
    ----
    """
    # Si el archivo no existe, cargo un dataframe vacío:
    filename = os.path.join(BASE_PATH, dataset_name, dataset_version + '.json')
    if os.path.isfile(filename):
        with open(filename) as json_file:
            json_data = json.load(json_file)
    else:
        json_data = {}

    # converting json dataset from dictionary to dataframe
    dt = pd.DataFrame(json_data)
    dt.reset_index(level=0, inplace=True)

    return dt


