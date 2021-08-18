import requests

def currency_rates(symbol):
    symbol = symbol.upper()
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    r = r.text
    if symbol not in r:
        return None

    rub = r[r.find('<Value>', r.find(symbol)) + 7:r.find('</Value>', r.find(symbol))]
    return rub

