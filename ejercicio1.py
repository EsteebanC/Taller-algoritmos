import math


def busqueda_binaria(arreglo, objetivo):
    low = 0
    high = len(arreglo) - 1
    traza = []

    while low <= high:
        mid = (low + high) // 2

        traza.append((low, high, mid))

        if arreglo[mid] == objetivo:
            return mid, traza

        elif arreglo[mid] < objetivo:
            low = mid + 1

        else:
            high = mid - 1

    return -1, traza


# Caso aplicado
guias = list(range(1, 50001))
guia_buscada = 38417

posicion, traza = busqueda_binaria(guias, guia_buscada)


# A. Traza de las primeras 5 iteraciones
print("TRAZA DE LAS PRIMERAS 5 ITERACIONES")

for i, (low, high, mid) in enumerate(traza[:5], 1):
    print(f"Iteración {i}: low={low}, high={high}, mid={mid}")


# B. Complejidad
comparaciones_binaria = math.floor(math.log2(len(guias))) + 1
comparaciones_lineal = len(guias)

print("\nCOMPLEJIDAD")
print(f"Búsqueda binaria: {comparaciones_binaria} comparaciones máximas")
print(f"Búsqueda lineal: {comparaciones_lineal} comparaciones máximas")
print("Complejidad de la búsqueda binaria: O(log n)")
print("Complejidad de la búsqueda lineal: O(n)")


# C. Crecimiento a 50 millones de registros
registros_50_millones = 50_000_000

comparaciones_50_millones = (
    math.floor(math.log2(registros_50_millones)) + 1
)

print("\nCRECIMIENTO DE LOS REGISTROS")
print(f"50.000 registros: {comparaciones_binaria} comparaciones")
print(f"50 millones de registros: {comparaciones_50_millones} comparaciones")

print(
    "\nCONCLUSIÓN:"
    "\nLa búsqueda binaria crece de forma logarítmica."
    "\nPor eso, al pasar de 50.000 a 50 millones de registros,"
    "\nlas comparaciones máximas aumentan de 16 a 26."
)

print(
    "\nSi las guías no están ordenadas por número de guía,"
    "\nprimero se deben ordenar por ese criterio para poder"
    "\naplicar correctamente la búsqueda binaria."
)