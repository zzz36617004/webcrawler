from selenium import webdriver
from bs4 import BeautifulSoup
from itertools import count
import pandas as ps
import time
def goobneStore():
    goob = []
    wd = webdriver.Chrome("D:/javaStudy/webdriver/chromedriver.exe")
    wd.get("https://www.goobne.co.kr/store/search_store.jsp")

    for page in count(start=95):
        wd.execute_script("store.getList(%s)" % page)
        time.sleep(5)
        html = wd.page_source
        soup = BeautifulSoup(html, 'html.parser')
        tbody_tag = soup.find('tbody',{"id":"store_list"})
        tr_tags = tbody_tag.find_all("tr")
        if tr_tags[0].get("class") is None:
            break
        for tr_tag in tr_tags:
            stringList = list(tr_tag.strings)
            name = stringList[1]
            tel = stringList[3]
            address = stringList[6]
            goob.append([name, tel, address])
    table = ps.DataFrame(goob, columns=["name", "tel", "address"])
    table.to_csv("D:/javaStudy/webdata/goob_table.csv", encoding="utf-8-sig", mode="w", index=True)

    return goob
result=goobneStore()
print(result)