import numpy as np
from time import sleep


class NaiveBayes:
    def __init__(self, weatherData, resData, dFrame) -> None:
        self.weatherData = weatherData
        self.resData = resData
        self.dFrame = dFrame
        self.trainedData = {}
        self.totalData = len(self.resData)
        self.totalYes = 0

    # data processing
    @staticmethod
    def process_data(dFrame):
        print('Now Data is processing..', end='')
        sleep(.2)
        print('.', end='')
        sleep(.2)
        print('.', end='')
        sleep(.2)
        print('.', end='')
        sleep(.2)
        print('.', end='')
        sleep(.2)
        print('.', end='')
        sleep(.2)
        print('.', end='')
        sleep(.2)
        print('.\n')
        sleep(.2)
        weatherData = dFrame.drop(dFrame.columns[-1], axis=1)
        res_data = dFrame[dFrame.columns[-1]]
        print('Data has been processed successfully..\n')
        sleep(.4)
        return weatherData, res_data

    # Model Training
    def train_model(self):
        print('Training your Model in running..', end='')
        sleep(.2)
        print('.', end='')
        sleep(.2)
        print('.', end='')
        sleep(.2)
        print('.', end='')
        sleep(.2)
        print('.', end='')
        sleep(.2)
        print('.', end='')
        sleep(.2)
        print('.', end='')
        sleep(.2)
        print('.\n')
        sleep(.2)
        for item in self.resData:
            if item == 'yes':
                self.totalYes += 1

        for weatherName in self.weatherData.columns:
            unique_list = np.unique(self.weatherData[weatherName])

            for weatherStatus in unique_list:
                cntYes = 0
                cnt = 0
                for i in range(len(self.weatherData[weatherName])):
                    if weatherStatus == self.weatherData[weatherName][i] and self.resData[i] == 'yes':
                        cntYes += 1
                    if weatherStatus == self.weatherData[weatherName][i]:
                        cnt += 1
                self.trainedData[weatherStatus] = {
                    'p': cntYes, 'np': cnt-cntYes, 'tp': cnt}
        print('Done. Now your Model is ready to TEST..\n')
        sleep(.4)

    # Model testing
    def test_model(self, testDataSetList):
        print('Testing you model...')
        # for played condition
        sum_nom_played = self.totalYes/self.totalData
        sum_denom_played = 1
        for weatherStatus in testDataSetList:
            sum_nom_played *= self.trainedData[weatherStatus]['p'] / \
                self.totalYes
            sum_denom_played *= self.trainedData[weatherStatus]['tp'] / \
                self.totalData
        sum_played = sum_nom_played/sum_denom_played

        # for not played condition
        total_no = self.totalData-self.totalYes
        sum_nom_not_played = total_no/self.totalData
        sum_denom_not_played = 1
        for weatherStatus in testDataSetList:
            sum_nom_not_played *= self.trainedData[weatherStatus]['np']/total_no
            sum_denom_not_played *= self.trainedData[weatherStatus]['tp'] / \
                self.totalData
        sum_not_played = sum_nom_not_played/sum_denom_not_played

        print(sum_played, sum_not_played)
