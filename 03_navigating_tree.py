from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title><style>.......</style></head>
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
# print(soup.head)
# print(soup.title)
# for a in soup.find_all('a'):
#     print(a)

# CONTENTS param

head_tag = soup.head
title_tag = head_tag.contents[0]
print(title_tag.contents[0])
print(head_tag.contents[0].contents[0])

# CHILDREN param

for i in title_tag.children:
    print(i)

# DESCENDANTS param

for i in head_tag.descendants:
    print(i)
