from bs4 import BeautifulSoup
import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
# LIST
# print(soup.find_all(['a','b']))

# REGULAR EXPRESSION
# for i in soup.find_all(re.compile("^b")):
#     print(i.name)

# BOOL
# for i in soup.find_all(True):
#     print(i.name)

# FUNCTION
# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')

# print(soup.find_all(has_class_but_no_id))

# print(soup.find_all(id="link2"))
# for i in soup.find_all('p'):
#     if i.get('class') == ['title']:
#         print(i.contents)
print(soup.find_all('a'))
for i in soup.find_all('a'):
    print(i.get('href'))