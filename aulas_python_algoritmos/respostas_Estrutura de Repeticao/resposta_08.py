print(f'Programa Média e Soma de 5 números')
teste = True

soma = 0
media = 0
aux = 0
max = 0
teste = True
cont = 0
while teste:
    cont+=1
    n1 = int(input(f'Digite Número {cont}:\n'))
    
    soma += n1
    if n1 > aux:
        aux = n1
    else:
        cont = cont    
    
    
    if cont >= 5:
        print(f'>>>>>Soma é {soma}<<<<<')
        print(f'>>>>>Média é {soma/(cont)}<<<<<')
        cont = 0
        soma = 0
        media = 0
        #print(f'\nPrograma Maior número de 5\n')
    