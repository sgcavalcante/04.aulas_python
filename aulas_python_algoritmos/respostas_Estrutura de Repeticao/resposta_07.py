print(f'Programa Maior número de 5')
teste = True


aux = 0
max = 0
teste = True
cont = 1
while teste:
    
    n1 = int(input(f'Digite Número {cont}:\n'))
    
    
    if n1 > aux:
        aux = n1
    else:
        cont = cont    
    
    cont+=1
    if cont > 5:
        print(f'>>>>>Número Máximo é {aux}<<<<<')
        cont = 1
        print(f'\nPrograma Maior número de 5\n')
    