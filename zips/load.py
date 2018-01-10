import pandas as pd


def load_dict(filename):
    '''
    :param filename: file to load the look up table to be used in service
    :return: lookup table as dictionary
    '''
    df_zips = pd.read_csv(filename, dtype=str)
    dict_zips = df_zips.set_index('zip')['state'].to_dict()
    return dict_zips

dict_zips = load_dict("zips/zip_city_state.csv")

def state_for(zip):
    return dict_zips[zip]


