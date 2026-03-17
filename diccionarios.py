# Diccionarios en Python
personas = ['Sebas', 40 , 1.5]
print(personas) # Imprime la lista de personas

persona = {
    'nombre': 'Sebas',
    'edad': 26,
    'altura': 1.71,
    'accesorios': ['Gafas', 'Reloj']
}
#print(persona['altura']) # Imprime la altura de la persona
#print(persona['accesorios'][1]) # Imprime los accesorios de la persona
#print(persona.get('nombre')) # Imprime el nombre de la persona utilizando el método get()
#print(persona.keys()) # Imprime las claves del diccionario persona
#print(persona.values()) # Imprime los valores del diccionario persona
#print(persona.items()) # Imprime los pares clave-valor del diccionario persona
print(persona.pop('nombre')) # Imprime el nombre de la persona y lo elimina del diccionario

#Tuplas en Python
colores = ('Rojo', 'Verde', 'Azul') # Tupla de colores
print(colores.count('Rojo')) # Imprime la cantidad de veces que aparece 'Rojo' en la tupla
print(colores.index('Verde')) # Imprime el índice de 'Verde' en la tupla

#Sets (conjuntos) en Python
a = set('abracadabra') # Set de números
b = set('alakazam') # Otra forma de crear un set de números utilizando la función set()


print(a) # Imprime el set de números (los elementos se muestran sin orden y sin duplicados)
print(a-b) # Imprime el set de númerosb (los elementos se muestran