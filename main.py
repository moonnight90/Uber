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
        if len(cands):
            return cands[0]
        return False
    def get_detail(self,type,id,provider):
        url = "https://www.uber.com/api/loadFEPlaceDetails?localeCode=en"
        payload = {
            "type": type,
            "locale": "en",
            "id": id,
            "provider": provider
        }
        res = self.ses.post(url, json=payload)
        if res.status_code == 200:
            data = res['data']
            return {
                "id": data['id'],
                "provider": data['provider'],
                "locale": "en",
                "latitude": data['lat'],
                "longitude": data['long']
            }


    
        

Uber().get_suggestions('minar Pakistan')



#### ESTIMATE ####

# url = "https://www.uber.com/api/loadFEEstimates"

# querystring = {"localeCode":"en"}

# payload = {
#     "origin": {
#         "id": "ChIJayiDCf0FGTkR2T-F1Jn-TSc",
#         "provider": "google_places",
#         "locale": "en",
#         "latitude": 31.4821489,
#         "longitude": 74.3964343
#     },
#     "destination": {
#         "id": "ChIJq6qqqncGGTkRaRSUZur4bBQ",
#         "provider": "google_places",
#         "locale": "en",
#         "latitude": 31.481977,
#         "longitude": 74.3962095
#     },
#     "locale": "en"
# }


# response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

# print(response.text)



##### Place Detail ####
# url = "https://www.uber.com/api/loadFEPlaceDetails"

# querystring = {"localeCode":"en"}

# payload = {
#     "type": "pickup",
#     "locale": "en",
#     "id": "ChIJayiDCf0FGTkR2T-F1Jn-TSc",
#     "provider": "google_places"
# }


# response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

# print(response.text)