import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import csv


def ejercicio(path_archivo):

    df = pd.read_csv(PATH_CSV, sep="\t")
    '''for column in df.columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    df = df.replace(np.nan, 0, regex=True)
    for column in df.columns:
        df[column] = df[column].astype(int)'''
    resumen = df.sum(axis=0)
    print("xxxxxxxx Resumen mensual xxxxxxxxxxxxx")
    print(resumen, "\n")
    print("¿Qué mes se ha gastado más?")
    print(np.absolute(resumen.min()))
    print("¿Qué mes se ha ahorrado más?")
    print(resumen.max())
    print("¿Cuál es la media de gastos al año?")
    print(np.absolute(resumen.mean().round(decimals=2)))
    print("¿Cuál ha sido el gasto total a lo largo del año?")
    ingresos = 0
    gastos = 0
    for keys in resumen.keys(): # Se crea un bucle para recorrer todos los meses
        if resumen[keys] < 0:
            gastos += resumen[keys] # si para ese mes el numero es negativo se considera gasto
        else:
            ingresos += resumen[keys] # si para ese mes el numero es positivo/0 se considera ingreso
    print(np.absolute(gastos))
    print("¿Cuáles han sido los ingresos totales a lo largo del año?")
    print(ingresos)
    print("Realice una gráfica de la evolución de ingresos a lo largo del año")
    meses = [] # Creamos una lista en la que se van a ir guardando como evolucionan los ingresos a lo largo del año
    a = 0
    for keys in resumen.keys():
        a += resumen[keys] # Para saber el computo global vamos a ir sumando al mes anterior el propio (en el caso de que sea negativo lo restaremos)
        meses.append(a) # Vamos añadiendo el computo global de cada mes en una lista
    grafica = pd.DataFrame(meses, index=df.columns, columns=['Evolucion_Precios']) #Transformamos la lista en un dataframe
    plt.bar(df.columns, grafica['Evolucion_Precios']) # Grafica tipo bar
    plt.xlabel('Meses') # nombre eje x
    plt.ylabel('Ingresos') # nombre eje y
    plt.show() # Mostramos la imagen creada


MEDIA_ROOT = os.path.expanduser("~/Python/Buenas practicas de programacion/lec1/")
PATH_CSV = MEDIA_ROOT + 'finanzas2020.csv'
fieldnames = []
filas = []
filas2 = []
try:
    with open(PATH_CSV) as File:
        reader = csv.reader(File, delimiter='\t')
        fieldnames = next(reader)
        print("El archivo se ha leido correctamente")
        if len(fieldnames) == 12:
            print(f"El archivo tiene {len(fieldnames)} columnas\n")
            for row in reader:
                for value in row:
                    if type(value) == str:
                        try:
                            value = float(value)
                        except:
                            value = 0
                    filas.append(value)
                filas2.append(filas)
                filas = []

            with open(PATH_CSV, 'w', newline='') as File:
                writer = csv.writer(File, delimiter='\t')
                writer.writerow(fieldnames)
                for row in filas2:
                    writer.writerow(row)

            ejercicio(PATH_CSV)

        else:
            print("El archivo no cuenta con 12 columnas")
except:
    print("No se ha encontrado el fichero o no puede leerse")