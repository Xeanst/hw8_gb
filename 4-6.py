class EquipmentWarehouse():
    def __init__(self, title):
        self.title = title
        self.received_equipment = {}
        self.given_equipment = {}

    def receive_equipment(self, equipment):
        self.received_equipment.update({equipment.title: equipment.count})
        return f'На {self.title} получено оборудование: {equipment.title}, количество: {equipment.count}'

    def give_equipment(self, equipment):
        self.given_equipment.update({equipment.title: equipment.count})
        return f'Со {self.title} выдано оборудование: {equipment.title}, количество: {equipment.count}'

class Equipment():
    def __init__(self, title, count):
        self.title = title
        self.count = count


    def __str__(self):
        return str(self.title)

class Printer(Equipment):
    def __init__(self, title, count, printing_type):
        Equipment.__init__(self, title, count)
        self.printing_type = printing_type

    def __str__(self):
        return f'Название модели: {Equipment.__str__(self)}, количество: {self.count}, тип печати: {str(self.printing_type)}'

class Scanner(Equipment):
    def __init__(self, title, count, scanning_type):
        Equipment.__init__(self, title, count)
        self.scanning_type = scanning_type

    def __str__(self):
        return f'Название модели: {Equipment.__str__(self)}, количество: {self.count}, тип сканирования: {str(self.scanning_type)}'

class Xerox(Equipment):
    def __init__(self, title, count, copying_type):
        Equipment.__init__(self, title, count)
        self.copying_type = copying_type

    def __str__(self):
        return f'Название модели: {Equipment.__str__(self)}, количество: {self.count}, тип копирования: {str(self.copying_type)}'

store = EquipmentWarehouse('cклад техники')

printer = Printer('принтер', 5, 'черно-белый')
print(printer)
scanner = Scanner('сканер', 4, 'цветной')
print(scanner)
xerox = Xerox('ксерокс', 7, 'цветной')
print(xerox)

print(store.receive_equipment(printer))
print(store.receive_equipment(scanner))
print(store.give_equipment(xerox))

print(f'Полученное оборудование: {store.received_equipment}')
print(f'Выданное обобрудодвание: {store.given_equipment}')