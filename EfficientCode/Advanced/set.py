list_a = ['Bulbasaur','Squirtle','Charmander']
list_b = ['Caterpie','Pidgey','Squirtle']

set_a = set(list_a)
set_b = set(list_b)

# Combinations
in_both = set_a.intersection(set_b)
print(in_both)  # Exists in both sets

exclusives_a = set_a.difference(set_b)
print(exclusives_a)  # Exclusive to set A. Does not appear in set b.

uniques = set_a.symmetric_difference(set_b)
print(uniques)  # Unique pokemon. Appear only once across sets. 

full_set = set_a.union(set_b)
print(full_set)  # combined set of all pokemon just once.


# Membership
exists = ('Squirtle' in set_a)
print(exists)  # exists in set_a


ash_pokedex   = ['Pikachu', 'Bulbasaur', 'Koffing', 'Spearow', 'Vulpix', 'Wigglytuff', 'Zubat', 'Rattata', 'Psyduck', 'Squirtle'] 
misty_pokedex = ['Krabby', 'Horsea', 'Slowbro', 'Tentacool', 'Vaporeon', 'Magikarp', 'Poliwag', 'Starmie', 'Psyduck', 'Squirtle']
brock_pokedex = ['Onix', 'Geodude', 'Zubat', 'Golem', 'Vulpix', 'Tauros', 'Kabutops', 'Omastar', 'Machop', 'Dugtrio']

# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
print(both)

# Find the Pokémon that Ash has and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only)

# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set)


