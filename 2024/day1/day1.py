from collections import Counter

data_file = 'lista.csv'

def Distancia(data_file):
    fila_izq = []
    fila_der = []
    # Abre el archivo CSV y separa valores en las dos listas
    with open(data_file, mode='r',) as csvfile:
        for row in csvfile:
            a, b = map(int, row.split('   '))
            fila_izq.append(a)
            fila_der.append(b)
    fila_izq.sort()
    fila_der.sort()
    distancia_total = sum(abs(a-b) for a,b in zip(fila_izq, fila_der))
    return distancia_total

def Similaridad(data_file):
    fila_izq = []
    fila_der = []
    # Abre el archivo CSV y separa valores en las dos listas
    with open(data_file, mode='r',) as csvfile:
        for row in csvfile:
            a, b = map(int, row.split('   '))
            fila_izq.append(a)
            fila_der.append(b)
            
            contador_der = Counter(fila_der)
            similitud_total = sum(a * contador_der[a] for a in fila_izq)
    return similitud_total
    
        
print(Distancia(data_file))
print(Similaridad(data_file))
# Llamar a la función para llenar las listas antes de imprimir
