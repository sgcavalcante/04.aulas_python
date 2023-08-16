altura = []
idade=[]
n=5

for i in range(0,5):
    print(f'=================================')
    idade.append(int(input(f'Digite idade {i+1}.')))
    altura.append(float(input(f'Digite altura {i+1}.')))

#print(f'Idade {idade}')   
print(f'=========Ordem Inversa===========') 
for i in range(5):
    print(f'{idade[i]}  ---  {idade[4-i]}')
 

 