import requests
import time
import re
import os

for num in range(65000,66000):

    url1 = 'https://www.bizhizu.cn/bizhi/'+str(num)+'/'
    url1 = url1.replace('bizhi/','photoview/')
    end='.html'
    urls1=[]
    urls2=[]

    for i in range(10):
        url=url1+str(i)+end
        url=str(url)
        urls1.append(url)

    for url in urls1:
    #    time.sleep(1)
        response = requests.get(url)
        html = response.text
        dir_name = re.findall('alt="(.*?)"', html)[0]
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        url = re.findall('img.*alt', html, re.DOTALL)
        url = re.findall('imgshow"><img src="(.*?)"', url[0])[0]

        response = requests.get(url)
        file_name = url.split('/')[-1]
        with open( dir_name + '/' + file_name, 'wb') as f:
            f.write(response.content)
