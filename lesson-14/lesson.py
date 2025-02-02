from bs4 import BeautifulSoup
import requests

html_doc = requests.get("https://example.com")
# print(html_doc.content.decode('utf-8'))
soup = BeautifulSoup(html_doc.content, 'html.parser')
# print(soup.prettify)
print(soup.h1)
print(soup.find('p'))
print(soup.find_all('a'))
# print(soup.p['class'])
print(soup.find(id = 'link1'))

soup.p['class'] = 'bold'
soup.p['id'] = 'hello'
del soup.p['class']
print(soup.p.attrs)

res = requests.get("https://data.worldbank.org/country")
soup_res = BeautifulSoup(res.content, 'html.parser')

# print(soup_res)
sections = soup_res.find_all('section')
# print(sections, 12)
countries = {}
for section in sections:
    title = section.find('h3')
    # print(title.text)
    names = section.find_all('a')
    countries[title.text] = []
    for name in names:
        # print('\t', name.text)
        countries[title.text].append(name.text)

print(countries['U'])