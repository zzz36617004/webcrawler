import requests
from bs4 import BeautifulSoup
from itertools import count
import pandas as ps
def bbq() :
    bbq=[]
    for page in count(start=140) : #range(140, 147):
        url = "http://changup.bbq.co.kr/findstore/findstore_ajax.asp?page=%s" % page
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        tbody_tag = soup.find('tbody')
        tr_tags = tbody_tag.find_all("tr")
        print(tr_tags)

        if len(tr_tags) <= 1:
            break

        for i, tr_tag in enumerate(tr_tags) :
           if i !=0:
               stringList =  list(tr_tag.strings)
               #print(stringList)

               name = stringList[1]
               tel = stringList[5]
               address = stringList[3]
               print(name, tel, address)
               bbq.append([name, tel, address])
    table = ps.DataFrame(bbq, columns=["name","tel","address"])
    table.to_csv("D:/javaStudy/webdata/bbq_table.csv",encoding="utf-8-sig",mode="w",index=True)

    return bbq


bbq()