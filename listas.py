datos = [1 , 2, 3, 'q', 'Sebastian', 4.5, True] # Lista de datos con diferentes tipos de elementos
print(datos) # Imprime la lista de datos
print(datos[0]) # Imprime el primer elemento de la lista (1)

#Tengo una tienda online con articulos
productos = ["Camisa", "Pantalón", "Zapatos", "Gorra"] # Lista de productos

productos[0] = "Sombrero" # Modifica el primer elemento de la lista (Camisa por Camiseta)

new_product = productos.copy() # Crea una copia de la lista de productos y la asigna a new_product
new_product[0] = 'Billetera' # Modifica el primer elemento de la lista (Sombrero por Billetera)
new_product.append("Cinturón") # Agrega un nuevo elemento al final de la lista (Cinturón)

productos.extend(new_product) # Agrega los elementos de new_product al final de la lista productos

new_product.insert(0, "Gafas") # Inserta un nuevo elemento en la posición 0 de la lista (Gafas)

productos.remove("Zapatos") # Elimina el elemento "Zapatos" de la lista productos
productos.clear() # Elimina todos los elementos de la lista productos

new_product.pop(1) # Elimina el último elemento de la lista new_product (Cinturón)
new_product.reverse() # Invierte el orden de los elementos en la lista new_product
new_product.sort() # Ordena los elementos de la lista new_product en orden alfabético

print(new_product.index("Gorra")) # Devuelve el índice del elemento "Gorra" en la lista new_product (0)
print(new_product.count("Gorra")) # Devuelve el número de veces que el elemento "Gorra" aparece en la lista new_product (1)

print(productos) # Imprime la lista de productos
print(new_product) # Imprime la lista de productos (new_product es una referencia a la misma lista que productos)

