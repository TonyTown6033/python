print('pls input the code:')
num=input()
url1 = 'https://www.bizhizu.cn/bizhi/'+str(num)+'/'
url1 = url1.replace('bizhi/','photoview/')
end='.html'
urls=[]
for i in range(9):
    url=url1+str(i)+end
    url=str(url)
    urls.append(url)

print(urls)