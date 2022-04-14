# Variables:

'''
entero = 1
flotante = 1.1
booleano = True
palabra = 'hola'

a = input("Escribi lo que quieras wachin: ")
print(type(a)) # "156"

firstNumToPlus = int(input("Inserta el primer numero a sumar: "))
secondNumToPlus = int(input("Inserta el segundo numero a sumar: "))
input("hola") # cadena de caracteres

cajaDeZapatos = "Remeras"
cajaDeRemeras = "Zapatos"
cajaDeApoyo = ""

cajaDeApoyo = cajaDeRemeras # cajaDeApoyo = "Zapatos" y cajaDeRemeras = "Zapatos" y cajaDeZapatos = "Remeras"
cajaDeRemeras = cajaDeZapatos
cajaDeZapatos = cajaDeApoyo
print(cajaDeZapatos)
print(cajaDeRemeras)

# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por
# hora. Después debe mostrar por pantalla la paga que le corresponde.

preguntarLashorasTrabajadas = int(input("¿Cuantas horas trabajaste?: "))
preguntarElPrecioPorHora = int(input("¿Cuanto te pagan la hora?: "))
pagoDiario = preguntarLashorasTrabajadas * preguntarElPrecioPorHora
print("Tenes q cobrar", pagoDiario, "pesos. Tus horas trabajadas fueron", preguntarLashorasTrabajadas, "Y tu paga por hora es", preguntarElPrecioPorHora)

# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance
# final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero.
# depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular
# y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear
# cada cantidad a dos decimales.


preguntarDineroADepositar = int(input("Buenos días, indicame por favor el importe que vas a depositar hoy: "))
interesAnualAño1 = preguntarDineroADepositar * 1.04
interesAnualAño2 = round(interesAnualAño1 * 1.04, 0)
interesanualAño3 = round(interesAnualAño2 * 1.04, 0)
print("El saldo de tu cuenta al final de año va a ser:", interesAnualAño1, "pesos.")
print("Pensamos que te gustaría saber también que el segundo año serán:", interesAnualAño2)
print("Y por último el tercer año tu saldo sería:", interesanualAño3, ". Muchas gracias por consultar")


# Estructura de Flujo de datos: Condicionales
cajaDeAhorroEnPesos = int(input("Digame su saldo en la caja de ahorro en pesos, si es igual o supero los $1000 usted sera apto para tener una tarjeta de credito: "))
siEsMayorA1000CajaDeAhorro = (cajaDeAhorroEnPesos >= 1000)
if siEsMayorA1000CajaDeAhorro:
    print("Sos apto para pedir una tarjeta de credito")
    confirmarPedidoDeTarjetaDeCredito = input("Queres pedir la tarjeta?(por favor conteste SI o NO)")
    if confirmarPedidoDeTarjetaDeCredito == "SI":
        print("Su pedido esta siendo procesado, felicitaciones")
    elif confirmarPedidoDeTarjetaDeCredito == "NO":
        print("Que cagada che")
    else:
        print("Escribime bien pelotudo")
else:
    print("No sos apto para pedir una tarjeta de credito")

# Operadores Logicos
# mayor > menor ------- menor < mayor ------ mayor o igual >= menor o igual --------- menor o igual <= mayor o igual
# igual == igual ------ condicional and condicional --------- condicional or condicional

bool1 = True
bool2 = True
bool3 = False
if bool1 and (bool2 or bool3):
    if (bool1 or bool3):
        print("Hola Mundo")


# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad
# o no. (La mayoria de edad es a partir de los 18 años inclusive)

edadDelUsuario = int(input("Ingresa tu edad: "))
mayorDeEdad = (edadDelUsuario >= 18)
if mayorDeEdad:
    print("sos mayor")

else:
    print("no sos mayor")
'''
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte
# al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario
# coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el
# divisor es cero el programa debe mostrar un error.
# (El error debe ser mostrado en pantalla con el msg "error no de puede dividir por 0")

# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o
# impar.
# (Para este ejercicio necesitas hacer uso de modulo "%". El modulo te da como resultado la resta de una divicion)
# Te dejo un ejemplo para que lo veas

variableModulo = 25 % 4
# el primero numero es el dividendo(numero a dividir),
# el segundo es el divisor (el que divide),
# el resultado de esta ecuacion no te va a dar el resultado de 25 divido 4,
# sino la resta se esa divicion (que es el numero que le falta a 25 para llegar a ser divisible por 4)
print(variableModulo)

# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos
# iguales o superiores a $100000 mensuales. Escribir un programa que pregunte al usuario su edad y
# sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
# calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa
# debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es
# menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18
# años, $1000.

# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
# ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de
# su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede
# elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se
# debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
# jhgjg

