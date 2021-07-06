import requests
import json

class OKExAPI:
    def __init__(self):
        self.base_url = 'https://www.okex.com'

    def get_tickers(self):
        response = requests.get(
            f"{self.base_url}/api/spot/v3/instruments/ticker/"
        )

        json_data = json.loads(response.text)
        return json_data

