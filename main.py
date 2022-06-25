file = open('mi_primer_archivo.txt', 'w')
file.write('¡He creado mi primer archivo!\n')
file.close()

file = open('mi_primer_archivo.txt', 'r+')
file.readline()
file.write('Esta es la segunda vez que escribo.\n')

file.seek(0)
print(file.read())
file.close()

from pickle import *

class Vehiculo:

    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas

    def __str__(self):
        return self.color + " " + self.puertas


corsa = Vehiculo("Azul", "4")
print(corsa)

file = open('vehiculo_objeto', 'w+b')

dump(corsa, file)

file.seek(0)
nuevo_corsa = load(file)

print(nuevo_corsa)
file.close()