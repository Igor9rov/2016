#https://habrahabr.ru/post/173509/
#http://toly.github.io/blog/2014/02/13/parallelism-in-one-line/
import time
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pickle
import requests
import multiprocessing
from multiprocessing import Pool as ThreadPool


def writetothepickle(test, data):
    output = open(test, 'wb')
    pickle.dump(data, output, 2)
    output.close()


def readfrompickle(test):
    input = open(test, 'rb')
    data = pickle.load(input)
    input.close()
    return data


def get_hublinks_from_vocabular_page(hubs_link):
    Hub_links = []
    for elem in hubs_link:
        soup = BeautifulSoup(urllib.request.urlopen(elem).read(),"lxml")
        for hubs in soup.find_all('div', attrs={"class": "hub"}):
            for hub in hubs.find_all('div', attrs={"class": "title"}):
                for link in hub.find_all('a'):
                    Hub_links.append(link.get('href'))
    return Hub_links


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


def combine_all_links(page):
    AllPageLinks = [page]
    try:
        i = get_link_to_the_next_page(page)
        while i != None:
            AllPageLinks.append(i)
            print(i)
            i = get_link_to_the_next_page(i)
    except Exception as e: print(e)
    time.sleep(0.4)
    return AllPageLinks


def get_link_to_article(hublink):
    print(multiprocessing.current_process())
    soup = BeautifulSoup(urllib.request.urlopen(hublink,timeout = 20).read(),  "lxml")
    print(multiprocessing.current_process(),'Create soup')
    for posts in soup.find_all('div', attrs={"class": "posts_list"}):
        for post in posts.find_all('h2', attrs={"class": "post__title"}):
            for link in post.find_all('a'):
                x = link.get('href')
                print(x)
                if x != '/sandbox/' and x!= '/info/help/karma/#recovery':
                    return x


def get_text_from_page(link):
    try:
        soup = BeautifulSoup(urllib.request.urlopen(link).read(), "lxml")
        for text in soup.find_all('div', attrs={"class": "content html_format"}):
            Texts = text.get_text()
            print('хыыыыыыыы')
    except Exception as e:
        print(e)
        Texts = None
    return Texts


if __name__ == '__main__':
    Time1 = time.clock()
    pool = ThreadPool(10)
    proxies = {'http': 'http://212.1.227.182:80'}
    proxy_support = urllib.request.ProxyHandler(proxies)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    main_page = "https://habrahabr.ru"
    hubs_page = "https://habrahabr.ru/hubs/"

    '''
    All_Hubs_Pages = combine_all_links(hubs_page)
    HubLinks = get_hublinks_from_vocabular_page(All_Hubs_Pages)
    Time2 = time.clock()
    print(Time2 - Time1)
    BigHubLinks = pool.imap(combine_all_links,HubLinks)
    #writetothepickle('BigHubLinks.pkl',BigHubLinks)
    #BigHubLinks = readfrompickle('BigHubLinks.pkl')
    HubsLinks = []
    for elem in BigHubLinks:
        for link in elem:
            HubsLinks.append(link)
    #writetothepickle('AllHubsLinks.pkl',HubsLinks)
    Time2 = time.clock()
    print(Time2 - Time1)
    '''
    HubsLinks = readfrompickle('AllHubsLinks.pkl')
    ArticleLinks = pool.imap(get_link_to_article, HubsLinks)
    ALinks = list(set(ArticleLinks))
    # writetothepickle('ArticleLinks.pkl', ALinks)
    Time2 = time.clock()
    print(Time2 - Time1)
    # ALinks = readfrompickle('ArticleLinks.pkl')
    AllTexts = pool.imap(get_text_from_page, ALinks)
    writetothepickle('AllText.pkl', AllTexts)
    Time2 = time.clock()
    print(Time2 - Time1)








