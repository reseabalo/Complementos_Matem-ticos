from typing import Callable, Tuple
from matplotlib import pyplot

def bisection(f: Callable, a: float, b: float, xtol=0.01, maxiter=3) -> Tuple[float, int]:
    """
    Encuentra una raíz de la función f en el intervalo [a, b] utilizando el método de la bisección.

    :param f: La función cuya raíz se busca.
    :param a: Extremo izquierdo del intervalo.
    :param b: Extremo derecho del intervalo.
    :param xtol: Tolerancia de error en la raíz (diferencia mínima entre a y b).
    :param maxiter: Número máximo de iteraciones permitidas.
    :return: Una tupla que contiene la aproximación de la raíz y el número de iteraciones realizadas.
    :raise ValueError: Si f(a) y f(b) tienen el mismo signo, lo que significa que no hay una raíz en el intervalo.
    :return al final: Si se excede el número máximo de iteraciones permitidas.
    """
    
    if f(b) * f(a) > 0:
        raise ValueError('No existe raíz en el intervalo dado')

    nit = 0
    while nit <= maxiter:
        nit += 1
        c = (a + b) / 2
        a_viejo = a
        if abs((((c - a)/c)*100)) <= xtol:
            return abs((((c - a)/c)*100)), nit
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return ("El número máximo de iteraciones permitidas ha sido excedido." , "Iteraciones:", nit , "error:", abs((((c - a_viejo)/c)*100)))

def fx(x):
    return x**3- 2*x**2-4*x+5

def graficar_funcion(funcion: callable):
    
    # Valores del eje X que toma el gráfico.
    x = range(-10, 15)
    
    # Graficar funcion.
    pyplot.plot(x, [funcion(i) for i in x])
    
    # Establecer el color de los ejes.
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    
    # Limitar los valores de los ejes.
    pyplot.xlim(-10, 10)
    pyplot.ylim(-10, 10)
    
    
    
    # Mostrarlo.
    pyplot.show()
    
    
CotaInferior = 2
CotaSuperior = 3


#graficar_funcion(fx)

resultado = bisection(fx,CotaInferior,CotaSuperior)
print(resultado)
