'''
Escriba un algoritmo que determine la categoría deportiva de un usuario en función de su edad:

6 a 7 años: benjamín

8 a 9 años: alevín

10 a 11 años: infantil

12 años y más: cadete

Escriba el programa Python asociado.
'''
def categoria (edad):
    if edad==6 or edad==7:
        return print('El niño con '+ str(edad) +' años es benjamin')
    elif edad==8 or edad==9:
        return print('El niño con '+ str(edad) +' años es alevin')
    elif edad==10 or edad==11:
        return print('El niño con '+ str(edad) +' años es infantil')
    elif edad>12:
        return print('El niño con '+ str(edad) +' años es cadete')

categoria(9)