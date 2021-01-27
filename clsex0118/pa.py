import requests
import re
import time
import os

#<meta name="description" content="小清新的女生，清纯的容颜，美好的意境。第一眼就映入我们眼帘的是那一抹笑颜，它深深的印刻在我们的脑海里。">
response = requests.get('https://www.bizhizu.cn/bizhi/10948.html')

html = response.text
dir_name = re.findall('<meta name="description" content="(.*?)">', html)[-1]
print(dir_name)
if not os.path.exists(dir_name):
   os.mkdir(dir_name)
urls = re.findall('src="(.*?)" width=".*?"', html)
print(urls)
for url in urls:
    time.sleep(1)
    file_name = url.split('/')[-1]
    response = requests.get(url)
    with open(dir_name + '/' + file_name, 'wb') as f:
        f.write(response.content)
