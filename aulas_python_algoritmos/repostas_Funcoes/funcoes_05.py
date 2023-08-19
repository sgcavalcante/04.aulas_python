def somaimposto(taxaimposto,custo):
    valorfinal = custo + (custo * (taxaimposto/100))
    print(f'Valor Final com Imposto: {valorfinal}')

custo       = float(input('Dgite o Custo do produto:\n'))    
taxaimposto = float(input('Dgite o valor do Imposto no formato %:\n'))   

somaimposto(taxaimposto,custo)