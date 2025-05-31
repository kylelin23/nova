import requests
from bs4 import BeautifulSoup

def fetch_news_articles():
    '''
    Use David's sources for testing purposes
    '''
    articles = [
        'https://finance.yahoo.com/news/live/stock-market-today-sp-500-marks-best-may-in-30-years-as-wall-street-bets-on-tariff-relief-200502633.html'
    ]
    return(articles)

def parse_article(article):
    '''
    Get the text and author of the article
    '''
    # Set Up:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }
    page = requests.get(article, headers = headers)
    soup = BeautifulSoup(page.content, "html.parser")

    # Author:
    if soup.find('div', class_='byline-attr-author yf-1k5w6kz') != None:
        author = soup.find('div', class_='byline-attr-author yf-1k5w6kz').get_text()
    else:
        author = "Unable to find author"

    # Content:
    paragraphs = soup.find_all('p', class_='yf-1090901')
    content = ""
    for paragraph in paragraphs:
        if 'atoms-wrapper' in paragraph.parent.get('class', []):
            content += paragraph.get_text() + " "

    return ('Author: ' + author + '\nContent: ' + content)