#!/usr/bin/env python3
import math

"----------------------------------------------------"

"""
Fonction pour ouvrir un fichier de texte, p.e. un csv. 
"""
def openCSV(csvFile):
    with open(csvFile, 'r') as f:
        aListOfPokemons = []
        for column in f:
            infos = column.split(';')
            infos[-1] = infos[-1].strip() # remove \n at the end of the line
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
    typeIndex = listOfPk[0].index('Legendary')
    legendPokemons = []
    
    for i in range(len(listOfPk)):
        if (listOfPk[i][typeIndex] == 'True'):
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


"----------------------------------------------------"

"""
Fonction pour calculer les stats de Pokemon Go
Noms des variables:
#;Name;Type 1;Type 2;HP base;Attack base;Defense base;Sp. Atk base;Sp. Def base;Speed base;Generation;Legendary
"""
def speedMolt(speedBase):
    return (1+(speedBase-75)/500)

def hpGO (hpBase):
    return (50+1.75*hpBase)

def attackGO (attackBase, attackSp, speedBase):
    return (1/4 * min(attackBase, attackSp) + 7/4 * max(attackBase, attackSp)*speedMolt(speedBase))

def defenseGO(defenseBase, defenseSp, speedBase):
    return (3/4 * min(defenseBase, defenseSp) + 5/4 * max(defenseBase, defenseSp)*speedMolt(speedBase))

def cp(hpGO, attackGO, defenseGO):
    return (math.sqrt(hpGO)*attackGO*math.sqrt(defenseGO)/10)


def pokemonGO(listOfPk):
    indexHP = listOfPk[0].index('HP base')
    indexAb = listOfPk[0].index('Attack base')
    indexDb = listOfPk[0].index('Defense base')
    indexSpA = listOfPk[0].index('Sp. Atk base')
    indexSpD = listOfPk[0].index('Sp. Def base')
    indexSpeed = listOfPk[0].index('Speed base')

    header = ['HP GO', 'Attack GO', 'Defense GO', 'CP\n']
    listOfPk[0].extend(header)

    for i in range(1, len(listOfPk)):
        hpgo = hpGO(int(listOfPk[i][indexHP]))
        attgo = attackGO(int(listOfPk[i][indexAb]), int(listOfPk[i][indexSpA]), int(listOfPk[i][indexSpeed]))
        defgo = defenseGO(int(listOfPk[i][indexDb]), int(listOfPk[i][indexSpD]), int(listOfPk[i][indexSpeed]))
        i_cp = cp(hpgo, attgo, defgo)
        extList = [str(hpgo), str(attgo), str(defgo), str(i_cp)+'\n']
        listOfPk[i].extend(extList)    

    return listOfPk

#print (pokemonGO(pokemonList))

"----------------------------------------------------"
