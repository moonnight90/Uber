import requests
from datetime import datetime
import sqlite3


def create_vehicle_table(vehicle_type):
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {vehicle_type} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time_of_entry TEXT,
            origination_address TEXT,
            destination_address TEXT,
            min_price TEXT,
            max_price TEXT
        );
    ''')
    conn.commit()

def insert_data(vehicle_type, origination, destination, min_price, max_price):
    time_of_entry = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute(f'''
        INSERT INTO {vehicle_type} (time_of_entry, origination_address, destination_address, min_price, max_price)
        VALUES (?, ?, ?, ?, ?);
    ''', (time_of_entry, origination, destination, min_price, max_price))
    conn.commit()


def get_table_names():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = [row[0] for row in cursor.fetchall()]
    return table_names

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
    def split_price(self,string):
        allowed_chars = "0123456789.-"
        string = "".join([char for char in string if char in allowed_chars])
        min_max = string.split('-')
        if len(min_max)==1:
            min_max.append('0')
        return min_max


    def get_suggestions(self,query):
        url = 'https://www.uber.com/api/loadFESuggestions?localeCode=en'
        payload = {"type":"pickup","q":query,"locale":"en","lat":31.495426,"long":74.38436}
        res = self.ses.post(url,json=payload)
        cands = res.json()['data']['candidates']
        if len(cands):
            return {
                "id":cands[0]['id'],
                "provider":cands[0]['provider'],
            }
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
            res = res.json()
            data = res['data']
            
            return {
                "id": data['id'],
                "provider": data['provider'],
                "locale": "en",
                "latitude": data['lat'],
                "longitude": data['long']
            },data['fullAddress']
    def load_estimate(self,payload):
        res = self.ses.post("https://www.uber.com/api/loadFEEstimates?localeCode=en",
                      json=payload
                      )
        prices = res.json()['data']['prices']
        for price in prices:
            yield (price['vehicleViewDisplayName'],price['fareString'])
    def run(self,pickup,destination):
        res = self.get_suggestions(pickup)
        pickup = self.get_detail('pickup',res['id'],res['provider'])
        res = self.get_suggestions(destination)
        destination = self.get_detail('destination',res['id'],res['provider'])
        payload = {
            "destination":destination[0],
            'origin': pickup[0],
            "locale":"en"
        }
        results = list(self.load_estimate(payload))

        for result in results:
            [min,max] = self.split_price(result[1])
            vehical = result[0]
            vehical = vehical.replace(' ','_')
            print(vehical,min,max,destination[1],pickup[1])
            if vehical not in existed_tables:
                create_vehicle_table(vehical)
                existed_tables.append(vehical)
            insert_data(vehical,pickup[1],destination[1],min,max)
            
            
if __name__ == "__main__":
    
    conn = sqlite3.connect('vehicles_data.sqlite3')
    cursor = conn.cursor()
    existed_tables = get_table_names()
    Uber().run('Botany Road & Southern Cross','Belrose, NSW')


        


