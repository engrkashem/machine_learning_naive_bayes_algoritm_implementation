import pandas as pd
import numpy as np
from read_csv_data import read_csv_data
from naive_bayes import NaiveBayes

# getting data
data = read_csv_data('data.csv')
dFrame = pd.DataFrame(data)
# print(df)


weatherData, resData = NaiveBayes.process_data(dFrame)
naive_bayes = NaiveBayes(weatherData, resData, dFrame)
naive_bayes.train_model()

# Training model


# Testing
test = ["Rainy", "Hot", "Normal", "yes"]

naive_bayes.test_model(test)
