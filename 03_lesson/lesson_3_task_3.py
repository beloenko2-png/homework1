from address import Address
from mailing import Mailing

from_addr = Address("111111", "Москва", "Тверская", "1", "1")
to_addr = Address("222222", "Нижний Новгород", "Большая Покровская", "2", "2")

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=100,
    track="RU3333333RU"
)
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")