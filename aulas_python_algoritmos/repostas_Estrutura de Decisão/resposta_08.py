print(f'Programa indica produto com menor preço.')
p1 = input(f'Digite o nome do produto 1:\n')
n1=int(input(f'Digite o preço do 1º produto:\n'))
p2 = input(f'Digite o nome do produto 2:\n')
n2=int(input(f'Digite o preço do 2º produto:\n'))
p3 = input(f'Digite o nome do produto 3:\n')
n3=int(input(f'Digite o preço do 3º produto:\n'))
 

print(f"====Menor Número====\n")

if (n1 < n2) and (n1 < n3):
    print(f'Você deve comprar produto {p1}. Seu preço é R$ {n1}.00, o mais barato.\n')
    print(f'Lista de Produtos:\n{p1}: {n1}\n{p2}: {n2}\n{p3}: {n3}\n\n')
elif (n2 < n1) and (n2 < n3):
    print(f'Você deve comprar produto {p2}. Seu preço é R$ {n2}.00, o mais barato.\n')
    print(f'Lista de Produtos:\n{p1}: {n1}\n{p2}: {n2}\n{p3}: {n3}\n\n')
elif (n3 < n1) and (n3 < n2):
    print(f'Você deve comprar produto {p3}. Seu preço é R$ {n3}.00, o mais barato.\n')
    print(f'Lista de Produtos:\n{p1}: {n1}\n{p2}: {n2}\n{p3}: {n3}\n\n')
else:
    print(f'Inválido')