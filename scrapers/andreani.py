import requests

from .IScraper import IScraper

class Andreani(IScraper):
    __API_URL = "https://tracking-api.andreani.com/api/v1/Tracking"

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

        return response.json()