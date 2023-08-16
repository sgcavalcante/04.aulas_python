numero = int(input("Informar número da Tabuada que deseja:\n"))

numeros = range(1,11)

print(f"===== Tabuada de {numero}=====")
for n in numeros:
    print(f"{numero}\tX\t{n}\t=\t{numero * n}")
print(f"====================")    
             