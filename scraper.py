from providers import Providers

from scrapers.IScraper import IScraper
from scrapers.oca import Oca
from scrapers.andreani import Andreani


class Scraper:
    __provider: IScraper = None
    __order_id: int | str = None

    def __init__(self, provider_id: int, order_id: int | str):
        match(provider_id):
            case Providers.ANDREANI:
                self.__provider = Andreani()
            case Providers.OCA:
                self.__provider = Oca()
            case _:
                raise ValueError("El ID del proveedor no existe.")

        self.__order_id = order_id

    def get_state(self) -> dict:
        return self.__provider.get_state(self.__order_id)
