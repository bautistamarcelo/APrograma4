#LISTAS:
    #Una lista es una estructura de datos en la que puedes añadir elementos para su posterior uso
    #permiten guardar cualquier tipo de dato, ya sea enteros, cadenas, objetos e incluso otras listas.
    #Para declarar una lista vacía se puede hacer con list() o con [].
lista1 = list()
lista2 = []

print('-------------------------------------------------------------')
print(f'la variable lista1 es de tipo {type(lista1)}')
print('-------------------------------------------------------------')
print(f'la variable lista2 es de tipo {type(lista2)}')
print('-------------------------------------------------------------')

#También podemos crear una lista con información predefinida:
my_list = list([7,6,3,4])
my_list2 = ['a', 'x', 'd']

print('-------------------------------------------------------------')
print(f'la variable my_list contiene {my_list}')
print('-------------------------------------------------------------')
print(f'la variable my_list2 contiene {my_list2}')
print('-------------------------------------------------------------')

#Para obtener el valor de una posición en concreto deberemos escribir el nombre de la lista, abrir corchetes, poner el número de la posición donde se encuentra el dato que queremos obtener y cerrar corchete.

# Mostrará el primer valor de la lista que es 7
print('-------------------------------------------------------------')
print(f'Mostramos el primer valor de la lista [7,6,3,4]: {my_list[0]}')
print('-------------------------------------------------------------')

# Mostrará el segundo valor de la lista que es 6
print(f'Mostramos el segundo valor de la lista [7,6,3,4]: {my_list[1]}')
print('-------------------------------------------------------------')

#En el caso de querer recorrer todos los valores de una lista podemos hacerlo con el bucle for.
lista3 = [7, 5, 9, 2, 3, 4]
posicion = 0
print('--------------------------------------------------------')
print('Para la lista [7, 5, 9, 2, 3, 4]')
print('--------------------------------------------------------')
for value in lista3:
    print(f'  en su posición {posicion} el valor es: {value}')
    print('--------------------------------------------------------')
    posicion = posicion+1

#Para añadir un elemento a la última posición de la lista lo haríamos con el método append.
lista3.append('hello')

# Después de esto el contenido de la lista será [7, 5, 9, 2, 3, 4 'hello']
print(f'Usando append la lista queda asi: {lista3}')
print('------------------------------------------------------------------------------')

#Para añadir un elemento en una posición en concreto usaremos el método insert donde el primer parámetro será la posición y el segundo el dato a insertar.
lista4 = list([7,6,3,4,5])
lista4.insert(3, 'test')

print('----------------------------------------------------------------------------------------')
print('Para la lista [7,6,3,4,5]')
print('----------------------------------------------------------------------------------------')
print(f'  usando insert en posición (3), el valor de la lista ahora es: {lista4}')
print('----------------------------------------------------------------------------------------')
# Ahora el valor de la lista es [7, 6, 3, 'test', 4, 5]

#Cuando queramos sustituir el valor de una posición en concreto deberemos escribir el nombre de la lista, abrir corchetes y añadir la posición del dato que queremos reemplazar, cerramos corchetes, escribimos igual y ya añadimos el valor que le queramos dar.
lista5 = list([7,6,3,4,5])

lista5[1] = 4
print('----------------------------------------------------------------------------------------')
print('Para la lista [7,6,3,4,5]')
print('----------------------------------------------------------------------------------------')
print(f'  especificando la posición (en este caso [1]), podemos reemplazar su valor y nos queda: {lista5}')
print('----------------------------------------------------------------------------------------')
# Ahora el valor de la lista es [7, 4, 3, 4, 5]
