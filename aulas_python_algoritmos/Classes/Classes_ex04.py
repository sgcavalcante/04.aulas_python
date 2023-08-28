class Pessoa:
    def __init__(self, nome:str,idade:int,peso:float,altura:float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def __str__(self):
        return f'{self.nome} {self.idade} {self.peso} {self.altura}'
    
    def crescer(self,crescimento):
         
        self.altura =  crescimento + self.altura

    def engordar(self,peso_ganho):
        self.peso += peso_ganho

    def emagrecer(self,peso_perdido):
        self.peso -= peso_perdido  


    def envelhecer(self,qtde_anos):
        nova_idade = self.idade + qtde_anos
        idade_antiga = self.idade
        self.idade = nova_idade
         
        if self.idade > 21 :
             
            crescimento =   0.05 * (21 - idade_antiga)
            print(crescimento)
            self.crescer(crescimento)
        else:
            crescimento =   0.05 * (nova_idade - idade_antiga)
            print(crescimento)
            self.crescer(crescimento)


p1 = Pessoa("eu",15,105,1.65)
p2 = Pessoa("ela",40,90,1.72)
p3 = Pessoa("Jangley", 19, 100, 100)
print(p1)
print(p2)
print(p3)
print('-------------------------')
p1.envelhecer(5)
print(p1)
print('-------------------------')
p2.crescer(0.28)
p2.engordar(5)
print(p2)
p2.emagrecer(10)
print(p2)
print('-------------------------')
p3.envelhecer(25)
print(p3)   