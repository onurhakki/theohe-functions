from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import yfinance as yf
from ...timeframe.get_frame import timeFrame

from datetime import datetime, timedelta


def bist_kap(verify = True, to_excel=False):
    main_url = "https://www.kap.org.tr/tr/Endeksler"
    url_main = requests.get(main_url, verify=verify)

    soup_bist = BeautifulSoup(url_main.content, features="lxml")
    
    ola1 = soup_bist.find("div", {"id": "printAreaDiv"}).find_all("div", {"class": "column-type1"})
    ola2 = soup_bist.find("div", {"id": "printAreaDiv"}).find_all("div", {"class": "column-type7"})
    
    main_store = dict()
    for i,j in zip(ola1, ola2):
        name = i.find("div").text
        store = list()
        for k in j.find_all("div", {"class","w-clearfix"}):
            val = k.find_all("a")
            if len(val) != 0:
                row = list()
                for l in val:
                    row.append(l.text)
                row.append("https://www.kap.org.tr" + l.get("href"))
                store.append(row)
        main_store[name] = pd.DataFrame(store, columns = ["no", "tag", "name", "href"])
    
    if to_excel:
        with pd.ExcelWriter('endeksler.xlsx') as writer:
            end = pd.Series(list(main_store.keys()))
            end.name = "Endeksler"
            end.to_excel(writer, sheet_name="Endeksler", index = False)
            for k,v in main_store.items():
                v.to_excel(writer, sheet_name=k, index = False)
    
    return main_store

        
def yf_data_download(tag, frame, progress=False):
    start, end, interval = frame

    result = yf.download(tag, start=start , end=end, interval=interval, progress=progress)
    result = result.rename(columns = {
        "Low":"low",
        "High":"high",
        "Close": "close",
        "Open": "open",
        "Volume": "volume",
        "Adj Close": "adj_close"
        })
    return result


def yf_data_multiframe_download(columns):
    now = datetime.now()
    m, w, d = now.strftime("%Y-%m-01"), (now - timedelta(days = now.weekday() + 1)).strftime("%Y-%m-%d"), (now - timedelta(days=1)).strftime("%Y-%m-%d")

    month_frame = timeFrame().get_three_year_frame(resolution="1mo")
    week_frame = timeFrame().get_three_year_frame(resolution="1wk")
    day_frame = timeFrame().get_three_year_frame(resolution="1d")

    df_month = yf_data_download(columns, frame = month_frame)
    df_week = yf_data_download(columns, frame = week_frame)
    df_day = yf_data_download(columns, frame = day_frame)
    return (df_month, df_week, df_day)



def crypto_format(result):
    res = result.copy()
    try:
        if res["s"] == "ok":
            res.pop("s")
            df = pd.DataFrame.from_dict(res)
            df["t"] = df["t"].apply(datetime.fromtimestamp)
            df = df.rename(columns = {"t":"date","h":"high","o":"open","l":"low","c":"close","v":"volume"})
            df = df.set_index("date")
            return df
        
        else:
            print(res["s"])
            return None
    except Exception as e:
        print(e)
        return None

def crypto_data_download(tag, frame):
    from_, to_, resolution = frame
    base = "https://graph-api.btcturk.com"
    method = "/v1/klines/history?from={}&resolution={}&symbol={}&to={}".format(
        from_, resolution, tag, to_ 
    )
    url = base+method
    result = requests.get(url=url)
    result = result.json()
    formatted_result = crypto_format(result)
    return formatted_result