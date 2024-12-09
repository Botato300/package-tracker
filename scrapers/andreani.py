import requests
from datetime import datetime

from .IScraper import IScraper

class Andreani(IScraper):
    __API_URL = "https://tracking-api.andreani.com/api/v1/Tracking"

    def __format_data(self, states):
        data = {}

        states = sorted(states, key=lambda x: x["orden"])

        for item in states:
            item_id = item["orden"]

            date_obj = datetime.fromisoformat(item["fechaUltimoEvento"])

            formatted_date = date_obj.strftime("%A, %d de %B a las %H:%Mhs").capitalize()
            formatted_date = formatted_date.replace(date_obj.strftime("%B"), date_obj.strftime("%B").capitalize())

            data[item_id] = {
                "id": item_id,
                "title": item["titulo"],
                "date": formatted_date,
            }

        return data

    def get_state(self, order_id):
        payload = {
            "idReceptor": 1,
            "idSistema": 1,
            "userData": '{"mail":""}',
            "numeroAndreani": str(order_id),
        }

        headers = {
            "Authorization": "XqPMiwXzTRKHH0mF3gmtPtQt3LNGIuqCTdgaUHINMdmlaFid0x9MzlYTKXPxluYQ",
        }

        response = requests.get(self.__API_URL, params=payload, headers=headers, timeout=60)

        data = self.__format_data(response.json()["timelines"])

        return data
