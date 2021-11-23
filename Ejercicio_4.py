'''
Escriba un algoritmo que permita saber cuál es el día de la semana, utilizando el siguiente método y después conviértalo a Python:

Conserve las dos últimas cifras del año.

Añada 1/4 de esta cifra, ignorando el resto: división entera.

Añada el día del mes.

Según el mes, añada el valor indicado:

Enero = 1

Febrero = 4

Marzo = 4

Abril = 0

Mayo = 2

Junio = 5

Julio = 0

Agosto = 3

Septiembre = 6

Octubre = 1

Noviembre = 4

Diciembre = 6

Si el año es bisiesto y el mes es enero o febrero, restamos 1.

Según el siglo, añada el valor indicado:

Años 1600 = 6

Años 1700 = 4

Años 1800 = 2

Años 1900 = 0

Años 2000 = 6

Años 2100 = 4

Divida la suma por 7 y guarde el resto: un módulo.

Este resto es el día de la semana buscado.

1 para Domingo

2 para Lunes

3 para Martes

4 para Miércoles

5 para Jueves

6 para Viernes

0 para Sábado
'''

def añadir_mes (mes):
    if mes == 'Enero':
        return 1
    elif  mes == 'Febrero':
        return 4
    elif  mes == 'Marzo':
        return 4
    elif  mes == 'Abril':
        return 0
    elif  mes == 'Mayo':
        return 2
    elif  mes == 'Junio':
        return 5
    elif  mes == 'Julio':
        return 0
    elif  mes == 'Agosto':
        return 3
    elif  mes == 'Septiembre':
        return 6
    elif  mes == 'Octubre':
        return 1
    elif  mes == 'Noviembre':
        return 4
    elif  mes == 'Diciembre':
        return 6

mes = 'Octubre'
mes2 ='Diciembre'
print (añadir_mes(mes))
print(añadir_mes(mes2))