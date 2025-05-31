import yfinance as yf

def fetch_stock_market_vars():
    '''
    Collect stock market data
    '''
    ticker_symbol = "UBER"
    ticker = yf.Ticker(ticker_symbol)
    financials = ticker.financials
    print("\nFinancials:")
    print(financials)

fetch_stock_market_vars()