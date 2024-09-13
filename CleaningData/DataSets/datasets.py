import pandas as pd
import json
import os

BASE_PATH = 'CleaningData/DataSets/'

#recibe dataset por parámetro y devuelve el json del mismo nombre:
def get_dataset(dataset_name, dataset_version = '1'):

    # Armo la ruta del archivo que contiene la version del dataset requerido:
    filename = os.path.join(BASE_PATH, dataset_name, dataset_version + '.json')
    # filename = dataset_name + '.json'
    with open(filename) as json_file:
        json_data = json.load(json_file)

    # converting json dataset from dictionary to dataframe
    dt = pd.DataFrame(json_data)
    dt.reset_index(level=0, inplace=True)

    return dt


