from taipy import Gui
import requests
import json

project_name="Stock Simulator By Varad Acharya"
image_path="./logo.png"

data=""
with open("stockInfo.json","r") as f:
    data=json.load(f)

company_name="IBM"
# print(company_name)

open_price=[]
close_price=[]
high_price=[]
low_price=[]
volume=[]

for i,j in data["Time Series (5min)"].items():
    open_price.append(float(j['1. open']))
    high_price.append(float(j['2. high']))
    low_price.append(float(j['3. low']))
    close_price.append(float(j['4. close']))
    volume.append(int(j['5. volume']))

dataFrame={
    "COMPANY":company_name,
    "OPEN":open_price,
    "HIGH":high_price,
    "LOW":low_price,
    "CLOSE":close_price,
    "VOLUME":volume
}

page="""
<|{image_path}|image|>

# <|{project_name}|text|format=%.2f|hover_text="Welcome to our Varad Simulator"|>

Name of the Stock : <|{company_name}|input|>

<|{dataFrame}|chart|type=line|title=Stock Price|x=COMPANY|y[1]=OPEN|y[2]=HIGH|y[3]=LOW|y[4]=CLOSE|y[5]=VOLUME|>

"""

Gui(page).run(use_reloader=True)