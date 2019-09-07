import requests
import os
import pprint as pp
from bs4 import BeautifulSoup

def getSourcecode(url):
    data = requests.get(url)
    return data.status_code, data.text

def extractURL(scode):
    links = []
    for link in soup.find_all('a'):
        href_link = link.get('href')
        links.append(href_link)
        # print(href_link)
    return links

def writeOutput(filename="output", data=[]):
    file = open(filename+".txt",'w')
    data_format = map(lambda x:x+'\n', data)
    file.writelines(data_format)
    file.close()

url = input("Input URL : ")
status, source_code = getSourcecode(url)
soup = BeautifulSoup(source_code, 'html.parser')
links = extractURL(soup)
links = [link for link in links if url in link]
writeOutput(input("Input Filename : "), links)