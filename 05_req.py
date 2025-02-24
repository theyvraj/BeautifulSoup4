import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.york.ac.uk/teaching/cws/wws/webpage1.html').text
soup = BeautifulSoup(r, 'html.parser').prettify()
# p_tags = soup.find_all('p')
# for i in p_tags:
#     print(i.prettify())
a_tags = soup.find_all('a')
for i in a_tags:
    print(i.get('href'))