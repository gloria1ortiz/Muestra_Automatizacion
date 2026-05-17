# test_app.py - Pruebas unitarias con pytest
# Para ejecutar:  pytest  test_app.py  -v

from app import suma, saludo


def test_suma_numeros_positivos ():
    #  Arrange:  preparamos los datos
    a,   b = 5, 3
    # Act:  ejecutamos la función
    resultado = suma(a,  b)
    # Assert:  verificamos el resultado
    assert resultado == 8, f'Se esperaba  8,  se obtuvo {resultado}'


def test_suma_numeros_negatios():
   assert  suma(-2,  -3) ==  -5


def test_suma_cero ():
   assert  suma(0,  5) ==  5


def test_saludo_contiene_nombre():
   resultado = saludo ('Maria')
   assert 'Maria' in resultado, ' El saludo debe contener el nombre'


def test_saludo_es_cadena():
   assert isinstance (saludo('Carlos'), str)
