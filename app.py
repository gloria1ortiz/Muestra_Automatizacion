#app.py - Archivo principal de la aplicación

def suma(numero_a, numero_b):
  """
  Retorna la sma de los números.
  Parámetros:
      numero_a (into o float): primer número
      numero_b (into o float): primer número
 Retorna:
     La suma de ambos valores
  """
  return numero_a + numero_b


def saludo(nombre):
  """Retorna un mensaje de saludo personalizado."""
  return f'Hola,  {nombre}. Bienvenido al mundo de GitHub Actions.'


if_name_=='_main_':
print(saludo('Estudiante'))
print(f'Resultado de 5 + 3 = {suma(5,  3)}')
