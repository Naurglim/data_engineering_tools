#DATA
import pokemon_data as poke_data

# 1:
"""
A list of integers that represents each Pokémon's generation has been loaded into your session called generations. 
You'd like to gather the counts of each generation and determine what percentage each generation accounts for out of the total count of integers.
"""
generations = poke_data.generations

# OG LOOP:
# Collect the count of each generation
gen_counts = Counter(generations)

for gen,count in gen_counts.items():
    total_count = len(generations)
    gen_percent = round(count / total_count * 100, 2)
    print(
      'generation {}: count = {:3} percentage = {}'
      .format(gen, count, gen_percent)
    )


#BETTER LOOP:
# Import Counter
from collections import Counter

# Collect the count of each generation
gen_counts = Counter(generations)

# Improve for loop by moving one calculation above the loop
total_count = len(generations)

for gen,count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    print('generation {}: count = {:3} percentage = {}'
          .format(gen, count, gen_percent))


# 2: 
"""
You'd like to gather all the possible pairs of Pokémon types. 
You want to store each of these pairs in an individual list with an enumerated index as the first element of each list. 
This allows you to see the total number of possible pairs and provides an indexed label for each pair.
"""
from itertools import combinations
pokemon_types = poke_data.all_types

# OG Loop:
possible_pairs = [*combinations(pokemon_types, 2)]

enumerated_pairs = []

for i,pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_pair_list = list(enumerated_pair_tuple)
    enumerated_pairs.append(enumerated_pair_list)


#BETTER LOOP:
# Collect all possible pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]

# Create an empty list called enumerated_tuples
enumerated_tuples = []

# Append each enumerated_pair_tuple to the empty list above
for i,pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_tuples.append(enumerated_pair_tuple)

# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerated_tuples)]
print(enumerated_pairs)


# 3:
"""
A list of 720 Pokémon has been loaded into your session as names. 
Each Pokémon's corresponding Health Points is stored in a NumPy array called hps. 
You want to analyze the Health Points using the z-score to see how many standard deviations each Pokémon's HP is from the mean of all HPs.
"""
import numpy as np

# Data
names = poke_data.names
hps = poke_data.hp

#OG Loop
poke_zscores = []

for name,hp in zip(names, hps):
    hp_avg = hps.mean()
    hp_std = hps.std()
    z_score = (hp - hp_avg)/hp_std
    poke_zscores.append((name, hp, z_score))

highest_hp_pokemon = []

for name,hp,zscore in poke_zscores:
    if zscore > 2:
        highest_hp_pokemon.append((name, hp, zscore))


# BETTER
# Calculate the total HP avg and total HP standard deviation
hp_avg = np.mean(hps)
hp_std = np.std(hps)

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

# Use list comprehension with the same logic as the highest_hp_pokemon code block
highest_hp_pokemon2 = [(name, hp, zscore) for name,hp,zscore in poke_zscores2 if zscore > 2]
print(*highest_hp_pokemon2, sep='\n')