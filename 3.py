class NotNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []
while True:
    try:
        x = input('Введите натуральное число или stop для завершения программы: ')
        if x == 'stop':
            break
        if not x.isnumeric():
            raise NotNumberError("Это не число!")
    except NotNumberError as err:
        print(err)
    else:
        my_list.append(x)
print(*my_list)