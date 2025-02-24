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
links = soup.find('a')
head_tag = soup.head
title_tag = head_tag.contents[0]
# print(title_tag.contents[0])
# print(head_tag.contents[0].contents[0])

# GOING DOWN
#      CHILDREN param

# for i in title_tag.children:
#     print(i)

#      DESCENDANT param
# for i in head_tag.descendants:
#     print(i)

#      STRING param
# for i in soup.strings:
#     print(i)

#     # STRIPPED STRING param

# for i in soup.stripped_strings:
#     print(i)

# GOING UP
#      PARENT param
# print(title_tag.parents)

#     # PARENTS param
# for i in links.parents:
#     print(i.name)

#  GOING SIDEWAYS
#      NEXT SIBLING and PREVIOUS SIBLING param
# sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", 'html.parser')
# print(sibling_soup.prettify())
# print(sibling_soup.b.next_sibling)
# print(sibling_soup.c.previous_sibling)
# for i in soup.a.next_siblings:
#     print(i)

# GOING BACK AND FORTH
    # NEXT ELEMENT and PREVIOUS ELEMENT param
# last_a_tag = soup.find("a", id="link3")
# print(last_a_tag.next_element)

# last_p_tag = soup.find("p")
# print(last_p_tag.next_element)

# print(last_a_tag.previous_element)