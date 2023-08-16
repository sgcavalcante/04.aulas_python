numeros=[]
for i in range(5):
    numeros.append(input(f'Digite número da posição {i} da lista:\n'))


for i in range(len(numeros)):
    print(f'A posição {i} da lista contém o número {numeros[i]}')   
    
print(numeros)    