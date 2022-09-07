#!/usr/bin/python

# ejercicio07.if02.py
# https://experiencia21.tec.mx/courses/315198/files/110396804?module_item_id=19262107


lado1 = float(input())
lado2 = float(input())
lado3 = float(input())

def check(a):
    # return not a > 0
    return a <= 0


if (check(lado1) or check(lado2) or check(lado3)):
    print('ERRor. todos los valores deben ser mayores a 0')
    exit()

if lado1 != lado2 :
    if lado1 != lado3 and lado2 != lado3 :
        print('escaleno')
    else:
        print('isoceles')

elif lado1 != lado3:
    print('isoceles')

else :
    print('equilatero')

