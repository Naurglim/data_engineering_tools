import recordlinkage
import pandas as pd
import recordlinkage.compare


restaurants = pd.DataFrame({'rest_name': ['Panga','Penga','Pinga','Ponga','Punga'],
                            'city': ['Buenos Aires', 'Córdoba', 'Sevilla', 'Mendoza', 'Tenerife'],
                            'cuisine_type': ['italian','italian','asian','american','american']})

restaurants_bis = pd.DataFrame({'rest_name': ['Pangea','Renga','Linga','Ponga','Puunga', 'Stone', 'Parchment', 'Shears', 'Dragon', 'Wizard'],
                                'city': ['Buenos Aires', 'Córdoba', 'Sevilla', 'Mendoza', 'Tenerife', 'Buenos Aires', 'Sevilla', 'Sevilla', 'Tenerife', 'Mendoza'],
                                'cuisine_type': ['italian','italian','asian','american','american','italian','italian','asian','american','american']})

# Create an indexer and object and find possible pairs
indexer = recordlinkage.Index()

# Block pairing on cuisine_type
indexer.block('cuisine_type')

# Generate pairs
pairs = indexer.index(restaurants, restaurants_bis)

# Create a comparison object
comp_cl = recordlinkage.Compare()

# Find exact matches on city, cuisine_types 
comp_cl.exact('city', 'city', label='city')
comp_cl.exact('cuisine_type', 'cuisine_type', label = 'cuisine_type')

# Find similar matches of rest_name
comp_cl.string('rest_name', 'rest_name', label='name', threshold = 0.8) 

# Get potential matches and print
potential_matches = comp_cl.compute(pairs, restaurants, restaurants_bis)

# DataFrame Linking:

matches = potential_matches[potential_matches.sum(axis = 1) >= 3]

duplicate_rows = matches.index.get_level_values(1)

# Duplicate Records
duplicate_restaurants = restaurants_bis[restaurants_bis.index.isin(duplicate_rows)]
print(duplicate_restaurants)

# New Records
new_restaurants = restaurants_bis[~restaurants_bis.index.isin(duplicate_rows)]

# Link Dataframes:
restaurants_full = pd.concat([restaurants, new_restaurants], ignore_index=True)
print(restaurants_full)