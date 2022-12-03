import pandas as pd
import numpy as np
from read_csv_data import read_csv_data
from naive_bayes import NaiveBayes

# getting data
data = read_csv_data('data.csv')
dFrame = pd.DataFrame(data)

# processing data
weatherData, resData = NaiveBayes.process_data(dFrame)

naive_bayes = NaiveBayes(weatherData, resData, dFrame)
# Training model
# naive_bayes.train_model()

# Testing
test_data_set_list = []
print('Please Enter your weather condition')
print('you need to choose an option that match your weather.\n')
for unique_column in weatherData.columns:
    column_data = list(np.unique(dFrame[unique_column]))
    print(f'Please choose an option from {unique_column}')
    for index in range(len(column_data)):
        print(f'{index}. {column_data[index]}')

    print(column_data)
# naive_bayes.test_model(test_data_set_list)
# print(resData.name)
