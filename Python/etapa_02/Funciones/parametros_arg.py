#Forma optima de sumar valores pasados mediante lista
def suma_total(numeros):
    return sum([*numeros])

#Llamamos a la función para asignarla a la variable resultado1
resultado1 = suma_total([5,15,23,41,17,36])

#Mostramos el resultado
print('-------------------------------------------------------')
print(resultado1)
print('-------------------------------------------------------')

#Forma optima de sumar valores pasados mediante lista per ahora usando (*args)
def suma_total2(nombre,*numeros):
    return f'{nombre}, la suma de los números es:{sum(numeros)}'

#Llamamos a la función para asignarla a la variable resultado1
resultado2 = suma_total2('Marcelo',5,15,23,41,17,36)

#Mostramos el resultado
print('-------------------------------------------------------')
print(resultado2)
print('-------------------------------------------------------')