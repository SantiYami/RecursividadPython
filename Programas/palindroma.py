# -*- coding: utf-8 -*-
#Los subconjuntos de cadenas pueden ser tomados usando el operador de corte ([] y [:])
#con índices comenzando en 0 en el comienzo de la cadena y trabajando su camino de -1 al final.
def palindroma(cadena):
    if len(cadena) < 2:
        return 'Es palindroma '
    if cadena[0] != cadena[-1]:
        return 'No es palindroma '
    return palindroma(cadena[1:-1])

print palindroma(raw_input("Escriba una palabra: "))