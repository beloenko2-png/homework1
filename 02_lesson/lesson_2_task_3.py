import math

def square():
    side = float(input("Введите длину стороны квадрата: "))
    rounded_side = math.ceil(side)
    area = rounded_side ** 2
    return area
result = square()
print(f"Площадь квадрата: {result}")