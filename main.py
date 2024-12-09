import locale
import time

from scraper import Scraper
from providers import Providers

locale.setlocale(locale.LC_TIME, "es_MX")

order_id = 360000000000000  # pon tu id del envío
provider_id = Providers.ANDREANI  # elige el proveedor del envío
SECONDS_DELAY = 5

scraper = Scraper(provider_id, order_id)

while True:
    data = scraper.get_state()

    for key, item in data.items():
        if key not in scraper.last_state_ids:
            print(f"#{item.id} {item.title}")
            print(item.formatted_date + "\n")
            scraper.last_state_ids.add(key)

    time.sleep(SECONDS_DELAY)