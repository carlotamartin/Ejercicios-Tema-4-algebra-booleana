'''
Escriba un algoritmo que permita saber cuál es el día de la semana, utilizando el siguiente método y después conviértalo a Python:

Conserve las dos últimas cifras del año.

Añada 1/4 de esta cifra, ignorando el resto: división entera.

Añada el día del mes.

Según el mes, añada el valor indicado:
Enero = 1 Febrero = 4 Marzo = 4 Abril = 0 Mayo = 2 Junio = 5 Julio = 0 Agosto = 3 Septiembre = 6 Octubre = 1 Noviembre = 4 Diciembre = 6

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
def main ():
    try:
        print('El día tiene que ser un número entero entre el 1 y el 31.')
        print('El mes tiene que ser una cadena de texto , donde tiene la primera letra tiene que ser en mayúsculas ')
        print ('El año tiene que estar entre el 1600 y el 2200')
        #Suponemos que tenemos que pedir por teclado el día, mes y año. Lanzamos una excepción si
        dia = int(input('Escribe el día: '))
        while dia <=1 and dia>=31:
            dia = int(input('Escribe el día: '))
        mes= input('Escriba el mes: ')
        año = int(input('Escriba el año: '))
        while año <=1600 and año>=2200:
            año = int(input('Escriba el año: '))
        #Conserve las dos últimas cifras del año.
        num = año%2
        #Añada 1/4 de esta cifra, ignorando el resto: división entera.
        num = num//4
        #Añada el día del mes.
        num += añadir_mes(mes)
        #Si el año es bisiesto y el mes es enero o febrero, restamos 1.
        if is_leap(año)== True or mes=='Enero' or mes == 'Febrero':
            num-=1
        #Según el siglo, añada el valor indicado:
        num += añadir_año(año)
        #Divida la suma por 7 y guarde el resto: un módulo.
        num = num%7
        dia_(num)
    except TypeError:
        print ('Algo fue mal')


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


#Función para saber si es bisiesto
def is_leap(year):
    leap = False
    if(((year % 4) ==0) or ((year% 100) !=0) or ((year% 400) ==0)):
        leap=True
# Write your logic here
    return leap

#función para el año
def añadir_año (año):
    if año >=1600 and año<1700:
        return 6;
    elif año >=1700 and año<1800:
        return 4;
    elif año >=1800 and año<1900:
        return 2;
    elif año >=1900 and año<2200:
        return 0;
    elif año >=2000 and año<2100:
        return 6;
    elif año >=2100 and año<2200:
        return 4;


#resultado
def dia_ (numero):
    if numero == 1:
        return print('El dia es el domingo')
    elif numero ==2:
        return print ('El día es el lunes')
    elif numero ==3:
        return print ('El día es el martes')
    elif numero ==4:
        return print ('El día es el miercoles')
    elif numero ==5:
        return print ('El día es el jueves')
    elif numero ==6:
        return print ('El día es el viernes')
    elif numero ==0:
        return print ('El día es el sabado')
    else:
        return print('Algo esta mal')



main ()