vogais = ("a","b","c","d","e")

letra = input("Digite uma letrado alfabeto:\n")

eh_vogal = letra.lower() in vogais

if eh_vogal:
    print(f"É Vogal!")
else :
    print(f"Não é Vogal!")    