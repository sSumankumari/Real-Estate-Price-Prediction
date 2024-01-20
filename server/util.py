import json
import pickle
import numpy as np
import warnings
import os

warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
         
    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    columns_path = os.path.join(os.path.dirname(__file__), 'artifacts', 'columns.json')
    model_path = os.path.join(os.path.dirname(__file__), 'artifacts', 'bangalore_home_price_model.pickle')

    with open(columns_path, "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = list(set(__data_columns[3:]))  # Extract unique locations from columns (skip first 3 columns)

    global __model
    if __model is None:
        with open(model_path, "rb") as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_data_columns():
    return __data_columns
def get_location_names():
    return __locations


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())

    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))