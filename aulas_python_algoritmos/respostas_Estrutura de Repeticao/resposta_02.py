print(f'{10*"="}Programa de Senha{10*"="}')
teste = True
login = ""
senha = ""
while teste:
    login = (input(f'\nDigite Login:'))
    senha = (input(f'Digite Senha:'))
    if login != senha:
        teste = False
        
    else:
        print(f'\nErro - Digite Senha diferente do Login\n\n')    
print(f'Senha Criada com Sucesso!')
