#!/usr/bin/env python3
import csv

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
print ("Q1. There are", len(pokemonList)-1, "saved pokemons")
#print(pokemonList[1])
#index = pokemonList[0].index('Name')

"----------------------------------------------------"

"""
Fonction pour trouver des pokemons de type 'Plante'
Noms des variables:
#;Name;Type 1;Type 2;HP base;Attack base;Defense base;Sp. Atk base;Sp. Def base;Speed base;Generation;Legendary
"""
def lookingForGrass(listOfPk):
    typeIndex = listOfPk[0].index('Type 1')
    grassPokemons = []
    
    for i in range(len(listOfPk)):
        if (listOfPk[i][typeIndex] == 'Grass') or (listOfPk[i][typeIndex+1] == 'Grass'):
            grassPokemons.append(listOfPk[i])
    
    return grassPokemons

grassPokemons = lookingForGrass(pokemonList)
print("Q2.1. Il y a",len(grassPokemons), "pokemons de type plante")

"----------------------------------------------------"

"""
Fonction pour trouver des pokemons 'legendaires'
Noms des variables:
#;Name;Type 1;Type 2;HP base;Attack base;Defense base;Sp. Atk base;Sp. Def base;Speed base;Generation;Legendary
"""
def lookingForLegend(listOfPk):
    typeIndex = listOfPk[0].index('Legendary\n')
    legendPokemons = []
    
    for i in range(len(listOfPk)):
        if (listOfPk[i][typeIndex] == 'True\n'):
            legendPokemons.append(listOfPk[i])
    
    return legendPokemons

legendPokemons = lookingForLegend(pokemonList)
print("Q2.2. Il y a",len(legendPokemons), "pokemons legendaires")

"----------------------------------------------------"

"""
Fonction pour trouver le pokemon le plus puissant
Il y a 6 stats à sommer. Noms des variables:
#;Name;Type 1;Type 2;HP base;Attack base;Defense base;Sp. Atk base;Sp. Def base;Speed base;Generation;Legendary
"""
def highestStats(listOfPk):
    indexNom = listOfPk[0].index('Name')
    indexStat1 = listOfPk[0].index('HP base')
    newListOfPk = []
    strongestPk = ["", 0]
    
    for i in range(1,len(listOfPk)):
        sumOfStats = 0
        for j in range(0,6):
            sumOfStats = sumOfStats + int(listOfPk[i][indexStat1+j])
        newListOfPk.append([listOfPk[i][indexNom],sumOfStats])
        if newListOfPk[i-1][1] > strongestPk[1]:
            strongestPk = newListOfPk[i-1]
    
    return strongestPk

print("Q3. Le pokemon le plus puissant est", highestStats(pokemonList))
