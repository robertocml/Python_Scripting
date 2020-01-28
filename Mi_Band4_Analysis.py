import pandas as pd

'''
    Analisis de los datos exportados de la Mi band 4
    Nota: Este es solo un pequeño dataset (2 meses).. del 
    dataset completo
'''

# Mostramos todos los rows
pd.set_option('display.max_rows', None)
# Cargamos del dataset
df = pd.read_csv('Data_Miband.csv')

# Eliminamos una columa añadida por error en la exportacion del la data
df = df.drop(['Unnamed: 5'], axis=1)

# Limpiamos la fecha del dataset
df['Creation Date'] = df['Creation Date'].str[:-5]
df['Start Date'] = df['Start Date'].str[:-5]
df['End Date'] = df['End Date'].str[:-5]

# Renombramos las columnas
df.rename(columns={'Unit': 'Unidad', 'Creation Date': 'FechaCreacion', 'Start Date': 'FechaInicio',
                   'End Date': 'FechaFin', 'Value': 'Valor'}, inplace=True)

# convertimos las fechas en formato dd/mm/aaaa a objetos tipo datatime de pandas
df['FechaCreacion'] = pd.to_datetime(df.FechaCreacion)
df['FechaInicio'] = pd.to_datetime(df.FechaInicio)
df['FechaFin'] = pd.to_datetime(df.FechaFin)


# -------  Empezamos con el Analisis

# Primero calculamos la cantidad de pasos totales por fecha..
df_Results = pd.DataFrame(columns=['Fecha', 'PasosTotales'])

df_Results = df.groupby(['FechaFin']).sum()

# ....
print(df_Results.columns)
