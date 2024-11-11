Pandas
Dataframes: 
    Are two dimensional: columns and rows
    Have Indexes

read_csv() reads all flat files.
    sep: separador
    nrows: cant de lineas
    skiprows: cant de lineas a saltear
    header= None: especifica que no hay header asi que no debe tomar los valores de la primer línea como nombre de columnas
    names: list con nombre de las columnas. Debe tener un nombre para cada columna.
    dtype: dictionary con nombre: typo. Ej: dtype = {"zipcode": str}. Los tipos que no se explicitan, los asume. 
    na_values: datos que deberían considerarse como nulos. Acepta un valor, una lista o un diccionario. Ej na_values = {"zipcode": 0}
    error_bad_lines = False : saltea líneas que no puede parsear (más columnas de la esperadas, por ej)
    warn_bad_lines = True: avisa cuando saltea líneas (qué pasa si no se usa con error_bad_lines??)
