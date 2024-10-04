from .oca import Oca

class Scraper():
    def __init__(self, provider_name: str, order_id: int|str):
        if provider_name == "oca":
            oca = Oca()
            oca.get_state(order_id)