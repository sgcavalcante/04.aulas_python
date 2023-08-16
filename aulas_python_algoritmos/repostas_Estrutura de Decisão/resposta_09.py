print(f'Programa ordem decrescente.')
n1=int(input(f'Digite o 1º número:\n'))
n2=int(input(f'Digite o 2º número:\n'))
n3=int(input(f'Digite o 3º número:\n'))

print(f"====Menor Número====\n")
print(f'Números digitados: {n1} {n2} {n3}:\n\n')
print(f'Números em dordem Decrescente')
if (n1 < n2) and (n1 < n3):
    if (n2<n3):
        print(f'{n3} {n2} {n1}')
    else:    
        print(f'{n2} {n3} {n1}')
elif (n2 < n3) and (n2 < n1):
    if (n1<n3):
        print(f'{n3} {n1} {n2}')
    else:    
        print(f'{n1} {n3} {n2}')

elif (n3 < n1) and (n3 < n2):
    if (n1<n2):
        print(f'{n2} {n1} {n3}')
    else:    
        print(f'{n1} {n2} {n3}')
