# extraction.py

import pandas as pd

def extract_data(file_path):
    df = pd.read_csv(file_path, encoding=('ISO-8859-1'))
    return df
