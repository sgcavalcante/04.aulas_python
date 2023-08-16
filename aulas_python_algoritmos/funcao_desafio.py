#
#Confira a tabela de contribuição do INSS 2023: 
#Até R$1.320,00 – 7,5%
#De R$1.320,00 até R$2.571,29 – 9%
#De R$2.571,30 até R$3.856,94 – 12% 
#De R$3.856,95 até R$7.507,49 – 14%

faixa1 = 1320.00
faixa2 = 2571.94
faixa3 = 3856.94
faixa4 = 7507.49

alicota = [0.075,0.090,0.120,0.140]
faixas = [1320.00,2571.94,3856.94,7507.49]
salario = 0.0
imposto = 0.0
resto = 0

def imposto_previdenciario(salario):

    #for i in range(len(alicota)):
         
    if salario < faixa1:
        imposto = salario * alicota[0]
        resto = salario - imposto
        
    elif salario >= faixa1 and salario < faixa2:
        imposto = (faixa1)            * alicota[0] 
        imposto = (salario - faixa1 ) * alicota[1] + imposto
          
         

    elif salario >= faixa2 and salario < faixa3:
         
        imposto = (faixa1 - 0)        * alicota[0] 
        imposto = (faixa2 - faixa1 )  * alicota[1] + imposto
        imposto = (salario - faixa2 ) * alicota[2] + imposto


    elif salario >= faixa3 and salario < faixa4:
        imposto = (faixa1 - 0)        * alicota[0] 
        imposto = (faixa2 - faixa1 )  * alicota[1] + imposto
        imposto = (faixa3 - faixa2 )  * alicota[2] + imposto
        imposto = (salario - faixa3 ) * alicota[3] + imposto


    else:
        imposto = (faixa1 - 0)         * alicota[0] 
        imposto = ((faixa2 - faixa1 )  * alicota[1]) + imposto
        imposto = ((faixa3 - faixa2 )  * alicota[2]) + imposto
        imposto = ((faixa4 - faixa3 )  * alicota[3]) + imposto
        #imposto = salario - faixa4 - imposto
        
    print(imposto)
    return 


salario = float(input(f'Digite seu Salário:\n'))
imposto_previdenciario(salario)


