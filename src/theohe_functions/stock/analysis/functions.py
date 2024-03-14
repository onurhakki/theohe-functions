
import ta
import pandas as pd

def add_emas(df, windows = [20,50,100, 200],inplace=True):
    if inplace == False:
        values = list()
    for w in windows:
        val = ta.trend.ema_indicator(df["close"], w)
        if inplace == True:            
            df.loc[:,"ema_{}".format(w)] = val
        else:
            values.append(val)
    if inplace == True:
        return df
    else:
        res = pd.concat(values, axis = 1)
        res.columns = ["ema_{}".format(w) for w in windows]
        return res

def add_rsi(df, windows = [14], inplace=True):
    if inplace == False:
        values = list()
    for w in windows:
        val = ta.momentum.rsi(df["close"], w)
        if inplace == True:            
            df.loc[:,"rsi_{}".format(w)] = val
        else:
            values.append(val)
    if inplace == True:
        return df
    else:
        res = pd.concat(values, axis = 1)
        res.columns = ["rsi_{}".format(w) for w in windows]
        return res

def add_stochrsi(df, windows = [14], inplace=True):
    if inplace == False:
        values = list()
    for w in windows:
        val = ta.momentum.stochrsi(df["close"], w)*100
        if inplace == True:            
            df.loc[:,"stochrsi_{}".format(w)] = val
        else:
            values.append(val)
    if inplace == True:
        return df
    else:
        res = pd.concat(values, axis = 1)
        res.columns = ["stochrsi_{}".format(w) for w in windows]
        return res



def add_min_max(df, windows = [200], inplace=True):
    if inplace == False:
        values = list()
    functions = ["min", "max"]
    for func in functions:
        for w in windows:
            val = getattr(df["close"].rolling(w),func)()
            if inplace == True:            
                df.loc[:,"{}_{}".format(func,w)] = val
            else:
                values.append(val)
    if inplace == True:
        return df
    else:
        res = pd.concat(values, axis = 1)
        res.columns = ["{}_{}".format(func,w) for w in windows for func in functions]
        return res


def trend_up(x, windows):
    if x["ema_{}".format(windows[3])] < x["ema_{}".format(windows[2])] and x["ema_{}".format(windows[2])] < x["ema_{}".format(windows[1])] and x["ema_{}".format(windows[1])] < x["ema_{}".format(windows[0])]:
        return True
    else:
        return False

def add_trend(df, windows = [20,50,100,200], inplace=True):
    for w in windows:
        if "ema_{}".format(w) not in df:
            print("ema_{} missing. (window = {})".format(w,w))
            return
    
    val = df.apply(lambda x: trend_up(x, windows=windows),axis = 1)
    val.name = "trend_up"
    if inplace == True:
        df.loc[:,"trend_up"] = val
        return df
    else:
        return val
    


def add_fibo(df, window = 200, inplace=True, remove_min_max = True):
    if "min_{}".format(window) not in df or "max_{}".format(window) not in df:
        print("Min-Max missing. (window = {})".format(window))
        return
    
    val = pd.DataFrame(
        index = df.index,
        data = df.loc[:,
                        ["min_{}".format(window),"max_{}".format(window)]
                        ].apply(lambda x:
                                [x["min_{}".format(window)] + 
                                (x["max_{}".format(window)] - x["min_{}".format(window)])*f
                                for f in [0,0.236, 0.382, 0.5, 0.618, 0.786, 1]],axis = 1).tolist())
    val = val.bfill()
    val.columns = [
        "fl{:.1f}".format(f).replace(".","")
        for f in [0,0.236, 0.382, 0.5, 0.618, 0.786, 1]
        ]

    if inplace == True:            
        for n in val:
            df.loc[:,n] = val[n]
        
        if remove_min_max == True:
            df.drop(["min_{}".format(window),
                     "max_{}".format(window)],axis = 1, inplace=True)
        return df
    else:
        return val



