# En app.py
from algoritmos.AmericanoIterativoEstatico import multiplicar as multAmericanoIterativoEstatico
from algoritmos.InglesaIterativoEstatico import multiplicar as multInglesaIterativoEstatico
from algoritmos.AmericanoRecursivoEstatico import multiplicar_recursivo as multAmericanoaRecursivoEstatico
from algoritmos.InglesaRecursivoEstatico import multiplicar_recursivo as multInglesaRecursivoEstatico
from algoritmos.AmericanoIterativoDinamico import multiplicar_dinamico as multAmericanoIterativoDinamico
from algoritmos.InglesaIterativoDinamico import multiplicar_dinamico as multInglesaIterativoDinamico
from algoritmos.AmericanoRecursivoDinamico import multiplicar_recursivo_dinamico as multAmericanoRecursivoDinamico
from algoritmos.InglesaRecursivoDinamico import multiplicar_recursivo_dinamico as multInglesaRecursivoDinamico
from algoritmos.HinduIterativoEstatico import multiplicar as multHinduIterativoEstatico
from algoritmos.DivideYVenceras import multiplicar as multDivideYVenceras
# Definición de los arreglos a multiplicar
arreglo1 = [1, 2, 3,4,5,6,7,8,9,1,4,5,6,4,2,4,2,1,4,5,6,4,3,1,3,2,4,5,6,7,5,1,4,3,2]
arreglo2 = [1, 2, 3,4,5,6,7,8,9,1,4,5,6,4,2,4,2,1,4,5,6,4,3,1,3,2,4,5,6,7,5,1,4,3,2]

# Llamada a la función multiplicar
resultado = multAmericanoIterativoEstatico(arreglo1, arreglo2)
print("El resultado de la multiplicación americano iterativa estatica es:", resultado)

# Llamada a la función multiplicar
resultado = multInglesaIterativoEstatico(arreglo1, arreglo2)
print("El resultado de la multiplicación inglesa iterativa estatica es:", resultado)

# Llamada a la función multiplicar
resultado = multAmericanoaRecursivoEstatico(arreglo1, arreglo2)
print("El resultado de la multiplicación americana recursiva estatica es:", resultado)

# Llamada a la función multiplicar
resultado = multInglesaRecursivoEstatico(arreglo1, arreglo2)
print("El resultado de la multiplicación inglesa recursiva estatica es:", resultado)

# Llamada a la función multiplicar
resultado = multAmericanoIterativoDinamico(arreglo1, arreglo2)
print("El resultado de la multiplicación americana iterativa dinamica es:", resultado)

# Llamada a la función multiplicar
resultado = multInglesaIterativoDinamico(arreglo1, arreglo2)
print("El resultado de la multiplicación inglesa iterativa dinamica es:", resultado)

# Llamada a la función multiplicar
resultado = multAmericanoRecursivoDinamico(arreglo1, arreglo2)
print("El resultado de la multiplicación americana recursiva dinamica es:", resultado)

# Llamada a la función multiplicar
resultado = multInglesaRecursivoDinamico(arreglo1, arreglo2)
print("El resultado de la multiplicación inglesa recursiva dinamica es:", resultado)

# Llamada a la función multiplicar
resultado = multHinduIterativoEstatico(arreglo1, arreglo2)
print("El resultado de la multiplicación hindu iterativa estatica es:", resultado)

# Llamada a la función multiplicar
resultado = multDivideYVenceras(arreglo1, arreglo2)
print("El resultado de la multiplicación por divide y venceras es:", resultado)
