#Creamos dos variables para contener los valores a trabajar
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 < num2:
    print(f'El número1: {num1}, es menor que el número2 {num2}')
elif num1 > num2:
    print(f'El número1: {num1}, es mayor que el número2 {num2}')
else:
    print(f'los números 1 y 2: ({num1} / {num2}), son iguales')
    