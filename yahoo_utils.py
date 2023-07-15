import yfinance as yf
from yahoofinancials import YahooFinancials



def get_stock_data(stock_abv):
    stock = yf.Ticker(stock_abv)

    # get all stock info
    info = stock.info
    twoHundredDaysAVG = info['twoHundredDayAverage']
    fiftyDaysAVG = info['fiftyDayAverage']
    previous_close = info['previousClose']
    ask = info['ask']

    if fiftyDaysAVG > twoHundredDaysAVG and ask > fiftyDaysAVG:
        purchase = True
    else:
        purchase = False

    return {
        'stock': stock_abv,
        'ask': ask,
        'previous_close': previous_close,
        '50 day avg': fiftyDaysAVG,
        '200 day avg': twoHundredDaysAVG,
        'purchase': purchase
    }
print(get_stock_data('MSFT'))