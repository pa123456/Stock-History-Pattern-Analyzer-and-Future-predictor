import datetime as dt
import pandas as pd
import pandas_datareader.data as web

end = dt.datetime.today()
start = dt.datetime.now() - dt.timedelta(days=30)


def getdata(symbol):
    try:
        df = web.DataReader(symbol, "yahoo", start, end)
    except:
        raise
        return False
    return 
        

def main():
    getdata("6SPC")


if __name__ == '__main__':
    main()

