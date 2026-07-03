from typing import Callable
from decimal import Decimal, localcontext
from matplotlib import pyplot

def newton_raphon(f: Callable, d: Callable, a: float, xtol=0.00001, maxiter=4):
    """
    :param f: La función cuya raíz se busca.
    :param d: Derivada de la función a la que cuya raíz se busca.
    :param x: conjetura inicial.
    :param xtol: Tolerancia de error en la raíz.
    :param maxiter: Número máximo de iteraciones permitidas.
    
    """
    with localcontext() as ctx:
        ctx.prec = 100  # 100 digitos de precision
        
    c = Decimal(0)

    nit = 0
    while nit <= maxiter:
        nit += 1
        c = Decimal(a) - (f(Decimal(a))/d(Decimal(a)))
        print(c)
        a_viejo = a
        if abs(((c-Decimal(a))/c)) <= xtol:
            return "error: ",abs((c-Decimal(a))/c), " Iteraciones: ", nit
        else:
            a = c
        
    
    return ("El número máximo de iteraciones permitidas ha sido excedido." , "Iteraciones:", nit , "error:", abs((c - Decimal(a_viejo))/c))

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



def fx(x):
    return x**3 - 2*x**2 - 4*x + 5

def dy(x):
    return 3*x**3-4*x-4


PuntoPartida = 3

resultado = newton_raphon(fx,dy,PuntoPartida)
print(resultado)
graficar_funcion(fx)