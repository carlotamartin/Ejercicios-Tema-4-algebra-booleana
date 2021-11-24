'''
Un ascensor se controla como sigue:

Un interruptor de fin de viaje a cambia cuando la cabina está abajo.
'''
def esta_abajo(a):
    a = True

def esta_arriba(b):
    b = False

def subiendo(c):
    c = True

def bajando(c):
    c = False

def main():
    a = False
    b = False
    c=0


'''

Un interruptor de fin de viaje b cambia cuando la cabina está arriba.

Un interruptor c permite subir o bajar.

Cuando el ascensor está totalmente abajo, solo a cambia. Si c cambia (posición 1), sube.

Cuando llega arriba, b cambia y el ascensor se detiene.

Si se cierra c (posición 0), el ascensor baja hasta abajo.

Cuando llega abajo, a cambia y el ascensor se detiene.

Si c se cierra cuando está subiendo, el ascensor vuelve a bajar.

Crear la tabla de verdad con dos resultados: M para subir y D para bajar. 

Deducir las dos expresiones buleanas asociadas y dar un corto ejemplo de utilización en una estructura Si.


'''
