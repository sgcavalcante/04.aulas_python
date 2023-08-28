class Quadrado:
    def __init__(self,lado:float):
        self.lado = lado
    def area(self,x_lado:float):
        x = x_lado
        area_quadrado = x * x
        print(area_quadrado)  

    def mudarLado(self,novo_lado:float):
        self.lado = novo_lado
            
    def valorLado(self):
        print(self.lado)  
        return self.lado 
        


quadrado1 = Quadrado(2.2)
quadrado2 = Quadrado(2.0)

 

quadrado2.area(quadrado2.valorLado())
quadrado2.mudarLado(3)
quadrado2.area(quadrado2.valorLado())