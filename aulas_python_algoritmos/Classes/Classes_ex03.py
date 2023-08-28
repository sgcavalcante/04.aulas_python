class Retangulo:
    def __init__(self,comodo:str,ladoa:float,ladob:float):
        self.ladoa = ladoa
        self.ladob = ladob
        self.comodo = comodo
    def mudarValores(self, novo_ladoa:float,novo_ladob:float):
        self.ladoa = novo_ladoa
        self.ladob = novo_ladob   
    def mostrarLados(self):
        print(f'Lado A:{self.ladoa}, Lado B:{self.ladob}')

    def dadosTecnicos(self):
        self.area = self.ladoa * self.ladob
        self.perimetro = 2 * (self.ladoa + self.ladob)  
        print(f'Área:{self.area} , Perimetro:{self.perimetro}')  

    def __str__(self) -> str:
        return f'O comodo {self.comodo}, de comprimeto:{self.ladoa} e largura: {self.ladob} precisará de {self.area} metros quadrados de piso e {self.perimetro} de roda pé.'


'''
r1 = Retangulo(2.0,3.0)

r1.mostrarLados()
r1.dadosTecnicos()
r1.mudarValores(5.0,7)
r1.mostrarLados()
r1.dadosTecnicos()

'''