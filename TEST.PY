milista = [1,2,3,4]

def sumador_array_1d(arr : list) -> list:
    nueva_lista = []
    sumador = 0

    for i in arr:
        sumador += i
        nueva_lista.append(sumador)
    
    return nueva_lista

print(sumador_array_1d(milista))