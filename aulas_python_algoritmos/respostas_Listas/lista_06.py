notas = []
soma = 0
n=0
teste = True
num_alunos = 10
num_notas = 4
while teste:
    for aluno in range(num_alunos):
        print(f'=================================')
        print(f'Digite as notas do aluno{aluno+1}.')
        print(f'---------------------------------')
        soma = 0
        for nota in range(num_notas):
            n=float(input(f'Digite a nota {nota+1} do aluno {aluno+1}:'))
            soma+=n
        notas.append(soma/num_notas)
    teste = False    
print(notas)   
print(notas[0])  
print(f'=================================')
print(f'Relacao de alunos com nota maior ou igual a 7.0')
for i in range(0,num_alunos):
    
    if (notas[i] >=7.0):
        print(f'Aluno {i+1} - Nota{notas[i]} ')



    