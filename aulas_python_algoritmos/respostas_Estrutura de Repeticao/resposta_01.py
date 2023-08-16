print(f'Programa de Repetição')
teste = True
n1 = 1
while teste:
    n1 = int(input(f'Digite Nota 1(entre 0 e 10):\n'))
    if n1>=0 and n1<=10:
        teste = False
        
    else:
        print(f'\n\n\nErro - Digite Valor Válido')    
print(f'Valor Válido.')
