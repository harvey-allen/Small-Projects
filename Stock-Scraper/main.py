import requests
import pandas as pd
from bs4 import BeautifulSoup

def getStockData(symbol, temp = [], table = {}):
    flag = True
    values = ["Shs Outstand", "Market Cap", "Shs Float", "Avg Volume"]
    output = [["Stock Symbol", "Outstanding Shares", "Market Capital", "Shares Float", "Average Volume"]]
    url = 'https://finviz.com/quote.ashx?t='
    response = requests.get(url+symbol)
    soup = BeautifulSoup(response.text, 'html.parser')
    posts = soup.select('.table-dark-row')
    for post in posts:
        for tableData in post.find_all("td"):
            temp.append(tableData.get_text())
    table["Symbol"] = symbol
    for i in range(len(temp)):
        if temp[i] in values:
            table[temp[i]] = temp[i+1]
    output.append(list(table.values()))
    stockData = pd.DataFrame(output[1:], columns=output[0])
    print(stockData)

getStockData("FB")
