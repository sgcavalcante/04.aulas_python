print(f'Programa Turno.')
l1=(input(f'Qual Turno você estuda? \nDigite:\nM para Matutino\nV para Vespertino ou\nN para Noturno:\n'))
#l2=(input(f'Digite o 1º número:\n'))

if l1 == "M":
    print(f'Bom Dia!')
elif l1 == "V":
    print(f'Boa Tarde')
elif l1 == "N":
    print(f'Boa Noite')
else:
    print(f'Valor Inválido')