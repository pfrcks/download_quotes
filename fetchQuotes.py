import re
from bs4 import BeautifulSoup
import urllib2
from multiprocessing import Process

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
r = opener.open('http://www.moviequotedb.com/browse.html')
soup = BeautifulSoup(r)

TAG_RE = re.compile(r'<[^>]+>')
bufsize = 0
def func1():
    saved_quotes = open('quotes1','w', bufsize)
    all_links = soup.find_all('a', href=True)
    movie_links = []
    for link in all_links:
        if 'movies' in link['href']:
            movie_links.append(link['href'])
    movie_urls = []
    prefix = 'http://www.moviequotedb.com'
    for element in movie_links:
        movie_urls.append(prefix+element)
    movie_urls = movie_urls[:500]
    for link in movie_urls:
        print 'Opening Link' + str(link) + '\n'
        r = opener.open(link)
        soup2 = BeautifulSoup(r)
        title = soup2.find_all('title')
        str_title = TAG_RE.sub('', str(title))[1:-34]
        quotePlusTrash = soup2.find_all('div', class_='padded')
        quotesPlusLinks = []
        for element in quotePlusTrash:
            if 'quote_' in str(element):
                quotesPlusLinks.append(element)
        print quotesPlusLinks
        quotes = []
        for i, element in enumerate(quotesPlusLinks):
            if i % 2 == 0:
                continue
            print element
            quotes.append(element)
        for quote in quotes:
            saved_quotes.write(str_title+'\n\t'+TAG_RE.sub('', str(quote))+'\n')
        saved_quotes.write('\n\n')

def func2():
    saved_quotes = open('quotes2','w', bufsize)
    all_links = soup.find_all('a', href=True)
    movie_links = []
    for link in all_links:
        if 'movies' in link['href']:
            movie_links.append(link['href'])
    movie_urls = []
    prefix = 'http://www.moviequotedb.com'
    for element in movie_links:
        movie_urls.append(prefix+element)
    movie_urls = movie_urls[500:]
    for link in movie_urls:
        print 'Opening Link' + str(link) + '\n'
        r = opener.open(link)
        soup2 = BeautifulSoup(r)
        title = soup2.find_all('title')
        str_title = TAG_RE.sub('', str(title))[1:-34]
        quotePlusTrash = soup2.find_all('div', class_='padded')
        quotesPlusLinks = []
        for element in quotePlusTrash:
            if 'quote_' in str(element):
                quotesPlusLinks.append(element)
        print quotesPlusLinks
        quotes = []
        for i, element in enumerate(quotesPlusLinks):
            if i % 2 == 0:
                continue
            print element
            quotes.append(element)
        for quote in quotes:
            saved_quotes.write(str_title+'\n\t'+TAG_RE.sub('', str(quote))+'\n')
        saved_quotes.write('\n\n')

if __name__ == '__main__':
  p1 = Process(target=func1)
  p1.start()
  p2 = Process(target=func2)
  p2.start()
  p1.join()
  p2.join()
