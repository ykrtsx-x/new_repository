from address import Address
from mailing import Mailing

from_address = Address("123456", "CityA", "StreetA", "1", "1")
to_address = Address("654321", "CityB", "StreetB", "2", "2")
mailing = Mailing(to_address, from_address, 10.0, "TRACK123")

print(f"Отправление {mailing.track} из {mailing.from_address.zip_code}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.zip_code}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} -"
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
