"""
Aquí se ejecutarán las iteraciones, propongo cada un milisegundo, se tienen una velocidad actual, 
posición actual, dirección_actual, momento actual, masa y sumatoria de fuerzas actual.
En base a los datos iniciales se ejecuta el movimiento del cohete y luego se realiza 
la sumatoria de fuerzas, para calcular las nuevas, velocidad, posición, dirección, momento, 
masa y sumatoria de fuerzas.
"""
import numpy as np


class motor:
    empuje = 0 # Empuje en Newtons
    consumo_combustible = 0 # Consumo es masa en kg
    

class generic_rocket:
    state = True # el cohete aun no se autodestrulle o choca
    
    position = np.array([0.0, 0.0, 0.0]) # Posición del cohete en metros, respecto al punto de despegue
    velocity = np.array([0.0, 0.0, 0.0]) # Velocidad del cohete en m/s 
    center = np.array([0.0, 0.0, 0.0]) # Posición relativa en metros, respecto al punto cero del cohete
    orientation = np.array([0.0, 0.0, 0.0]) # Dirección del cohete, vector sin unidades (la suma de los 3 ejes es 0)
    weigth = 0.0 # Peso en kg del cohete sin el combustible
    height = 0.0 # Altura en metros del cohete

    fuel_center = np.array([0.0, 0.0, 0.0]) # Posición relativa en metros, respecto al punto cero del cohete
    fuel_weigth = 0.0


rocket = generic_rocket()

i = 1
while i < 6:
  print(i)
  i += 1


