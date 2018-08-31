# -*- coding: utf-8 -*-
"""
import requests

Created on Fri Jul 13 16:39:49 2018

@author: T6014250


rq=requests.get('http://cybersec.hatenadiary.jp/')
rq_conv=rq.text
print(rq_conv)

"""

"""
# ダウンロード（読み込み + ローカル保存）
# ダウンロードして rss.xml というファイル名で保存する例
import requests
 
# url = 'http://it-engineer-lab.com/feed'
url = 'http://cybersec.hatenadiary.jp/'

try:
    r = requests.get(url)
    with open('rss.xml', mode='w') as f:
        f.write(r.text)
except requests.exceptions.RequestException as err:
    print(err)
"""
    
import requests
from bs4 import BeautifulSoup

xml = requests.get('http://news.yahoo.co.jp/pickup/science/rss.xml', verify=False)
soup = BeautifulSoup(xml.text, 'html.parser')
for news in soup.findAll('item'):
    print(news.title.string, news)