numeros=[]
par=[]
impar=[]
for i in range(20):
    x = (int(input(f'Digite caracter {i+1} da lista:\n')))
    
    numeros.append(x)
    if (x%2) == 0:
        par.append(x) 
    else:
        impar.append(x)    

print(f'Números pares: {par}')
print(f'Números pares: {impar}')
