from datetime import datetime

class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return str(self.date)

    @classmethod
    def make_int(cls, date):
        line = datetime.strptime(date, "%d-%m-%Y")
        d = line.day
        m = line.month
        y = line.year
        cls.d = d
        cls.m = m
        cls.y = y
        return d, m, y

    @staticmethod
    def validation(d, m, y):
        if (d in range(1, 31)):
            if (m in range(1, 12)):
                if (y > 0):
                    return f'Формат корректен'
                else:
                    return f'Неправильно введен год'
            else:
                return f'Неправильно введен месяц'
        else:
            return f'Неправильно введено число'


a = "15-06-2020"
date = Date(a)

print(date)
print(date.make_int(a))
print(date.d)

x,y,z = date.make_int(a)
print(date.validation(x,y,z))
print(date.validation(11, 15, 2020))
print(date.validation(40, 12, 1998))
print(date.validation(1, 2, -1))