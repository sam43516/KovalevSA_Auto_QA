from address import Address
from mailing import Mailing

to_address = Address("435160", "г.Москва","ул.Тверская","д.8","кв.12")
from_address = Address ("117802", "г.Москва","ул.Пушкина","д.35","кв.55")

my_mail = Mailing(to_address, from_address, 8000, "трек-номер 07800612")
my_mail.dispatch()