import requests

class Uber():
    def __init__(self) -> None:
        self.ses = requests.Session()
        self.ses.headers.update({
            "authority": "www.uber.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9,ur;q=0.8",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "origin": "https://www.uber.com",
            "pragma": "no-cache",
            "referer": "https://www.uber.com/global/en/price-estimate/",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
            "x-csrf-token": "x"
            })
    def get_suggestions(self,query):
        url = 'https://www.uber.com/api/loadFESuggestions?localeCode=en'
        payload = {"type":"pickup","q":query,"locale":"en","lat":31.495426,"long":74.38436}
        res = self.ses.post(url,json=payload)
        cands = res.json()['data']['candidates']
        for c in cands:
            print(c['addressLine1']+"\n"+c['addressLine2'])
        

Uber().get_suggestions('minar Pakistan')



# url = "https://www.uber.com/api/loadFEEstimates"

# querystring = {"localeCode":"en"}

# payload = {
#     "origin": {
#         "id": "a8180d56-e4b3-1dbb-c6fd-02460cea6bd4",
#         "provider": "uber_places",
#         "locale": "en",
#         "latitude": 40.791419,
#         "longitude": -74.014679
#     },
#     "destination": {
#         "id": "061daaf7-18b1-cf42-634e-ed73a13d09c3",
#         "provider": "uber_places",
#         "locale": "en",
#         "latitude": 40.794691,
#         "longitude": -74.0228919
#     },
#     "locale": "en"
# }

# response = requests.request("POST", url, json=payload, params=querystring)

# print(response.text)