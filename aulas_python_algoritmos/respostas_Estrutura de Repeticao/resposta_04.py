print(f'Programa para Cálculo de Projeção de população\n')
a = 80000
tx_anual_a = 1.030

b = 200000
tx_anual_b = 1.015

teste = True
while teste:
    for i in range (1,10000):
        a = a * tx_anual_a
        b = b * tx_anual_b
        print(f'Ano {i}: País A: {a} - País B: {b}')
        if a > b:
            teste = False
            break
print(f'A população do país A será maior do que o país B em {i} anos')