import requests
response = requests.get('https://uploadfile.bizhizu.cn/2014/0807/20140807110113429.jpg.source.jpg')
with open('ll.jpg','wb') as f:
    f.write(response.content)