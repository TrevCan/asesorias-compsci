#!/usr/bin/python


while True:
    n = int( input('ingrese un numero entre 1 y mil:\t') )
    if n < 1 or n > 1000:
        input('Te la mamasteeee!! ')
    else:
        break

for c in range( 2, n, 1 ):
    if n%c == 0 :
        print('No es primo!!')
        break
    elif c == n - 1 :
        print("ex primoooo!! ")
        break

if n == 1:
    print("no binaario! ")

