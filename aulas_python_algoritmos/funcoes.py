def bem_vindo():
    print("Bem Vindo")

def entrada(texto):
    return int(input(texto))

def somar(numero1,numero2):
    resultado = numero1 + numero2
    return resultado

n1 = entrada("Digite um número: ")
n2 = entrada("Digite outro número: ") 

resultado = somar(n1,n2)

print(resultado)