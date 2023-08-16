print(f'Programa para Cálculo de Projeção de população\n')
a = 80000
tx_anual_a = 1.030

b = 200000
tx_anual_b = 1.015


testea = True

 

teste = True
while teste:
    
    
    while testea:
        testeb=0
        print(f'\n{10*"="}Projeção Populacional!{10*"="}')
        a = float(input(f'Digite a população do país A:'))
        if a < 0 :
            print(f'Digite informação válida!')
            break
        else:
            testeb+=1

        tx_anual_a  = float(input(f'Digite a taxa de crescimento da população do país A:'))
        if tx_anual_a < 0 or tx_anual_a > 5:
            print(f'Digite informação válida!')  
            break
        else:
            testeb+=1


        b = float(input(f'Digite a população do país B:'))
        if b < 0 :
            print(f'Digite informação válida!')
            break
        else:
            testeb+=1

        tx_anual_b  = float(input(f'Digite a taxa de crescimento da população do país B:'))
        if tx_anual_b < 0 or tx_anual_b > 5:
            print(f'Digite informação válida!')   
            break
        else:
            testeb+=1

        if testeb == 4:
            print(f'Dados Verificados!')
            for i in range (1,10000):
                a *= tx_anual_a
                b *= tx_anual_b
                
                print(f'Ano {i}: País A: {a} - País B: {b}')
                input()
                if (a > b):
                    #teste = False
                    print(f'\nA população do país A será maior do que o país B em {i} anos')
                    break
        else:
            print(f'Reveja seus dados!')
    
    