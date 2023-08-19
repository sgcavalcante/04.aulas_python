def qtdedigitos(n):
    teste = True
     
    mult = 10
    cont = 0
    while teste:
        n = n/10
        #print(n)
        cont += 1
        if (n < 1):
            print(cont)
            teste = False
        
           
while True:                         
    n = int(input(f'Digite um numero inteiro:\n'))
    qtdedigitos(n)            