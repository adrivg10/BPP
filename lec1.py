import pandas as pd
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import csv


def csv_file(csv_file):
    df = pd.read_csv(csv_file, sep="\t")
    return df.sum(axis=0)


def maximo(dataframe):
    return dataframe.max()


def minimo(dataframe):
    return dataframe.min()


def media(dataframe):
    return dataframe.mean().round(decimals=2)


def ingresos(dataframe):
    ingresos = 0
    for keys in dataframe.keys():
        if dataframe[keys] > 0:
            ingresos += dataframe[keys]
    return ingresos


def gastos(dataframe):
    gastos = 0
    for keys in dataframe.keys():
        if dataframe[keys] < 0:
            gastos += dataframe[keys]
    return gastos


def grafica(dataframe):
    meses = []
    a = 0
    df = pd.read_csv(PATH_CSV, sep="\t")
    for keys in dataframe.keys():
        a += dataframe[keys]
        meses.append(a)
    grafica = pd.DataFrame(meses, index=df.columns, columns=['Evolucion_Precios'])
    plt.bar(df.columns, grafica['Evolucion_Precios'])
    plt.xlabel('Meses')
    plt.ylabel('Ingresos')
    plt.show()


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
            print("xxxxxxxx Resumen mensual xxxxxxxxxxxxx")
            print(csv_file(PATH_CSV), "\n")
            print("¿Qué mes se ha gastado más?")
            print(np.absolute(minimo(csv_file(PATH_CSV))))
            print("¿Qué mes se ha ahorrado más?")
            print(maximo(csv_file(PATH_CSV)))
            print("¿Cuál es la media de gastos al año?")
            print(np.absolute(media(csv_file(PATH_CSV))))
            print("¿Cuál ha sido el gasto total a lo largo del año?")
            print(np.absolute(gastos(csv_file(PATH_CSV))))
            print("¿Cuáles han sido los ingresos totales a lo largo del año?")
            print(ingresos(csv_file(PATH_CSV)))

            grafica(csv_file(PATH_CSV))

        else:
            print("El archivo no cuenta con 12 columnas")
except:
    print("No se ha encontrado el fichero o no puede leerse")
