
#entrada de dados
#nota1 = float(input("Digite sua 1ª nota:\n"))
#nota2 = float(input("Digite sua 2ª nota:\n"))
#nota3 = float(input("Digite sua 2ª nota:\n"))
 
#conceitos:


#
nota1 = float(input("Digite sua 1ª nota:\n"))
nota_invalida =  nota1 <0 or nota1 >10.0 
while nota_invalida: 
    print("Digite valor válido!")
    nota1 = float(input("Digite sua 1ª nota:\n"))
    nota_invalida =  nota1 <0 or nota1 >10.0 

nota2 = float(input("Digite sua 2ª nota:\n"))
nota_invalida =  nota2 <0 or nota2 >10.0 
while nota_invalida: 
    print("Digite valor válido!")
   
    nota2= float(input("Digite sua 2ª nota:\n"))
    nota_invalida =  nota2 <0 or nota2 >10.0 
nota3 = float(input("Digite sua 3ª nota:\n"))
nota_invalida =  nota3 <0 or nota3 >10.0 
while nota_invalida: 
    print("Digite valor válido!")
    nota3 = float(input("Digite sua 1ª nota:\n"))
    nota_invalida =  nota3 <0 or nota3 >10.0 
    


media = (nota1 *4 + nota2 * 5 + nota3 * 6)/15
media_invalida = media <0 or media > 10
nota_invalida = 0
aprovado =  media >= 7.0
recuperacao = media >=3 and media < 7.0  
reprovado = media < 3.0
if media_invalida:
    print(f"Média Inválida -> {media}")
elif aprovado:
    print(f"Parabéns! Sua média é {media}. Você foi APROVADO! \o/")
elif recuperacao:
    print(f"Quase! Sua média é {media}. Você está em RECUPERAÇÃO! |")  
    nota4 = float(input(f"Insira nota da 4ª avaliação:\n") )
    media = (nota4 + media)/2
    aprovado = media >= 5.0
    if aprovado >= 5:
        print(f"Você é cobra. Sua média final é {media} está APROVADO!")
    else:
        print(f"Até o próximo semestre nesta mesma disciplina. Sua média final é {media}. Você está REPROVADO!")    
elif reprovado:
    print(f"Que pena! Sua média é {media}. Você está REPROVADO por nota! :(")    

    