from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import yfinance as yf


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
