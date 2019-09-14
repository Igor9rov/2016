import time
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pickle
import requests
from multiprocessing.dummy import Pool as ThreadPool

def combine_all_links(vocabular_pages):
    AllPageLinks = []
    for elem in vocabular_pages:
        i = get_link_to_the_next_page(elem)
        while i != None:
            AllPageLinks.append(i)
            i = get_link_to_the_next_page(i)
            print(i)
    return AllPageLinks

def get_link_to_the_next_page(page):
    soup = BeautifulSoup(urllib.request.urlopen(page).read(), "lxml")
    for page in soup.find_all('ul', attrs={"class": "next-prev"}):
        if page == None:
            return None
        else:
            for elem in page.find_all('a', attrs={"class": "next"}):
                if elem == None:
                    return None
                else:
                    link = (elem.get('href'))
                    link = main_page + link
                    return link

main_page = "https://yandex.ru"
proxies = {'http': 'http://212.1.227.182:80'}
kok = requests.get(main_page, proxies = proxies)
print(kok)

proxy_support = urllib.request.ProxyHandler({ 'http': 'http://110.172.167.34:8080'})
print(1)
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
print(1)
html = opener.open(main_page).read()
print(html)
soup = BeautifulSoup(html,'lxml')
hubs_page = ["https://habrahabr.ru/hubs/"]
All_Hubs_Pages = combine_all_links(hubs_page)

