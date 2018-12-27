from bs4 import BeautifulSoup
import urllib.request


response = urllib.request.urlopen('http://python.org/')
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))