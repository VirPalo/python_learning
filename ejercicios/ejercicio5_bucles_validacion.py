'''
Ejercicio 5: Bucles y Validación de entradas
Autora: Virginia Paloma
Año: 2025
'''

def obtener_num_positivo(mensaje):
    '''
    Solicita un número positivo al usuario.
    
    Args:
        mensaje (str): Mensaje a mostrar
    
    Return:
        num (float): Número positivo validado
    '''
    
    while True:
        try:
            num = float(input(mensaje))
            if num <= 0:
                print('Error: El número debe ser positivo.')
                continue
            return num
        except ValueError:
            print('Error: Ingrese un valor numérico válido.')
            
def clasificar_parcela(superficie):
    '''
    Clasifica una parcela según su superficie.
    
    Args:
        superficie (float): Superficie en metros cuadrados [m2]
        
    Return:
        tipo (str): Clasificación de la superficie
    '''
    
    if superficie < 1000:
        tipo = 'Pequeña'
    elif superficie < 5000:
        tipo = 'Mediana'
    elif superficie < 10000:
        tipo = 'Grande'
    else:
        tipo = 'Muy Grande'
    
    return tipo
        

# Funcion que agrupa el código principal
def main():
    print('\n--- Clasificador de Parcelas Rurales ---')
    
    cant = int(obtener_num_positivo('\n¿Cuántas parcelas desea clasificar?'))
    
    for i in range(1, cant + 1):
        print(f'\n--- Parcela {i} ---')
        superficie = obtener_num_positivo('\nIngrese la superficie en metros cuadrados [m2]: ')
        clasificacion = clasificar_parcela(superficie)
        hectareas = superficie / 1000
        print(f'\nSuperficie: {hectareas:.2f} has. | Clasificación: {clasificacion}')
        

if __name__ == '__main__':
    main()


    