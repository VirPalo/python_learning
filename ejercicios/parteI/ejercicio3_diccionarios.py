'''
Ejercicio 3: Diccionarios
Autora: Virginia Paloma
Año: 2025
'''

# 1. Creo un diccionario con los datos de una parcela

parcela1 = {
    'numero' : '0001',
    'partida' : '10-0-0-111111/0000',
    'manzana' : 42,
    'superficie' : 320, # en m2
    'propietario' : 'Juan Perez',
    'zona' : 'urbana'
}

print('Datos de la Parcela:')
for clave, valor in parcela1.items():
    print(f' - {clave} : {valor}')

# 2. Modificar propietario
parcela1['propietario'] = 'Pedro Perez'
print(f'\nPropietario actualizado: {parcela1['propietario']}')

# 3. Agregar un campo de observaciones
parcela1['observaciones'] = 'No posee servicios'
print('\nParcela actualizada:')
for clave, valor in parcela1.items():
    print(f' - {clave} : {valor}')
    
# Otro ejemplo ________________________________________________________________

# Contactos
contactos = {
    'Alicia' : {'tel' : '341-155100000', 'email' : 'alicia@correo.com'},
    'Virginia' : {'tel' : '341-155100001', 'email' : 'virginia@correo.com'},
    'Catriel' : {'tel': '341-155100002', 'email' : 'catriel@correo.com'}
}

print('\nLista de contactos:')
for clave, valor in contactos.items():
    print(f' - {clave} : {valor['tel']} - {valor['email']}')

# Agrego un contacto
contactos['Pedro'] = {'tel': '341-155100003', 'email' : 'pedro@correo.com'}
print('\nContacto agregado correctamente.')

# Modifico un email
contactos['Alicia']['email'] = 'alicia.modificado@correo.com'
print('\nContacto actualizado.')

# Muestro el contacto actualizado
print('\nLista de contactos actualizada:')
for clave, valor in contactos.items():
    print(f' - {clave} : {valor['tel']} - {valor['email']}')
