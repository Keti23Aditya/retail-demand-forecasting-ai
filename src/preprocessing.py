import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def preprocess(df):
    df = df.sort_values('Date')
    df.set_index('Date', inplace=True)
    return df