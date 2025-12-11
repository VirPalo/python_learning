'''
Ejercicio 2: Listas
Autora: Virginia Paloma
Año: 2025
'''

# Creación de listas

num_pares = [2, 4, 6, 8, 10]
print(num_pares)

num_impares = list((1, 3, 5, 7, 9))
print(num_impares)

num_rango = list(range(10))
print(num_rango)

num_divisibles_por_dos = [number for number in range(1, 10) if number % 2 == 0]
print(num_divisibles_por_dos)

# Listas vacías

lst_vacia = []
print(lst_vacia)

otra_lst_vacia = list()
print(otra_lst_vacia)

# Ejercicio con una lista

# 1. Creo una lista de ciudades
ciudades = ['Buenos Aires', 'Rosario', 'Cordoba', 'Mendoza', 'Santa Fe', 'Posadas']
print('Lista inicial:', ciudades)

# 2. Agrego ciudades
ciudades.append('San Miguel de Tucuman')
print('Lista actualizada:', ciudades)

ciudades.extend(['San Salvador de Jujuy', 'Mar del Plata']) # Extend es como si concatenara las dos listas
print('Lista actualizada:', ciudades)

ciudades.insert(1, 'Villa Carlos Paz')
print('Lista actualizada:', ciudades)

# 3. Elimino la ultima ciudad
ciudad_eliminada = ciudades.pop(-1)
print('Ciudad eliminada:', ciudad_eliminada)
print('Lista actualizada:', ciudades)

# 4. Ordeno la lista alfabeticamente
ciudades.sort()
print('Lista ordenada:', ciudades)

# 5. Imprimo cada ciudad con un indice
print('Lista de ciudades:')
for i, ciudad in enumerate(ciudades, 1):
    print(f'{i}. {ciudad}')





