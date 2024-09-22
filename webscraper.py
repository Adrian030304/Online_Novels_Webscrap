from bs4 import BeautifulSoup
import requests
import json
from random import randint 
from time import sleep  

def scrape():
    novels = []
    page_link = "https://novelbin.com/sort/latest"
    for i in range(1,5):
        pageToScrape = requests.get(page_link + "?page=" + str(i))
        soup = BeautifulSoup(pageToScrape.text,"html.parser")
        
        titles = soup.findAll('h3',attrs={'class':'novel-title'})
        novel_titles = [title.find('a').text for title in titles]
        
        authors = soup.find_all('span',class_="author")
        novel_authors = [author.text for author in authors]
    
        for novel_title, novel_author in zip(novel_titles, novel_authors):
            book = {
            "title":novel_title,
            "author":novel_author,
        }
            novels.append(book)
    return novels

with open('data.json','w') as f:
    json.dump(scrape(),f,sort_keys=True)
print(scrape())