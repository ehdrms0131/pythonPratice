import requests
import pprint

client_id = ''
client_secret = ''

naver_open_api = 'https://openapi.naver.com/vl/search/shop.json?query=android&display=100&start=201'

header_params = {"X-Naver-Client-ID":client_id, "X-Naver-Client-Secret":client_secret}
res = requests.get(naver_open_api,headers=header_params)

res.json()

if res.status_code == 200:
  data = res.json()
  pprint.pprint (data['item'])
else:
  print("error Code :",res.status_code)



import requests

client_id = ''
client_secret = ''

start = 1
for index in range(10):
  start_number = start + (index * 100) 
  naver_open_api = 'https://openapi.naver.com/vl/search/shop.json?query=android&display=100&start=201' + str(start_number)
  print(naver_open_api)


import requests

client_id = ''
client_secret = ''

start = 1
for index in range(10):
  start_number = start + (index * 100) 
  naver_open_api = 'https://openapi.naver.com/vl/search/shop.json?query=android&display=100&start=201' + str(start_number)
  header_params = {"X-Naver-Client-ID":client_id, "X-Naver-Client-Secret":client_secret}
  res = requests.get(naver_open_api,headers=header_params)
  if res.status_code == 200:
    data = res.json
    for num, item in enumerate(data['items']):
      print(num+1,item['title'],item['link'])
  else:
    print("error code:",res.status_code)

import requests

client_id = ''
client_secret = ''

start = 1
for index in range(100):
  start_number = start + (index * 100) 
  naver_open_api = 'https://openapi.naver.com/vl/search/shop.json?query=android&display=1000&start=101' + str(start_number)
  header_params = {"X-Naver-Client-ID":client_id, "X-Naver-Client-Secret":client_secret}
  res = requests.get(naver_open_api,headers=header_params)
  if res.status_code == 200:
    data = res.json
    for num, item in enumerate(data['items']):
      print(num+1,item['title'],item['link'])
  else:
    print("error code:",res.status_code)


import requests

client_id = ''
client_secret = ''

start = 100

for index in range(9):
    start_number = start + (index * 100)
    naver_open_api = 'https://openapi.naver.com/v1/search/shop.json?query=컴퓨터&display=100&start=' + str(start_number)
    header_params = {"X-Naver-Client-ID": client_id,"X-Naver-Client-Secret": client_secret}
    res = requests.get(naver_open_api, headers=header_params)

    if res.status_code == 200:
        data = res.json()
        for num, item in enumerate(data['items']):
            print(num + start_number, item['title'], item['link'])
    else:
        print("Error Code:", res.status_code)


import requests
import pprint

client_id = ''
client_secret = ''

naver_open_api = 'https://openapi.naver.com/vl/search/shop.json?query=android&display=100&start=201'

header_params = {"X-Naver-Client-ID":client_id, "X-Naver-Client-Secret":client_secret}
res = requests.get(naver_open_api,headers=header_params)

res.json()

if res.status_code == 200:
  data = res.json()
  for index,item in enumerate(data['item']):
    print(index+1,item['title'],item['link'])
else:
  print("error Code :",res.status_code)