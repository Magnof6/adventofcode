df = 'lista.txt'

def es_seguro(numeros):
    
    difs = [numeros[i+1]-numeros[i] for i in range(len(numeros)-1)]
    
    creciente = all(d > 0 for d in difs)
    decreciente = all(d < 0 for d in difs)
    
    if not (creciente or decreciente):
        return False
    if not all( 1 <= abs(d) <= 3 for d in difs):
        return False
    return True

def contar_seguros(df):
    contador = 0
    with open(df, 'r') as file:
        for line in file:
            numeros = list(map(int, line.split()))
            if es_seguro_v2(numeros):
                contador += 1
    return contador

def es_seguro_v2(numeros):
    if es_seguro(numeros):
        return True
    for i in range(len(numeros)):
        lista_reducida = numeros[:i]+ numeros[i+1:]
        if es_seguro(lista_reducida):
            return True
    return False

print(f"{contar_seguros("lista.txt")} +  seguros encontrados")