"""
"# Sentencias de control: if, elif, else"
num = int(input("Ingrese un número: "))# Solicita al usuario que ingrese un número y lo convierte a entero
        # int: para que lo guarde como numero entero, no como texto

if num != 0: # Verifica si el número es diferente de cero
    if num > 0: # Verifica si el número es mayor que cero (es positivo)
        if num % 2 == 0: # Verifica si el número es divisible por 2 (es par)
            print(f'El número {num} es par y positivo') # Imprime que el número es par junto con el número ingresado
        else:
            print(f'El número {num} es impar y positivo')

    else:
     # Verifica si el número es menor que cero (es negativo)
        if num % 2 == 0: # Verifica si el número es divisible por 2 (es par)
            print(f'El número {num} es par y negativo') # Imprime que el número es par junto con el número ingresado
        else:
            print(f'El número {num} es impar y negativo')

    
else: # Si el número es igual a cero
    print(f"El número {num} es neutral") # Imprime que el número es cero
"""

"""""
vocal = input("Ingrese una letra: ") # Solicita al usuario que ingrese una letra

if vocal in "aeiouAEIOU": # Verifica si la letra ingresada es una vocal (tanto mayúscula como minúscula)
    print(f'La letra {vocal} es una vocal') # Imprime que la letra es una vocal junto con la letra ingresada
else:
    print(f'La letra {vocal} no es una vocal') # Imprime que la letra no es una vocal junto con la letra ingresada  
"""

"""
vocal = input("Ingrese una letra: ") # Solicita al usuario que ingrese una letra

if vocal =="a":
    print(f'La letra {vocal} es una vocal') # Imprime que la letra es una vocal junto con la letra ingresada
elif vocal =="e": #elif: si la letra no es "a", verifica si es "e"
    print(f'La letra {vocal} es una vocal') # Imprime que la letra es una vocal junto con la letra ingresada
elif vocal =="i":   
    print(f'La letra {vocal} es una vocal') # Imprime que la letra es una vocal junto con la letra ingresada
elif vocal =="o":
    print(f'La letra {vocal} es una vocal') # Imprime que la letra es una vocal junto con la letra ingresada
elif vocal =="u":
    print(f'La letra {vocal} es una vocal') # Imprime que la letra es una vocal junto con la letra ingresada
else:
    print(f'La letra {vocal} no es una vocal') # Imprime que la letra no es una vocal junto con la letra ingresada
"""

"""
#while: mientras se cumpla la condición, se ejecuta el bloque de código
cont = 1
suma = 0
num = int(input("Ingrese un número: ")) # Solicita al usuario que ingrese un número y lo convierte a entero
while cont <= num: # Mientras cont sea menor o igual a 10
    suma += cont # Suma el valor de cont a la variable suma(suma = suma + cont)
    cont += 1 # Incrementa el valor de cont en 1(cont = cont + 1)
print(suma) # Imprime el valor de suma
"""


"""
#Mostrar el número menor de n números ingresados
n = int(input("Ingrese la cantidad de números: "))
menor = 0
i = 1
while(i <=n):
    num = int(input("Ingrese un número: "))
    if i == 1: # Si es el primer número ingresado, se asigna a menor
        menor = num
    elif num < menor: # Si el número ingresado es menor que el valor actual de menor, se actualiza menor
        menor = num
    i += 1 # Incrementa el valor de i en 1
print(f'El número menor es: {menor}') # Imprime el número menor encontrado
"""



#for: para iterar sobre una secuencia (lista, tupla, diccionario, conjunto o cadena)
palabras = ["Hola", "Mundo", "Python", "Programación"] # Lista de palabras
for palabra in palabras: # Itera sobre cada palabra en la lista de palabras
    print(palabra, len(palabra)) # Imprime la palabra actual y su longitud

for i in range(1, 11): # Itera sobre los números del 1 al 10 (range(1, 11) genera una secuencia de números desde 1 hasta 10
    print(i) # Imprime el número actual