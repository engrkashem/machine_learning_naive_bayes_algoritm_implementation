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
trained_data = {}
total_data = len(resData)
total_yes = 0
for item in resData:
    if item == 'yes':
        total_yes += 1

for weatherName in weatherData.columns:
    unique_list = np.unique(weatherData[weatherName])

    for weatherStatus in unique_list:
        cntYes = 0
        cnt = 0
        for i in range(len(weatherData[weatherName])):
            if weatherStatus == weatherData[weatherName][i] and resData[i] == 'yes':
                cntYes += 1
            if weatherStatus == weatherData[weatherName][i]:
                cnt += 1
        trained_data[weatherStatus] = {
            'p': cntYes, 'np': cnt-cntYes, 'tp': cnt}


# Testing
test = ["Rainy", "Hot", "Normal", "yes"]
# for played
sum_nom_played = total_yes/total_data
sum_denom_played = 1
for weatherStatus in test:
    sum_nom_played *= trained_data[weatherStatus]['p']/total_yes
    sum_denom_played *= trained_data[weatherStatus]['tp']/total_data
sum_played = sum_nom_played/sum_denom_played
# for not played
total_no = total_data-total_yes
sum_nom_not_played = total_no/total_data
sum_denom_not_played = 1
for weatherStatus in test:
    sum_nom_not_played *= trained_data[weatherStatus]['np']/total_no
    sum_denom_not_played *= trained_data[weatherStatus]['tp']/total_data
sum_not_played = sum_nom_not_played/sum_denom_not_played
print(sum_played, sum_not_played)
naive_bayes.test_model(test)
