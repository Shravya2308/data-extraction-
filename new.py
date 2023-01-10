import pandas as pd
from selenium import webdriver
import time
import pickle
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
exceldata = pd.read_csv("Sheet1.csv")
for idx in exceldata.index:
    driver.get(exceldata['URL'][idx])
    start = time.time()
    initialScroll = 0
    finalScroll = 1000
    while True:
        driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
        initialScroll = finalScroll
        finalScroll += 1000
        # time.sleep(1)
        end = time.time()
        if round(end-start)>20:
            break
    src = driver.page_source
    soup = BeautifulSoup(src,'html.parser')
    title = soup.title.string
    content = soup.find('div',{'class': 'td-post-content'})
    content = content.get_text()
    # print('title',title,
    #     'content',content.get_text()
    total = title + content
    f = open(f"{exceldata['URL_ID'][idx]}.txt", "w",encoding="utf-8")
    f.writelines(total)
            

    # with open(f"{exceldata['URL_ID'][idx]}.txt",'wb') as f:
    #     pickle.dump(total,f)