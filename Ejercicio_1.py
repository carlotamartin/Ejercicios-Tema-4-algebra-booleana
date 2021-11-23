#Escriba, usando comparaciones, un algoritmo que muestre el estado del agua (hielo, líquido, vapor) en función de su temperatura.
def estado_agua_cel (temp):
    if temp>=100:
        return print('La temperatura ' + str(temp)+ 'º (celosious) está en estado gaseoso (vapor)')
    elif temp <=0:
        return print('La temperatura ' + str(temp)+ 'º (celosious) está en estado sólido (hielo)')
    else:
        return print('La temperatura ' + str(temp)+ 'º (celosious) está en estado líquido')


def estado_agua_far (temp):
    if temp>=212:
        return print('La temperatura ' + str(temp)+ 'F (Fahrenheit) está en estado gaseoso (vapor)')
    elif temp <= 32:
        return print('La temperatura ' + str(temp)+ 'F (Fahrenheit) está en estado sólido (hielo)')
    else:
        return print('La temperatura ' + str(temp)+ 'F (Fahrenheit) está en estado líquido')

estado_agua_cel (89)