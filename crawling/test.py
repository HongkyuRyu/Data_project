import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta

startnum = 1
endnum = 5

url = f'http://openapi.seoul.go.kr:8088'
params = {
    'KEY': "61626573486b797538384970536178",
    'TYPE': "xml",
    'SERVICE': "citydata",
    'START_INDEX': startnum,
    'END_INDEX': endnum,
    'AREA_NM': 13   # gasan digital
}
res = requests.get(url=url, params=params)
print(res)


x = 
y = target


x_train, x_test 7 3
from sklearn.model_selection import train_test_split
from stats.model
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=.3)







from sklearn.linear_model import Lasso

Lasso()