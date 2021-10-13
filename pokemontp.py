#!/usr/bin/env python3


"----------------------------------------------------"

"""
Fonction pour ouvrir un fichier de texte, p.e. un csv. 
"""
def openCSV(csvFile):
    with open(csvFile, 'r') as f:
        aListOfPokemons = []
        for column in f:
            infos = column.split(';')
            aListOfPokemons.append((infos[0:]))
    return aListOfPokemons

pokemonList = (openCSV('Pokemon.csv'))
#print(pokemonList[0])
#index = pokemonList[0].index('#')

"----------------------------------------------------"

