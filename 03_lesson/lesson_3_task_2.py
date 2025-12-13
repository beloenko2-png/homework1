from smartphone import Smartphone
catalog = [
    Smartphone("Apple", "iPhone 12 Pro", "+79111111111"),
    Smartphone("Samsung", "Galaxy S24", "+79222222222"),
    Smartphone("Xiaomi", "13T", "+79333333333"),
    Smartphone("Huawei", "P60", "+79444444444"),
    Smartphone("Google", "Pixel 8", "+79555555555")
]
for smartphone in catalog:
    print(smartphone.brand + " - " + smartphone.model + " . " + smartphone.number)