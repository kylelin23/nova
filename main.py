from sendToLLM import fetch_news_articles, parse_article
from sendToRL import fetch_stock_market_vars


def main():
    print("What is sent to LLM Model: ")
    article = fetch_news_articles()[0]
    print(parse_article(article))
    print("\nWhat is sent to RL Model: \nFinancials:")
    print(fetch_stock_market_vars())


if __name__ == "__main__":
    main()
