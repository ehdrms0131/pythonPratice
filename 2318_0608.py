import requests
from bs4 import BeautifulSoup
res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content,'html.parser')
items = soup.select('li')
for item in items:
  print(item.get_text())

import requests
from bs4 import BeautifulSoup
res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content,'html.parser')
items = soup.select('ul > li')
for item in items:
  print(item.get_text())

import requests
from bs4 import BeautifulSoup
res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content,'html.parser')
items = soup.select('.course')
for item in items:
  print(item.get_text())

import requests
from bs4 import BeautifulSoup
res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content,'html.parser')
items = soup.select('#start')
for item in items:
  print(item.get_text())

import requests
from bs4 import BeautifulSoup
res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content,'html.parser')
items = soup.select('li.course.paid')
for item in items:
  print(item.get_text())

import requests
from bs4 import BeautifulSoup
res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content,'html.parser')
items = soup.select('tr')
for item in items:
  columns = item.select('td')
  row_str = ''
  for column in columns:
    row_str += ',' in
  print(item.get_text())

import requests
from bs4 import BeautifulSoup
res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content,'html.parser')
titles = soup.find_all('li','course')
for title in titles:
  print(title.get_text())

import requests
from bs4 import BeautifulSoup
res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content,'html.parser')
section = soup.find('ul',id='hobby_course_list')
titles = section.find_all('li','course')
for title in titles:
  print(title.get_text())

import requests
from bs4 import BeautifulSoup
res = requests.get('https://search.shopping.naver.com/best100v2/main.nhn')
soup=BeautifulSoup(res.content,'html.parser')
items = soup.select('#popular_srch_lst > li >span.txt')
for item in items:
  print(item.get_text())

import requests
from bs4 import BeautifulSoup
res=requests.get('https://finance.naver.com/sise/')
soup = BeautifulSoup(res.content,'html.parser')
#a태그이면서 href속성값이 특정한 값을 갖는 경우 탐색
data = soup.select("#popularItemList > li > a")
for item in data:
  print(item.get_text())

import requests
from bs4 import BeautifulSoup
res=requests.get('https://finance.naver.com/sise/')
soup = BeautifulSoup(res.content,'html.parser')
#a태그이면서 href속성값이 특정한 값을 갖는 경우 탐색
data = soup.select("div.rgt > ul.lst_major > li")
for item in data:
  print(item.get_text())
  print("지수이름 : ",item.find('a').get_text(),"현재지수 : ",item.find('span').get_text(),item.find('em').get_text())

!pip install openpyxl #크롤링을 엑셀파일로 변환

import openpyxl

excel_file = openpyxl.Workbook()

excel_sheet = excel_file.active
#excel_sheet.title = '리포트'
excel_sheet.append(['data1','data2','data3'])
excel_file.save('tmp.xlsx')
excel_file.close()

import openpyxl

def write_excel_template(filename,sheetname,listdata):
  excel_file = openpyxl.Workbook()
  excel_sheet = excel_file.active
  excel_sheet.column_dimensions['A'].width = 100
  excel_sheet.column_dimensions['B'].width = 20

  if sheetname != ' ':
    excel_sheet.title = sheetname
  for item in listdata:
    excel_sheet.append(item)
  excel_file.save(filename)
  excel_file.close()

  import requests
from bs4 import BeautifulSoup

product_lists = list()

for page_num in range(10):
  if page_num == 0:
    res = requests.get('https://davelee-fun.github.io/')
  else:
    res = requests.get('https://davelee-fun.github.io/page'+str(page_num+1))
  soup = BeautifulSoup(res.content, 'html.parser')

  data = soup.select('div.card')
  for item in data:
    product_name = item.select_one('div.card-body h4.card-text')
    product_date = item.select_one('div.wrapfooter span.post-date')
    product_info = [product_name.get_text().strip(),product_date.get_text()]
    product_lists.append(product_info)
  write_excel_template('tmp.xlsx','상품정보',product_lists)