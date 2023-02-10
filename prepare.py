import pandas as pd
from datetime import timedelta, datetime





def clean_df(df):
    colombia_df = df[df['Country'].str.contains('Col') == True]
    colombia_df.columns = colombia_df.columns.str.lower()

    colombia_df = colombia_df.rename(columns = {'dt':'date',
                                                'averagetemperature':'avg_temp',
                                                'averagetemperatureuncertainty':'avg_temp_uncertainty'})

    start_date = '1846-01-01'
    end_date = '2013-08-01'
    mask = (colombia_df['date'] >= start_date) & (colombia_df['date'] <= end_date)
    colombia_df = colombia_df.loc[mask]
    
    colombia_df['date'] = pd.to_datetime(colombia_df['date'])
    colombia_df.set_index('date', inplace = True)
    
    colombia_resampled = colombia_df.resample('m').mean()
    
    return colombia_df, colombia_resampled