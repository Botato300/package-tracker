import requests
from bs4 import BeautifulSoup

from ._interface import IScraper

class Oca(IScraper):
    def get_state(self, order_id):
        url = f"https://www.oca.com.ar/Seguimiento/Paquetes/{order_id}"

        response = requests.post(url, data={"CaptchaHome": "true"}, timeout=60)
        parser = BeautifulSoup(response.text, "html.parser")

        item_table = parser.find(id="time-line-envio")
        completed_items = item_table.find_all("li", class_="complete")

        for item in completed_items:
            print(item.find("h6").text)