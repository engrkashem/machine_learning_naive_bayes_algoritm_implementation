import pandas as pd
import numpy as np
from read_csv_data import read_csv_data
from naive_bayes import NaiveBayes
from loading import loading
from time import sleep

# getting data
data = read_csv_data('data.csv')
dFrame = pd.DataFrame(data)

# processing data
weatherData, resData = NaiveBayes.process_data(dFrame)

naive_bayes = NaiveBayes(weatherData, resData, dFrame)
# Training model
naive_bayes.train_model()

# Testing
while True:
    test_data_set_list = []
    print('Please Enter your weather condition')
    print('you need to choose an option that match your weather.\n')
    sleep(.1)
    # print(list(weatherData.columns))
    for unique_column in weatherData.columns:
        # print(unique_column)
        column_data = list(np.unique(dFrame[unique_column]))
        print(f'Please choose an option from {unique_column}')
        for index in range(len(column_data)):
            print(f'{index}. {column_data[index]}')
        inp = None
        while True:
            inp = int(input())
            if inp < 0 or inp >= len(column_data):
                print('Error Occured. Your input is out of range. Enter option again.')
            else:
                break
        test_data_set_list.append(column_data[inp])
    sleep(.1)
    print(f'\n\nYour Test Data Set is: {test_data_set_list}\n')
    sum_played, sum_not_played = naive_bayes.test_model(test_data_set_list)
    print('Predicting.', end="")
    loading()
    print(
        f'The probability of Playing Game is: {round(sum_played*100)}% and Abandond Match is: {round(sum_not_played*100)}%\n\n')
    sleep(.1)
    if sum_played > sum_not_played:
        print(f'WOW... Weather is Good. Please start the Match..!\n\n')
    else:
        print(f"OOPS... Weather is not so Good. Can't start the Match..!\n\n")
    status = input('Want to Predict Again? (y/n)')
    if status == 'n' or status == 'N':
        break
