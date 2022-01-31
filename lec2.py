import pytest
import pandas as pd
import newlec1
import os
import numpy as np

MEDIA_ROOT = os.path.expanduser("~/Python/Buenas practicas de programacion/lec2/")
PATH_CSV = MEDIA_ROOT + 'test.csv'


def test_csv_file():

    nombres = ['Carlos', 'David', 'Maria', 'Marta']
    resumen = np.array([-58, 107, 15, 10])
    resultado = pd.Series(resumen, index=nombres, dtype='Int64')
    assert (resultado == newlec1.csv_file(PATH_CSV)).all()


def test_maximo():
    resultado = 107
    assert resultado == newlec1.maximo(newlec1.csv_file(PATH_CSV))


def test_minimo():
    resultado = -58
    assert resultado == newlec1.minimo(newlec1.csv_file(PATH_CSV))


def test_media():
    resultado = 18.50
    assert resultado == newlec1.media(newlec1.csv_file(PATH_CSV))


def test_ingresos():
    resultado = 132
    assert resultado == newlec1.ingresos(newlec1.csv_file(PATH_CSV))


def test_gastos():
    resultado = -58
    assert resultado == newlec1.gastos(newlec1.csv_file(PATH_CSV))
