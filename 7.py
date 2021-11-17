class ComplexNumber():
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return str(f'{self.real} + {self.imaginary}i')

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real - self.imaginary * other.imaginary), (self.imaginary * other.real + self.real * other.imaginary))

z_1 = ComplexNumber(3, 5)
z_2 = ComplexNumber(-6, 8)
print(f'Комплексные числа {z_1} и {z_2}')
print(f'Их сумма равна {z_1 + z_2}')
print(f'Их произведение равно {z_1 * z_2}')