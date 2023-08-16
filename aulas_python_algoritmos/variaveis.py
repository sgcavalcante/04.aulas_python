numero1 = int(input("Digite o 1º número:\n"))

numero2 = int(input("Digite o 2º número:\n"))

soma             = numero1  +  numero2
subtracao        = numero1  -  numero2
multiplicacao    = numero1  *  numero2
divisao          = numero1  /  numero2
divisao_inteira  = numero1  // numero2
resto_da_divisao = numero1  %  numero2

#print("A soma dos números é:",soma)
#print("A divisão inteira dos números é:",divisao_inteira)
#print("O resto da divisão dos números é:",resto_da_divisao)

print(f"A soma do {numero1} com o {numero2} é {soma}")
print(f"A subtração do {numero1} com o {numero2} é {subtracao}")
print(f"A multiplicação do {numero1} com o {numero2} é {multiplicacao}")
print(f"A divisão do {numero1} pelo {numero2} é {divisao}")
print(f"A divisão inteira do {numero1} pelo {numero2} é {divisao_inteira}")
print(f"O resto da divisão do {numero1} pelo {numero2} é {resto_da_divisao}")