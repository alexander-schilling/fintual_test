import requests
from tools.utils import date_to_string

FINTUAL_ASSETS_URL = "https://fintual.cl/api/real_assets/"

class Stock:
    def __init__(self, name, asset_id):
        self.name = name
        self.id = asset_id

    def get_price_from_date(self, date):
        date_string = date_to_string(date)
        result = requests.get(f"{FINTUAL_ASSETS_URL}{self.id}/days?date={date_string}")

        if result.status_code == 200:
            try:
                response_data = result.json()
                return response_data["data"][0]["attributes"]["price"]
            except:
                raise Exception(f"No data for {self.name} on {date_string}")
        else:
            raise Exception(f"Error getting price for {self.name} on {date_string}")
