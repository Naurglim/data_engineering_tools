# pip install line_profiler
# cargo en memoria las funciones y variables:
"""
import hero_funcs

%load_ext line_profiler
%lprun -f convert_units convert_units(heroes, hts, wts)

# Comparo con la siguiente funcion:
%load_ext line_profiler
%lprun -f convert_units_broadcast convert_units_broadcast(heroes, hts, wts)

"""

# Tiene decoradores. Usar eso en vez!!!