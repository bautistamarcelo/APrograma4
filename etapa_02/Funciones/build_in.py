#Creamos una lista iterable de números para ver funciones numéricas
num = [1,3,5,7,9,12,15,18]

#Encontremos el número más alto de la lista
num_mas_alto = max(num)
print('-----------------------------------------------------------')
print(f'El número más alto de la lista es: {num_mas_alto}')
print('-----------------------------------------------------------')

#Encontremos el número más bajo
num_mas_bajo = min(num)
print('-----------------------------------------------------------')
print(f'El número más bajo es: {num_mas_bajo}')
print('-----------------------------------------------------------')

#Sumemos los valores de la lista numerica
num_sumados = sum(num)
print('-----------------------------------------------------------')
print(f'La suma de todos los números da: {num_sumados}')
print('-----------------------------------------------------------')

#La función bool nos retorna falso siempre que por parámetros le pasemos 
#los valores 0, null, vacío, false, none
resultado_bool = bool(0)
print(f'El resultado de la función bool es: {resultado_bool}')
print('-----------------------------------------------------------')

#La función all nos retorna true siempre que todos los datos iterables pasados
#como parámetros sean verdaderos o distintos de nulo, 0, vacío, o none
resultado_all = all([None,"falaz",True,[125,14]])
print(f'El resultado de la función all es: {resultado_all}')
print('-----------------------------------------------------------')