from smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Apple", "iPhone 14", "+79161234567"))
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79262345678"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79363456789"))
catalog.append(Smartphone("Google", "Pixel 7", "+79464567890"))
catalog.append(Smartphone("OnePlus", "11 Pro", "+79565678901"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
