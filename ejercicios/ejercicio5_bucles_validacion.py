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
    
    