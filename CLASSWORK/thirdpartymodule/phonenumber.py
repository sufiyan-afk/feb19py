import phonenumbers
from phonenumbers import geocoder , carrier , timezone

number = phonenumbers.parse("+918669745503")

#country / region
print(geocoder.description_for_number(number,"en"))

#carrier (network) - jio/airtel/Vi
print(carrier.name_for_number(number,"en"))

#timezone
print(timezone.time_zones_for_number(number))

