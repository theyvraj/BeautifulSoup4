import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')

# TAG CREATION

tag = soup.b
#print(tag.name)
#print(tag.attrs)
tag.name = 'g'
print(tag.name)
tag['class'] = "container"
print(tag.get_attribute_list('class'))
