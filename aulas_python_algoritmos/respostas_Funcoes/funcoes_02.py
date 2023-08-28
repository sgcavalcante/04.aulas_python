
def imprimir(n):
    cont=1
    for i in range(0,n):
        for j in range(0,cont):
            print(str(j+1) ,end="")
        cont+=1
        print("")
n = int(input(f'Digite número:\n'))
imprimir(n)   