import csv
import time
import pandas as pd

data = {
    "Outlook": ["Rainy", "Rainy", "Overcast", "Sunny", "Sunny", "Sunny", "Overcast", "Rainy", "Rainy", "Sunny", "Rainy", "Overcast", "Overcast", "Sunny"],
    "Temp": ["Hot", "Hot", "Hot", "Mild", "Cool", "Cool", "Cool", "Mild", "Cool", "Mild", "Mild", "Mild", "Hot", "Mild"],
    "Humidity": ["High", "High", "High", "High", "Normal", "Normal", "Normal", "High", "Normal", "Normal", "Normal", "High", "Normal", "High"],
    "Windy": ['no', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'no', 'yes'],
    "Play": ["no", "no", "yes", "yes", "yes", "no", "yes", "no", "yes", "yes", "yes", "yes", "yes", "no"]
}


print("Converting dataset to csv format Started.", end=' ')
time.sleep(0.15)
print(".", end=' ')
time.sleep(0.15)
print(".", end=' ')
time.sleep(0.15)
print(".", end=' ')
time.sleep(0.15)
print(".", end=' ')
time.sleep(0.15)
print(".", end=' ')
time.sleep(0.15)
print(".", end=' ')
time.sleep(0.15)
print(".\n")
time.sleep(0.15)
dframe = pd.DataFrame.from_dict(data, orient="index")
dframe.to_csv("data.csv")
print("You CSV file is ready. Now you can train your model\n")
