import urllib
from bs4 import BeautifulSoup
html = urllib('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC+html%ED%8C%8C%EC%8B%B1&oquery=%ED%8C%8C%EC%9D%B4%EC%8D%AC+%ED%8C%8C%EC%8B%B1&tqi=hCKO7wprvOsssEbeD%2F0ssssss%2Bs-099473')
soup = BeautifulSoup(html, 'lxml')
titles = soup.find_all('title')
for title in titles:
    print(title)