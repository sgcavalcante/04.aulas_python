numeros=[]
for i in range(4):
    numeros.append(int(input(f'Digite nota {i+1}:\n')))



print(f'A média das notas é: {sum(numeros)/len(numeros)}')    