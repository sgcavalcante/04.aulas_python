
numeros=['0','1','2','3','4','5','6','7','8','9']
vogal = ['a','e','i','o','u']
consoantes=[]
caracteres_digitados=[]
for i in range(10):
    
    x = ((input(f'Digite caracter {i+1} da lista:\n')))
    if x.lower() in vogal or x in numeros:
        caracteres_digitados.append(x)
    else:
        consoantes.append(x)
print(f'O Sistema leu {len(consoantes)} consoantes.')            

#for i in range(len(numeros)):
#    print(f'A posição {i} da lista contém o número {numeros[i]}')   

numeros.sort(reverse=True)    
print(numeros)    