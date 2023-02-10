import pandas as pd
import os

def get_temp_data():
    '''
    This function is to acquire the people data from a local csv
    '''
    
    if os.path.isfile('GlobalLandTemperaturesByCountry.csv'):
        
        return pd.read_csv('GlobalLandTemperaturesByCountry.csv')