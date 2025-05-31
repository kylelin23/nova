import yfinance as yf

def fetch_stock_market_vars():
    '''
    Collect stock market data
    '''
    ticker_symbol = "UBER"
    ticker = yf.Ticker(ticker_symbol)
    historical_data = ticker.history(period="5y")
    financials = ticker.financials
    return(financials)