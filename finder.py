from getdata import getdata
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
style.use('ggplot')


def main():
    # loop
    while 1:
        while 1:
            days = input("How many days do you want to check? (integar between 2 and 7)    ")
            if 2 <= int(days) <= 7:
                break
            print("Input error  Please try again")
        # Pickle load matching map        
        with open("som" + days + ".pickle", "rb") as f:
            som = pickle.load(f)
            
         with open("date" + days + ".pickle", "rb") as f:
            dateMap = pickle.load(f)
            
        df = getdata("^GSPC")
        if df == False:
            print("Failed to download data. Try again later")
            continue
        
        coord = som.winner(df.iloc[-days:]) # a x y coord
        
        # get dates
        dates = dateMap[coord]
        
        # show graph
        data = pd.read_csv("^GSPC.csv")
        X, y, date = sample_data(df=data, period=1)
        
        for z in dates:
            for i in range(len(date)):
                if date[i] == z:
                    ind = i
                    break
            fig, axes = plt.subplots(nrows=1, ncols=1)
            candlestick_ohlc(axes, X[i], width=0.7, colorup='g')


def sample_data(df, period=3):
    df.drop(['Adj Close'], axis=1,inplace=True)
    for i in range(len(df) - period + 1):
        sc = MinMaxScaler(feature_range = (0, 1))
        try:
            X = np.vstack((X, sc.fit_transform(df.iloc[i:i+period, 1:5].as_matrix().reshape((-1,1))).ravel()))
        except UnboundLocalError:
            X = sc.fit_transform(df.iloc[i:i+period, 1:5].as_matrix().reshape((-1,1))).ravel()
    X = X[:-1]
    y = np.array(df['Close'].rolling(2).apply(lambda arr: arr[-1] > arr[0]).drop(0).iloc[period-1:]) # 1 For up
    date = np.array(df['Date'].iloc[period-1:])
    return X, y, date


if __name__ == "__main__":
    main()

