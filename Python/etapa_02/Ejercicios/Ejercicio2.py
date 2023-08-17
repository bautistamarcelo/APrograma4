#Creamos dos variables para contener los valores a trabajar
num1 = int(input("Ingrese el dividendo: "))
num2 = int(input("Ingrese el divisor: "))
if num2 == 0:
    print("ERROR, no es posible dividir por 0")
else:
    print(f'el resultado de dividir {num1}/{num2} es: {num1/num2}')
    