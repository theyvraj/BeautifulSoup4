import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')

# TAG CREATION

# tag = soup.b
# print(tag.name)
# print(tag.attrs)
# tag.name = 'g'
# print(tag.name)
# tag['class'] = 'container'
# print(tag.get_attribute_list('class'))
# new_tag = soup.find_all('g')
# for i in new_tag:
#     print(i.get_attribute_list('class'))

# DELETING ATTRIBUTE

# del tag['id']
# print(tag.get('id'))

# MULTIPLE-VALUED ATTRIBUTE
# You can disable this by passing multi_valued_attributes=None 
# as a keyword argument into the BeautifulSoup constructor

# tag['class'] = ['container', 'test_add']
# tag['id'] = 'test_id'
# print(tag)
# for i in new_tag:
#     print(i.get_attribute_list('class'))
#     print(i.get('id'))

# NAVIGABLE STRING  

# tag = soup.b
# print(tag.string)

#  TEXT REPLACEMENT

# new_string = 'No bold text'
# tag.string.replace_with(new_string)
# print(tag.string)

#  TAG CONVERSION

# new_tag = soup.b.string.wrap(soup.new_tag('i'))
# print(new_tag)

#  TAG TYPE CONVERSION
# new_tag = str(new_tag)
# print(type(new_tag))

# 