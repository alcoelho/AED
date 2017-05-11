#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

    Escrever um algoritmo para calcular, de forma exata, a potência de 2. O algo-
    ritmo deve considerar até 2^1000 e, portanto, usar a representação de números
    grandes dada em sala.

'''

def calculadoraDeDoisElevadoAQualquerNumeroAteMilEmNumerosGrandes(numero):
    doisElevadoAoNumero = 2 ** numero

    return conversorDeNumeroPequenoParaNumeroGrande(doisElevadoAoNumero)

def conversorDeNumeroPequenoParaNumeroGrande(numero):

    numeroConvertidoParaString = str(numero)
    tamanhoDoNumero = len(numeroConvertidoParaString)
    vetorDoNumeroGrande = [0]*(tamanhoDoNumero+1)

    if (numero > 0):
        vetorDoNumeroGrande[0] = 1
    else:
        vetorDoNumeroGrande[0] = -1

    for i in range(1, tamanhoDoNumero+1):
        vetorDoNumeroGrande[i] = int(numeroConvertidoParaString[i-1])

    return vetorDoNumeroGrande


for i in range(0, 1001):
    print calculadoraDeDoisElevadoAQualquerNumeroAteMilEmNumerosGrandes(i)
