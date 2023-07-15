import requests
from bs4 import BeautifulSoup


#chatGPT
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.capitoltrades.com/trades"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html')
trade_names = soup.select('script')
next_data = trade_names[16]
tc = next_data.contents
data = tc[0]
res = json.loads(str(data))

r = soup.select('body')
rd = r[0]
ttc = rd.contents
datad = ttc[0]
dd = json.loads(str(datad))


print(soup)



# for trade_name in trade_names:
#     print(trade_name.text)



# r = requests.get('https://www.capitoltrades.com/trades')
#
# # check status code for response received
# # success code - 200
# print(r)
# print(r.content)

# soup = BeautifulSoup(r.content, 'html.parser')
# for jk in soup:
#     print(str(jk) + '\n' + '\n')
# s = soup.find('div', class_='__NEXT_DATA__')
#
# lines = s.find_all('a')
#
# for line in lines:
#     print(line.text)
# # # Parsing the HTML
# # soup = BeautifulSoup(r.content, 'html.parser')
# # print(soup.prettify())