from bs4 import BeautifulSoup
import requests

def scrape():
    page_link = "https://novelbin.com/"
    pageToScrape = requests.get(page_link)

    
print(scrape())