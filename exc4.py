#!/usr/bin/env python
# -*- coding: utf-8 -*-

def geradorDeDicionariosComAsFrequencias(vet):
    tamanho = len(vet)
    dicionario = {}
    i = 0

    for i in range(0, tamanho):
        dicionario[vet[i]] = 0
        for j in range(0, tamanho):
            if (vet[j] == vet[i]):
                dicionario[vet[i]] = dicionario[vet[i]] + 1


    #print dicionario
    return dicionario

def retornarQtdNumsComuns(diciA, diciB):
    tamanhoA = len(diciA)
    tamanhoB = len(diciB)
    diciFinal = {}
    i = 0
    j = 0


    for elementoA in diciA:
        diciFinal[elementoA] = 0
    for elementoB in diciB:
        diciFinal[elementoB] = 0

    for elementoA in diciA:
        for elementoB in diciB:
            if (elementoB == elementoA):
                if (diciB[elementoB] < diciA[elementoA]):
                    diciFinal[elementoB] = diciB[elementoB]
                elif (diciA[elementoA] < diciB[elementoB]):
                    diciFinal[elementoA] = diciA[elementoA]
                elif (diciB[elementoB] == diciA[elementoA]):
                    diciFinal[elementoA] = diciA[elementoA]
    print diciFinal

vetorA = [1, 2, 2, 2, 3, 3, 4]
vetorB = [1, 2, 2, 3, 4, 5]
diciA = geradorDeDicionariosComAsFrequencias(vetorA)
diciB = geradorDeDicionariosComAsFrequencias(vetorB)
retornarQtdNumsComuns(diciA, diciB)
