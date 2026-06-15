class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def display(self):
        sign = "+" if self.imag >= 0 else "-"
        print(f"{self.real} {sign} {abs(self.imag)}i")

a = Complex(1, 2)
b = Complex(3, 4)
c = a.add(b)
c.display()  # 4 + 6i
