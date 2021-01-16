import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        res = requests.get(url, timeout=30)
        res.encoding = 'gb2312'
        return res.text
    except:
        return ''

def parse_html(html):
    soup = BeautifulSoup(html,'lxml')
    tr_list=soup.find_all('tr',attrs={"bgcolor":"#FFFFFF"})
    houses = {}
    for tr in tr_list:
        house = {}
        house["详细地址"] = tr.find_all('a',\
            attrs={"target":"_blank"})[0].string
        house["详情链接"] = "https://www.lgfdcw.com/cs/" +\
            tr.find_all('a',attrs={"target":"_blank"})[0].attrs["href"]
        house["房型"] = tr.find.all("td")[2].string
        house["户型"] = tr.find.all("td")[3].string
        house["面积"] = tr.find.all("td")[4].string[:-2]+"平方米"
        house["出售价格"] = tr.find.all("td")[5].string.strip()
        house["登记时间"] = tr.find.all("td")[6].string
        houses.append(house)
    return houses

def save_file(dic):
    df = pd.DataFrame(dic,columns={"","","","","","",""})
    df.to_excel(r'D:/Code/python/clsex0116/houses.xlsx')

def main():
    html=get_html("https://www.lgfdcw.com/cs/index.php?PageNo=1")
    res=parse_html(html)
    save_file(res)

main()
