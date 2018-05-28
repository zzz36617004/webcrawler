import requests
from bs4 import BeautifulSoup
from itertools import count

def pericanaStore():
    #for page in count(start=1):
    pStoreList = []
    for page in range(1,117):
        url="http://www.pelicana.co.kr/store/stroe_search.html?page=%s" %page
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        table=soup.find("table",{"class":"table mt20"})                                     #정보를 갖고있는 테이블 하나만 가져옴
        table_tbody = table.find("tbody")
        tr_tags = table_tbody.find_all("tr")

        for tr_tag in tr_tags:
            storeData=list(tr_tag.strings)
            name = storeData[1]
            tel = (storeData[5]).strip()
            address = storeData[3]
            print(name,tel, address)
            pStoreList.append([name,tel,address])
    return pStoreList

result=pericanaStore()
print(result)