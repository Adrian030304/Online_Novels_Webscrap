from bs4 import BeautifulSoup
import requests

def book(title,author):
    obj = {
        "title":"",
        "author":"",
    }
    obj.update(title=title,author=author)
    return obj


def scrape():
    page_link = "https://novelbin.com/sort/latest"
    pageToScrape = requests.get(page_link)
    soup = BeautifulSoup(pageToScrape.text,"html.parser")
    titles = soup.findAll('h3',attrs={'class':'novel-title'})
    novel_titles = [title.find('a').text for title in titles]
    
    authors = soup.find_all('span',class_="author")
    novel_authors = [author.text for author in authors]
    
    novels = []
    for novel_title, novel_author in zip(novel_titles, novel_authors):
        novels.append(book(novel_title,novel_author))
    print(novels)
    
    # novel_titles = []
    # for title in titles:
    #     titles_elements = title.findChildren('a',title=True)
    #     for title_element in titles_elements:
    #         title_text = title_element.text
    #         novel_titles.append(title_text)
    # print(novel_titles)

print(scrape())