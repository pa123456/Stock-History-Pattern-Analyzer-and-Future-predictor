from urllib.request import urlretrieve
import pandas as pd
import numpy as np

def msnget(stockname,period='1y'):
    #Get raw data from msn money history

    url = 'http://finance.services.appex.bing.com/Market.svc/ChartAndQuotes?symbols='+stockname.upper()+'&chartType='+period+'&isEOD=False&isCS=true&isVol=true'
    filename= stockname.upper() + '.csv'
    a = urlretrieve(url,filename)

    #Process raw data to usable data
    f = open(filename,'r')
    try:
        initdata=f.read()
        dataa=''
        (left,right,time,ist)=(0,0,0,0)
        for i in range(len(str(initdata))):
            if initdata[i]=='[':
                left+=1
                if left==3:
                    time=1
                    dataa=dataa+initdata[i]
            elif initdata[i]==']':
                right+=1
                if right==2:
                    dataa=dataa+initdata[i]
                    time=0
                    break
            elif initdata[i] == 'I' and left==3:
                ist+=1
            elif ist>0 and ist<18:
                ist+=1
            else:
                if time==1:
                    dataa=dataa+initdata[i]
        f.close()
        print(dataa)
        
        dataa = eval(dataa)
        
        df = pd.DataFrame(list())
        for key in range(6):
            ser = pd.Series(())
            for i in dataa: 
                
                ser.append(round(list(i.values())[key], 2))
            df.append(ser)
                
    except:
        raise
    

def main():
    msnget("SPX")
    

if __name__ == "__main__":
    main()


