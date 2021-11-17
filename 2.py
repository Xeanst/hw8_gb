class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt

divisor = int(input("Введите делимое: "))
divident = int(input("Введите делитель: "))

try:
    if divident == 0:
        raise MyZeroDivisionError("Делитель не должен быть нулем!")
except MyZeroDivisionError as err:
    print(err)
else:
    print(f'Результат деления: {divisor/divident}')

