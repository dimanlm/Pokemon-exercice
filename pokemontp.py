#!/usr/bin/env python3
import math

"----------------------------------------------------"

"""
Function to open a text file, csv file in our case
* Input: name of the csv file
* Output: a list of pokemon data
"""
def openCSV(csvFile):
    with open(csvFile, 'r') as f:
        listOfPokemons = []
        for column in f:
            infos = column.split(';')
            infos[-1] = infos[-1].strip() # remove \n at the end of the line
            listOfPokemons.append((infos[0:]))
    return listOfPokemons

"----------------------------------------------------"

"""
Function to find all the Grass pokemons
* Input: a list with pokemon data
* Output: a list of grass pokemons with their data
Header (list[0]):
#;Name;Type 1;Type 2;HP base;Attack base;Defense base;Sp. Atk base;Sp. Def base;Speed base;Generation;Legendary
"""
def lookingForGrass(listOfPokemons):
    typeIndex = listOfPokemons[0].index('Type 1')
    grassPokemons = []
    
    for i in range(len(listOfPokemons)):
        if (listOfPokemons[i][typeIndex] == 'Grass') or (listOfPokemons[i][typeIndex+1] == 'Grass'):
            grassPokemons.append(listOfPokemons[i])
    
    return grassPokemons

"----------------------------------------------------"

"""
Function to find all the 'Legendary' pokemons
* Input: a list with pokemon data
* Output: a list of legendary pokemons with their data
Header (list[0]):
#;Name;Type 1;Type 2;HP base;Attack base;Defense base;Sp. Atk base;Sp. Def base;Speed base;Generation;Legendary
"""
def lookingForLegend(listOfPokemons):
    typeIndex = listOfPokemons[0].index('Legendary')
    legendPokemons = []
    
    for i in range(len(listOfPokemons)):
        if (listOfPokemons[i][typeIndex] == 'True'):
            legendPokemons.append(listOfPokemons[i])
    
    return legendPokemons

"----------------------------------------------------"

"""
Function to find the strongest pokemon.
To do so, we sum all the numeric stats (HP base:Speed base)
* Input: a list with pokemon data
* Output: the name and the power of the strongest pokemon
Header (listOfPokemons[0]):
#;Name;Type 1;Type 2;HP base;Attack base;Defense base;Sp. Atk base;Sp. Def base;Speed base;Generation;Legendary
"""
def highestStats(listOfPokemons):
    indexNom = listOfPokemons[0].index('Name')
    indexStat1 = listOfPokemons[0].index('HP base')
    newlistOfPokemons = []
    strongestPk = ["", 0]
    
    for i in range(1,len(listOfPokemons)):
        sumOfStats = 0
        for j in range(0,6):
            sumOfStats = sumOfStats + int(listOfPokemons[i][indexStat1+j])
        newlistOfPokemons.append([listOfPokemons[i][indexNom],sumOfStats])
        if newlistOfPokemons[i-1][1] > strongestPk[1]:
            strongestPk = newlistOfPokemons[i-1]
    
    return strongestPk

"----------------------------------------------------"

# Pokemon Go data calculations.
# All inputs are values from the initial list of data imported from 'Pokemon.csv'
"""
* Input: Speed base
* Output: speedMolt
"""
def speedMolt(speedBase):
    return (1+(speedBase-75)/500)

"""
* Input: HP base
* Output: HP Go
"""
def hpGO (hpBase):
    return (50+1.75*hpBase)

"""
* Input: Attack base, Sp. Atk base, Speed base
* Output: attackGo
"""
def attackGO (attackBase, attackSp, speedBase):
    return (1/4 * min(attackBase, attackSp) + 7/4 * max(attackBase, attackSp)*speedMolt(speedBase))

"""
* Input: Defense base, Sp. Def base, Speed base
* Output: defenseGo
"""
def defenseGO(defenseBase, defenseSp, speedBase):
    return (3/4 * min(defenseBase, defenseSp) + 5/4 * max(defenseBase, defenseSp)*speedMolt(speedBase))

"""
* Input: HP Go, attackGo, defenseGo 
* Output: CP
"""
def cp(hpGO, attackGO, defenseGO):
    return (math.sqrt(hpGO)*attackGO*math.sqrt(defenseGO)/10)

"""
Function to calculate the stats for Pokemon Go
* Input: a list with pokemon data
* Output: updated list, that includes PokemonGo stats
Header (list[0]):
#;Name;Type 1;Type 2;HP base;Attack base;Defense base;Sp. Atk base;Sp. Def base;Speed base;Generation;Legendary
"""
def pokemonGO(listOfPokemons):
    # find the index of the needed data
    indexHP = listOfPokemons[0].index('HP base')
    indexAb = listOfPokemons[0].index('Attack base')
    indexDb = listOfPokemons[0].index('Defense base')
    indexSpA = listOfPokemons[0].index('Sp. Atk base')
    indexSpD = listOfPokemons[0].index('Sp. Def base')
    indexSpeed = listOfPokemons[0].index('Speed base')

    header = ['HP GO', 'Attack GO', 'Defense GO', 'CP\n']
    listOfPokemons[0].extend(header)

    for i in range(1, len(listOfPokemons)):
        # round() used to set a maximum number of decimals, 2 in our case
        hpgo = round(hpGO(int(listOfPokemons[i][indexHP])),2)
        attgo = round(attackGO(int(listOfPokemons[i][indexAb]), int(listOfPokemons[i][indexSpA]), int(listOfPokemons[i][indexSpeed])),2)
        defgo = round(defenseGO(int(listOfPokemons[i][indexDb]), int(listOfPokemons[i][indexSpD]), int(listOfPokemons[i][indexSpeed])),2)
        i_cp = round(cp(hpgo, attgo, defgo),2)
        # save the calculated stats in a new list
        extList = [str(hpgo), str(attgo), str(defgo), str(i_cp)+'\n']
        # add the new stats to the initial list
        listOfPokemons[i].extend(extList)    

    return listOfPokemons

"----------------------------------------------------"

"""
Function to create a new csv file and write in it the updated list.
"""
def writeCSV(listOfPokemons):
    with open('NewPokemon.csv', 'w') as out_f:
        for line in listOfPokemons:
            out_f.write(";".join(line))
    print ("\nUpdated data have been saved in 'NewPokemon.csv'.\n")
    return 0

"----------------------------------------------------"


# Open, read and save the data from 'Pokemon.csv' in a list
pokemonList = (openCSV('Pokemon.csv'))
print ("Q1. There are", len(pokemonList)-1, "saved pokemons")

# Find all grass type pokemons
grassPokemons = lookingForGrass(pokemonList)
print("Q2.1. Il y a",len(grassPokemons), "pokemons de type plante")

# Find all the legendary pokemons
legendPokemons = lookingForLegend(pokemonList)
print("Q2.2. Il y a",len(legendPokemons), "pokemons legendaires")

# Get the strongest pokemon
print("Q3. Le pokemon le plus puissant est", highestStats(pokemonList))

# Calculate the new stats and update the initial list: pokemonGO(list)
# Write everything in a new file called 'NewPokemon.csv' writeCSV(list)
writeCSV(pokemonGO(pokemonList))