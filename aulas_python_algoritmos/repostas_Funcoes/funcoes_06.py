def converte(hora,min1):
    if hora <12 :
        h = hora
        ampm = "AM"
    else:
        h = hora - 12   
        ampm = "PM" 
    return h,min1,ampm

def imprime(h,min):
    hora,min1,ampm = converte(h,min)
    print(f'A hora convertida é: {hora}:{min:02d} - {ampm}')

hora = int(input('Digite a hora a ser convertida:\n'))    
min = int(input('Digite os minutos:\n'))    
imprime(hora,min)