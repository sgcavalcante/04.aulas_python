
 
#entrada de dados
nota1 = float(input("Digite sua 1ª nota:\n"))
nota2 = float(input("Digite sua 2ª nota:\n"))
nota3 = float(input("Digite sua 2ª nota:\n"))
media = (nota1 *4 + nota2 * 5 + nota3 * 6)/15
#nota4=0.0
#conceitos:

media_invalida = media <0 or media > 10

aprovado =  media >= 7.0
recuperacao = media >=3 and media < 7.0  
reprovado = media < 3.0
#
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

    