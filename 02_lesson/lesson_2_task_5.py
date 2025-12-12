def month_to_season(month):
    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    else: 
        return "Осень"
month = int(input("Введите номер месяца (1–12): "))
season = month_to_season(month)
print(f"Время года: {season}")