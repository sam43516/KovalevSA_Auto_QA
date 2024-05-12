from smartphone import Smartphone
catalog = []

catalog.append(Smartphone("iPhone", "13 Pro", "+79088971233"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79088922453"))
catalog.append(Smartphone("iPhone", "15 Pro Max", "+79088977887"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 4", "+79998971533"))
catalog.append(Smartphone("Huawei", "Nova 12i", "+79258666233"))

for smartphone in catalog:
    smartphone.infoDevice()
    
