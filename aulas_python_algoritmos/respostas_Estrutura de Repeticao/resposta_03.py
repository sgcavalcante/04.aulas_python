print(f'{10*"="}Programa de Validação{10*"="}')
teste1 = True
nome = ""
idade = ""
salario = ""
sexo=""
estado_civil = ""
 
teste = 0
while teste1:
    nome = (input(f'\nDigite seu nome:'))
    idade = int(input(f'Digite sua idade:'))
    salario = int(input(f'Digite seu salário:'))
    sexo = (input(f'Digite seu sexo:'))
    estado_civil = (input(f'Digite seu estado civil:'))

    if len(nome)>3:
        teste+=1
    if idade > 0 and idade <150:
        teste+=1
    if salario > 0:
        teste+=1
    if sexo.lower() in ['f','m']:
        teste+=1
    if estado_civil.lower() in ['s','c','v','d']:            
        teste+=1
    if teste == 5:
        teste1 = False
    else:
        print(f'Reveja seus dados. Cadastro negado!')
     
print(f'Validação realizada com Sucesso!')
