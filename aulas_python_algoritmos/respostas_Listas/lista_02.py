numeros=[]
for i in range(10):
    numeros.append(int(input(f'Digite número da posição {i} da lista:\n')))


#for i in range(len(numeros)):
#    print(f'A posição {i} da lista contém o número {numeros[i]}')   

numeros.sort(reverse=True)    
print(numeros)    