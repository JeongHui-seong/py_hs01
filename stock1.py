
import requests

def findStock():
    url = "https://finance.naver.com/sise/sise_market_sum.naver"
    req = requests.get(url)
    
    inp = input("주식 가격 알려드림 ")
    find_text_index = req.text.find(f'class="tltle">{inp}')
    
    if find_text_index == -1:
        print('그런 주식 없음 돌아가')
    else:
        find_price = req.text[find_text_index + 31:find_text_index + 71]
        replace_price = int(find_price.replace('<td class="number">',"").replace('</td>',"").replace("\n","").replace("	","").replace(",","").replace("<","").replace(">","").replace("t","").replace("d",""))
        print(f"{inp}의 가격 : {replace_price:,}원") 

if __name__ == "__main__":
    findStock()
    