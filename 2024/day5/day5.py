orden = "orden.txt"
update = "update.txt"
def procesar_orden(archivo_orden, archivo_update):
    with open(archivo_orden,  'r') as orden_file:
        reglas = [tuple(map(int, line.strip().split('|'))) for line in orden_file if line.strip()]
    with open(archivo_update, 'r') as update_file:
        actualizaciones = [
            list(map(int, line.strip().split(','))) for line in update_file if line.strip()
        ]
    def es_correcta(update, reglas):
        for x, y in reglas:
            if x in update and y in update:
                if update.index(x) > update.index(y):
                    return False
        return True
    ##
    # La función es_correcta verifica si una
    # actualización cumple con las reglas dadas.
    
    suma_medios = 0
    for update in actualizaciones:
        if es_correcta(update, reglas):
            medio = update[len(update)//2] # // Devuelve la parte entera de la división
            suma_medios += medio
    return suma_medios
    

print("La suma de los elementos medios es:", procesar_orden(orden, update))