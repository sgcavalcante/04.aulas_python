numeros = []
soma = 0
multiplicacao = 1
n=5
for i in range(0,5):
    print(f'=================================')
    print(f'Digite numero {i+1}.')
    print(f'---------------------------------')
    numeros.append(int(input(f'{i+1}.')))

for i in numeros:
    soma+=i
    multiplicacao*=i
print(f'------SOMA------')    
print(soma)
print(f'------MULT------')  
print(multiplicacao)    


    