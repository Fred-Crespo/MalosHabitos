# Función para calcular
def calcular(primerValor, segundoValor, tercerValor):
    resultado = primerValor * segundoValor + tercerValor
    return resultado

# Función principal
def principal():
    # Definimos los números
    primerNumero = 5
    segundoNumero = 3
    tercerNumero = 7
    # Llamamos a la función calcular y guardamos el resultado
    resultado = calcular(primerNumero, segundoNumero, tercerNumero)
    # Imprimimos el resultado
    print("El resultado es:", resultado)

# Llamamos a la función principal para iniciar el cálculo
principal()