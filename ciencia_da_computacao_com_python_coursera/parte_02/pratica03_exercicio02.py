class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, triangulo):
        r_1 = self.a / triangulo.a
        r_2 = self.b / triangulo.b
        r_3 = self.c / triangulo.c
        if r_1 == r_2 == r_3:
            return True
        else:
            return False
