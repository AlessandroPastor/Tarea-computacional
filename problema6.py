#En un cuadrado cuyo lado es a, se unen los puntos medios de sus 4 lados, formandose otro cuadrado cuyos puntos medios se unen también formando otro cuadrado, y así susesivamente. Calcule la suma de las áreas de todos los cuadrados asi formados.

d1: float
d2: float
AreaRombo: float

#entrada
d1 = float(input("Ingrese diagonal mayor: "))
d2 = float(input("Ingrese diagonal maenor: "))

# proceso
AreaRombo=d1*d2/2

# salida
print(f'El área del rombo es: {AreaRombo}')|
