from scrapers.scraper import Scraper

PROVIDERS = {
    "oca": "oca",
    "andreani": "andreani"
}

order_id = 1 #pon tu id del envío
provider_name = PROVIDERS["oca"] #elige el proveedor del envío

scraper = Scraper(provider_name, order_id)