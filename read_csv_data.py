import pandas as pd
from time import sleep
from loading import loading


def read_csv_data(fileName):
    print('Reading data from csv.', end='')
    loading()
    sleep(.5)
    dFrame = pd.read_csv(fileName, index_col=0)
    data = dFrame.to_dict("split")
    data = dict(zip(data['index'], data['data']))
    return data
