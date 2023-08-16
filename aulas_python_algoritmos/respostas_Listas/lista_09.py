numero = []
soma = 0  
n=10

for i in range(0,n):
    print(f'=================================')
    numero.append(int(input(f'Digite numero {i+1}.')))
    soma+=numero[i]*numero[i]

#print(f'Idade {idade}')   
print(f'====================') 
print(soma)