import requests
# r = requests.get("https://financialmodelingprep.com/api/v3/quote-short/AAPL?apikey=demo")  # agar hum get request marte hai to hamari request browser ki history mei save ho jati hai
# print(r.text)
# print(r.status_code)  # it returns 200 that means all ok

url = "https://financialmodelingprep.com/api/v3/quote/AAPL?apikey=demo"
data={

}
r2 = requests.post(url=url,data=data)   # agar hum post request marte hai to hamari request browser ki history mei save nhi hoti hai
print(r2.text)
print(r2.status_code)