
Dataframes:
    loc: filter in columns or lines. [:] se usa para señalar todo el rango en alguna de las dimensiones.
        data_frame.loc[data_frame["name"] == "Apparel", :]  # filtra los registros con name = "Apparel"
        data_frame.loc[:, ["name", "num_firms"]]  # filtra y devuelve las columnas "name" y "num_firms" nada más. 
    to_csv(path): guarda el data frame en un archivo de texto plano. Puede recibir varios parámetros adicionales.
    to_json(), to_excel(), to_sql() también existen.
    