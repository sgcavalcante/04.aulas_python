print(f'Programa imprimi maior valor.')
n1=int(input(f'Digite o 1º número:\n'))
n2=int(input(f'Digite o 2º número:\n'))
n3=int(input(f'Digite o 3º número:\n'))

if n1 > (n2+n3):
    print(f'Número {n1} é o maior número.')
    print(f'Números digitados: {n1} {n2} {n3}')
elif n2 > (n1+n3):
    print(f'Número {n2} é o maior número.')
    print(f'Números digitados: {n1} {n2} {n3}')
else:
    print(f'Número {n3} é o maior número.')
    print(f'Números digitados: {n1} {n2} {n3}')
