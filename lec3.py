import pandas as pd
import os
import matplotlib.pyplot as plt
MEDIA_ROOT = os.path.expanduser("~/Python/Buenas practicas de programacion/lec1/")
PATH_CSV = MEDIA_ROOT + 'finanzas2020.csv'


class finanzas:
    """Finanzas.

    Atributos:
    ----------
    serie:
        hace referencia a la serie creada a partir de la funcion csv_file

    Metodos:
    --------
        maximo:
            Escoge el valor maximo entre todas las columnas de la serie
        minimo:
            Escoge el valor minimo entre todas las columnas de la serie
        media:
            Calcula el valor medio de todas las columnasde la serie
        ingresos:
            Calcula la suma de todos los valores positivos de las columnas de la serie
        gastos:
            Calcula la suma de todos los valores negativos de las columnas de la serie
        grafica:
            Crea una grafica en funcion de los meses y sus ingresos

        Ejemplos
        --------
        >>> import finanzas
        >>> import lec3
        >>> import pandas as pd
        >>> import os
        >>> import matplotlib.pyplot as plt
        >>> MEDIA_ROOT = os.path.expanduser("~/Python/Buenas practicas de programacion/lec1/")
        >>> PATH_CSV = MEDIA_ROOT + 'finanzas2020.csv'
        >>> df = pd.read_csv(PATH_CSV, sep="\t")
        >>> serie =  df.sum(axis=0)
        >>> fin = finanzas(serie)
        >>> resultado_maximo = fin.maximo()
        >>> print (resultado_maximo)
        >>> resultado_minimo = fin.minimo()
        >>> print (resultado_minimo)
        >>> resultado_media = fin.media()
        >>> print (resultado_media)
        >>> resultado_ingresos = fin.ingresos()
        >>> print (resultado_ingresos)
        >>> resultado_gastos = fin.gastos()
        >>> print (resultado_gastos)
        >>> resultado_grafica = fin.grafica()
        >>> print (resultado_grafica)
        """

    def __init__(self, serie):
        self.serie = serie

    def maximo(self):
        """
        Escoge el valor maximo entre todas las columnas de la serie
        """
        return self.serie.max()

    def minimo(self):
        """
        Escoge el valor minimo entre todas las columnas de la serie
        """
        return self.serie.min()

    def media(self):
        """
        Calcula el valor medio de todas las columnasde la serie
        """
        return self.serie.mean().round(decimals=2)

    def ingresos(self):
        """
        Calcula la suma de todos los valores positivos de las columnas de la serie
        """
        ingresos = 0
        for keys in self.serie.keys():
            if self.serie[keys] > 0:
                ingresos += self.serie[keys]
        return ingresos

    def gastos(self):
        """
        Calcula la suma de todos los valores negativos de las columnas de la serie
        """
        gastos = 0
        for keys in self.serie.keys():
            if self.serie[keys] < 0:
                gastos += self.serie[keys]
        return gastos

    def grafica(self):
        """
        Crea una grafica en funcion de los meses y sus ingresos
        """
        meses = []
        a = 0
        df = pd.read_csv(PATH_CSV, sep="\t")
        for keys in self.serie.keys():
            a += self.serie[keys]
            meses.append(a)
        grafica = pd.DataFrame(meses, index=df.columns, columns=['Evolucion_Precios'])
        plt.bar(df.columns, grafica['Evolucion_Precios'])
        plt.xlabel('Meses')
        plt.ylabel('Ingresos')
        plt.show()
