import requests

from bs4 import BeautifulSoup
res = requests.get('https://news.v.daum.net/v/20210525163533884')
soup = BeautifulSoup(res.content, 'html.parser')
mydata = soup.find('title')
print(mydata.get_text())

from bs4 import BeautifulSoup
res = requests.get('https://news.v.daum.net/v/20210525163533884')
soup = BeautifulSoup(res.content, 'html.parser')#lxml
mydata=soup.find('span',class_="txt_info")
print(mydata.get_text())

from bs4 import BeautifulSoup
html = """<html>
<body>
<hl id='title'>[1]크롤링이란></h1>
<p class=cssstyle>'웹 페이지에서 필요한 데이터를 추출하는 것'</p>
<p id='bpdu' align='center'>파이썬을 중심으로 다양한 웹 크롤링 기술 발달</p>
</body>
</html>"""
soup=BeautifulSoup(html,'html.parser')
data=soup.find('p')
print(data.get_text())  

from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test')
soup = BeautifulSoup(res.content, 'html.parser')

titles = soup.find_all('li','course')
for title in titles:
  print(title.get_text())

"""~
p 태그 문장이 두 개인데 이 중에 하나를 선택하려면?

1.data = soup.find('p',class_='cssstyle')
2.data = soup.find('p','cssstyle')
3.data = soup.find('p',arrts={'align':'center'})
4.data = soup.find(id='body) 
"""

