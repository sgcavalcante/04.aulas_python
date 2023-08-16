#estrutura de repetição
resposta_nao_for_sim = True
contador = 1
while resposta_nao_for_sim:
    resposta = input(f"Você gosta de mim?\nTentativa {contador}\n")
    resposta_nao_for_sim = resposta != "sim"
    if resposta_nao_for_sim:
        print("Que pena, repita novamente!")
    else:
        print("Parabens, você é um ótimo amigo!")    
    contador += 1