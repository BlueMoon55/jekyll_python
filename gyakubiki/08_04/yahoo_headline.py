import requests
from bs4 import BeautifulSoup

xml = requests.get('https://cybersecurity-tokyo.jp/', verify=False)
soup = BeautifulSoup(xml.text, 'html.parser')
for news in soup.findAll('item'):
    print(news.title.string, '\n', news)
