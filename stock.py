import requests
import sys

req = requests.get("https://finance.naver.com/sise/sise_market_sum.naver")
html = req.text

args = sys.argv[1:]

def stock_price(a):
    find_stock = html.find(a)
    find_index = html[find_stock:find_stock + 100].find('<td class="number">')
    find_price = html[find_stock:find_stock + 100][find_index:50]
    replace_price = int(find_price.replace('<td class="number">',"").replace('</td>',"").replace("\n", "").replace("	", "").replace(",",""))
    return replace_price

for i in args:
    stockPrice = stock_price(i)
    print(f"{i} : {stockPrice:,}원")
