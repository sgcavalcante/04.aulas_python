numeros = []
numeros1 = []
maior = 0
for n in range(5):
    numero = int(input(f'Digite o número{n+1}:\n'))
    numeros.append(numero)

numeros.sort()
numeros1 = numeros.copy()
print(numeros1)    

numeros.sort(reverse = True)
print(numeros)    
