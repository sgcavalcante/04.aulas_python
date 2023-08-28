class Bola:
    def __init__(self,cor:str,circunferencia:float, material:str):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def __str__(self):
        return f'{self.cor},{self.circunferencia},{self.material}'


    def trocarCor(self,novacor:str):
        self.cor = novacor
    
    def mostrarCor(self):
        print(self.cor)


bola1 = Bola("rosa",0.95,"couro")
bola2 = Bola("preta",1.95,"meia")
bola3 = Bola("ouro",0.095,"ouro")
bola4 = Bola("azul",2.95,"plastico")
'''
print(bola1.cor)
print(bola1.circunferencia)
print(bola1.material)
'''
#print(bola1)
bola1.mostrarCor()
bola1.trocarCor('verde')
bola1.mostrarCor()
#print(bola1)
