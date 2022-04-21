#Calcule la suma de numeros los cubos de los n primeros numeros.

n: int
s: int

#entrada
n=int(input("Ingrese número de términos: "))

#proceso
s=n*n*(n+1)*(n+1)/4

#salida
print(f'La suma de los cubos de los primeros {n} primeros términos es: {s}')
