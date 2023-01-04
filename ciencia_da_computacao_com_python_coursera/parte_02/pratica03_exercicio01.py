class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        ret = self.c ** 2
        ret_2 = (self.a ** 2) + (self.b ** 2)
        if ret == ret_2:
            return True
        else:
            return False
