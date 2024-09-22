from bs4 import BeautifulSoup
import requests

def scrape():
    page_link = "https://novelbin.com/sort/latest"
    pageToScrape = requests.get(page_link)
    soup = BeautifulSoup(pageToScrape.text,"html.parser")
    titles = soup.findAll('h3',attrs={'class':'novel-title'})
    novel_titles = [title.find('a').text for title in titles]
    print(novel_titles)
    
    authors = soup.find_all('span',class_="author")
    novel_authors = [author.text for author in authors]
    print(novel_authors)
    
    # novel_titles = []
    # for title in titles:
    #     titles_elements = title.findChildren('a',title=True)
    #     for title_element in titles_elements:
    #         title_text = title_element.text
    #         novel_titles.append(title_text)
    # print(novel_titles)

    
print(scrape())