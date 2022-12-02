import pandas as pd
import numpy as np


data = {
    "Outlook": ["Rainy", "Rainy", "Overcast", "Sunny", "Sunny", "Sunny", "Overcast", "Rainy", "Rainy", "Sunny", "Rainy", "Overcast", "Overcast", "Sunny"],
    "Temp": ["Hot", "Hot", "Hot", "Mild", "Cool", "Cool", "Cool", "Mild", "Cool", "Mild", "Mild", "Mild", "Hot", "Mild"],
    "Humidity": ["High", "High", "High", "High", "Normal", "Normal", "Normal", "High", "Normal", "Normal", "Normal", "High", "Normal", "High"],
    "Windy": ['no', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'no', 'yes'],
    "Play": ["no", "no", "yes", "yes", "yes", "no", "yes", "no", "yes", "yes", "yes", "yes", "yes", "no"]
}

# data processing
df = pd.DataFrame(data)
raw_data = df.drop(df.columns[-1], axis=1)
res_data = df[df.columns[-1]]

# Training model
for dSetName in raw_data.columns:
    unique_list = np.unique(raw_data[dSetName])

    for dName in unique_list:
        cntYes = 0
        cnt = 0
        for i in range(len(raw_data[dSetName])):
            if dName == raw_data[dSetName][i] and res_data[i] == 'yes':
                cntYes += 1
            if dName == raw_data[dSetName][i]:
                cnt += 1
        print(f'{dName}-> {cnt}, {cntYes} ')
