print(f'Programa imprimi Média.')
n1=float(input(f'Digite a 1ª Nota:\n'))
n2=float(input(f'Digite a 2ª Nota:\n'))
soma = n1+n2
media = soma/2
#
if media>= 7.0:
    if media == 10:
        print(f'APROVADO com distinção')
    else:
        print(f'APROVADO')
else:
    print(f'REPPROVADO')
