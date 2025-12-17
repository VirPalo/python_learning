'''
Ejercicio 4: Funciones
Autora: Virginia Paloma
Año: 2025
'''

import math

# 1. Calcular el área de un rectangulo
def area_rectangulo(base, altura):

    '''
    Calcula el área de un rectangulo.

    Args:
        base (float): Base del rectangulo
        altura (float): Altura del rectangulo
        
    Return:
        area (float): Área del rectangulo

    '''

    area = base * altura
    return area

# 2. Calcular el área de un círculo
def area_circulo(radio):
    '''
    Calcula el área de un círculo.

    Args:
        radio (float): Radio del círculo
        
    Return:
        area (float): Área del círculo
    '''
    
    area = math.pi *(radio ** 2)
    return area

# 3. Calcular promedio entre 3 valores
def promedio(a, b, c):
    '''
    Calcula el promedio de 3 valores.
    
    Args:
        a (float): Valor uno 
        b (float): Valor dos 
        c (float): Valor tres
    
    Return:
        prom (float): Promedio de los 3 valores
    '''
    
    prom = (a + b + c) / 3
    return prom

# 4. Conversion de segundos a horas

def seg_a_horas(segundos):
    '''
    Conversión de segundos a horas
    
    Args:
        segundos (int): Segundos
    
    Return:
        horas (float): Horas
    '''
    
    horas = (segundos / 60) / 60
    return horas

# Función que agrupa el código principal
def main():
    print('\n--- Funciones ---')
    
    print('\nCálculo del área de un rectangulo:')
    base = 10
    altura = 5
    area_rec = area_rectangulo(base, altura)
    print(f'El área de un rectángulo de {base} m por {altura} m es {area_rec:.2f} m2.')
    
    print('\nCálculo del área de un círculo:')
    radio = 3.5
    area_circ = area_circulo(radio)
    print(f'El área de un círculo de radio {radio} m es {area_circ:.2f} m2.')
    
    print('\nCálculo del promedio entre 3 valores:')
    a = 9
    b = 8
    c = 8.5
    prom = promedio(a, b, c)
    print(f'El promedio entre los valores {a}, {b} y {c} es {prom:.2f}.')
    
    print('\nConversión de segundos a horas:')
    segundos = 355
    horas = seg_a_horas(segundos)
    print(f'{segundos} segundos equivalen a {horas:.2f} horas.')
    
    
if __name__ == '__main__':
    main()