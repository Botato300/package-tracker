from dataclasses import dataclass

from providers import Providers
from scrapers.IScraper import IScraper
from scrapers.oca import Oca
from scrapers.andreani import Andreani


@dataclass
class ItemState:
    id: int
    title: str
    formatted_date: str

class Scraper:
    __provider: IScraper = None
    __order_id: int | str = None

    progress: dict[int, ItemState] = {}
    last_state_ids = set()

    def __init__(self, provider_id: int, order_id: int | str):
        match(provider_id):
            case Providers.ANDREANI:
                self.__provider = Andreani()
            case Providers.OCA:
                self.__provider = Oca()
            case _:
                raise ValueError("El ID del proveedor no existe.")

        self.__order_id = order_id

    def get_state(self) -> dict[str, ItemState]:
        states = self.__provider.get_state(self.__order_id)

        for item in states.values():
            item_id = item["id"]
            item_date = item["date"]
            item_title = item["title"]

            if item_id not in self.progress:
                self.progress[item_id] = ItemState(item_id, item_title, item_date)

        return self.progress