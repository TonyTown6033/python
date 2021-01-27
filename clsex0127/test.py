import requests
import time
import os
import re

url = 'https://www.bizhizu.cn/photoview/2567/3.html'
response = requests.get(url)
html = response.text
file=open('html.txt','w')
file.write(html)
file.close()
response = requests.get('https://uploadfile.bizhizu.cn/2014/0807/20140807110113429.jpg.source.jpg')
with open('ll.jpg','wb') as f:
    f.write(response.content)
