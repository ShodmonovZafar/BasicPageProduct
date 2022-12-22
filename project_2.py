html_doc = """
<html>
    <zafar>
        <title>
            The Dormouse's story
        </title>

    </zafar>
    
    <body>
        <p class="title">
            <b>
                The Dormouse's story
            </b>
        </p>

        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                Elsie
            </a>,
            <a href="http://example.com/lacie" class="sister" id="link2">
                Lacie
            </a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">
                Tillie
            </a>;
            and they lived at the bottom of a well.
        </p>

        <p class="story">
            ...
        </p>
    </body>
</html>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# prettify() -> str
# print(soup.prettify())

# print(type(soup.title))
# <title>The Dormouse's story</title>

#print(soup.title.name)
# # u'title'

# soup.title.string
# # u'The Dormouse's story'

#print(soup.title.parent.name)
# # u'head'

#print(soup.p)
# # <p class="title"><b>The Dormouse's story</b></p>

#print(soup.p['class'])
# # u'title'

# soup.a
# # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# print(soup.find_all('a'))
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# soup.find(id="link3")
# # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
