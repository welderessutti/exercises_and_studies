class Recibo:
    def __init__(self, v):
        self.recibo = v


recibo1 = Recibo(50)
recibo2 = Recibo(100)
recibo3 = Recibo(200)
recibo4 = recibo3
recibo3 = None
recibo1 = recibo3
recibo4 = recibo1
recibo3 = recibo2


print(recibo1.recibo)
print(recibo2.recibo)
print(recibo3.recibo)
print(recibo4.recibo)
