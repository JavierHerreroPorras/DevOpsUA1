from utils import sumar, restar, multiplicar, dividir
from data import numeros
print ("Adrián García")
def menu():
    print("=== Calculadora simple ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

while True:
    menu()
    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("¡Hasta luego!")
        break

    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))

    if opcion == "1":
        print("Resultado:", sumar(a, b))
    elif opcion == "2":
        print("Resultado:", restar(a, b))
    elif opcion == "3":
        print("Resultado:", multiplicar(a, b))
    elif opcion == "4":
        print("Resultado:", dividir(a, b))
    else:
        print("Opción no válida")
