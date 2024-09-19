#  Zip: combina colecciones -> objeto que debe ser unpacked (*) en una coleccion de tuples
names = ['Bulbasaur', 'Charmander', 'Squirtle']
hps = [45, 39, 44]
combined_zip = zip(names, hps)
print(type(combined_zip))
combined_zip_list = [*combined_zip]
print(combined_zip_list)


# Counter: cuenta objetos en una coleccion -> diccionario
poke_types = ['Grass', 'Dark', 'Fire', 'Fire', 'Fire', 'Grass']
from collections import Counter
type_counts = Counter(poke_types)
print(type_counts)


# Combination: 
poke_types = ['Grass', 'Dark', 'Bug', 'Fire', 'Ghost', 'Water']
from itertools import combinations
combos_obj = combinations(poke_types, 2)
print(type(combos_obj))
combos = [*combos_obj]
print(combos)

