
# %timeit se corre en ipython (linea de comando) y devuelve datos del tiempo de ejecución del código que se le pasa como parámetro:

"""
%timeit n2 r5 formal_list = list()
%timeit n2 r5 literal_list = []


%%timeit
hero_wts_lbs = []
for wt in wts:
    hero_wts_lbs.append(wt * 2.20462)

%%timeit
wts_np = np.array(wts)
hero_wts_lbs_np = wts_np * 2.20462
"""