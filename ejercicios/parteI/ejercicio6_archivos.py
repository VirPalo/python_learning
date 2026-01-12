'''
Ejercicio 6: Lectura y escritura de archivos
Autora: Virginia Paloma
Año: 2025
'''
import csv

# Constantes
NOMBRE_ARCHIVO = 'parcelas.txt'

# Creo una lista de parcelas con número, propietario, superficie, zona
PARCELAS_INICIALES = [
    {'numero': 'P-001', 'propietario': 'Juan Perez', 'superficie': 320, 'zona': 'urbana'}, 
    {'numero': 'P-002', 'propietario': 'Maria Rodriguez', 'superficie': 180, 'zona': 'urbana'},
    {'numero': 'P-003', 'propietario': 'Catriel Cena', 'superficie': 200, 'zona': 'urbana'},
    {'numero': 'P-004', 'propietario': 'Jose Martinez', 'superficie': 500, 'zona': 'suburbana'}, 
    {'numero': 'P-005', 'propietario': 'Virginia Paloma', 'superficie': 150, 'zona': 'urbana'}
]


# Función para crear el archivo parcelas.txt
def crear_archivo(parcelas, nombre_archivo = NOMBRE_ARCHIVO):
    '''
    Crea un archivo CSV con la lista de parcelas.
    
    Args:
        parcelas (list): Lista de diccionarios con datos de parcelas
        nombre_archivo (str): Nombre del archivo a crear (default: 'parcelas.txt')
    '''
    
    
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['numero', 'propietario', 'superficie', 'zona'])
        escritor.writeheader()
        escritor.writerows(parcelas)
    print(f'Archivo "{nombre_archivo}" creado correctamente.')
    
# Función para agregar una parcela al archivo     
def agregar_parcela(parcela, nombre_archivo = NOMBRE_ARCHIVO):
    '''
     Agrega una nueva parcela al archivo CSV.
    
    Args:
        parcela (dict): Diccionario con datos de la parcela a agregar
        nombre_archivo (str): Nombre del archivo (default: 'parcelas.txt')
    '''
    
    with open(nombre_archivo, 'a', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['numero', 'propietario', 'superficie', 'zona'])
        escritor.writerow(parcela)

# Función para cargar el archivo .csv y usar siempre la ultima versión
def carga_archivo(nombre_archivo = NOMBRE_ARCHIVO):
    '''
    Carga todas las parcelas desde el archivo CSV.
    
    Args:
        nombre_archivo (str): Nombre del archivo a leer (default: 'parcelas.txt')
    
    Returns:
        list: Lista de diccionarios con los datos de las parcelas
    
    Nota:
        DictReader automáticamente:
        1. Lee la primera línea del archivo (encabezado)
        2. Guarda esos nombres como claves para los diccionarios
        3. A partir de ahí, cada línea se convierte en un diccionario
    '''
       
    parcelas = []
    
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for linea in lector:
                parcela = {'numero': linea['numero'], 'propietario': linea['propietario'], 'superficie': linea['superficie'], 'zona': linea['zona']}
                parcelas.append(parcela)
            
        return parcelas
    
    except FileNotFoundError:
        print(f'Error: El archivo "{nombre_archivo}" no existe.')
        return []
    
def mostrar_parcelas(parcelas):
    '''
    Muestra las parcelas en formato tabla.
    
    Args:
        parcelas (list): Lista de diccionarios con datos de parcelas
    '''
    
    if not parcelas:
        print('No hay parcelas para mostrar.')
        return
    
    print('..... Listado de parcelas .....')
    print('Número   | Propietario   | Superficie [m2]   | Zona')
    for parcela in parcelas:
        print(f'Número: {parcela['numero']} | Propietario: {parcela['propietario']} | Superficie: {parcela['superficie']} | Zona: {parcela['zona']}')

# Función principal

def main():
      
    '''
    Función principal del programa
    '''
    
    print('\n=== Sistema de Gestión de Parcelas ===')
    
    # Primero creo el archivo parcelas.csv
    print('\nCreando archivo con parcelas iniciales...')
    crear_archivo(PARCELAS_INICIALES)
    
    # Muestro parcelas iniciales
    print('\nParcelas cargadas inicialmente:')
    mostrar_parcelas(PARCELAS_INICIALES)
    
    # Agrego una parcela
    print('\nAgregando una nueva parcela...')
    nueva_parcela = {'numero': 'P-006', 'propietario': 'Juana Colonna', 'superficie': 400, 'zona': 'suburbana'}
    agregar_parcela(nueva_parcela)
   
    # Cargo y muestro todas las parcelas desde el archivo
    print('\nCargando archivo actualizado...')
    parcelas_actualizadas = carga_archivo()
    mostrar_parcelas(parcelas_actualizadas)
    
if __name__ == '__main__':
    main()
    
