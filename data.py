# Datos de ejemplo para practicar con el repo
numeros = [10, 20, 30, 40, 50]

def mostrar_datos():
    for n in numeros:
        print(f"[Comp1] Numero actual -> {n}")
        if n % 2 == 0:
            print(f"[Comp2] Numero par: {n}")
    print("Fin de la lista de numeros (Comp1)")
    print("Procesamiento terminado (Comp2)")
    print("¡Cambio de prueba aplicado!")  # Pequeña modificación extra
