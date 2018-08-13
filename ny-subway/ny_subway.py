import urllib
from bs4 import BeautifulSoup

def gets_urls(url):
    u = urllib.urlopen(url)
    html = u.read()
    
    return html

def content_search(url, extension):
    read_url = gets_urls(url)
    soup = BeautifulSoup(read_url, 'html.parser')
    links = soup.find_all('a')
    
    for link in links:
        if extension in link.get('href'):
            save_file(link, url)

def save_file(link, url):
    print (link)#return urllib.urlretrieve('http://web.mta.info/developers/turnstile.html' + '/' + link, 'turnstile_100617.txt')

content_search('http://web.mta.info/developers/turnstile.html', '0610')