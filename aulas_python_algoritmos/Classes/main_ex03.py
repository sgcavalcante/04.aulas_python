from Classes_ex03 import Retangulo

while True:
    comodo = input(f'Digite nome do Cômodo:\n')
    ladoa = float(input(f'Digite valo do lado A:\n'))
    ladob = float(input(f'Digite valo do lado B:\n'))

    nome = Retangulo(comodo,ladoa,ladob)
    nome.mostrarLados()
    nome.dadosTecnicos()

    print(nome)