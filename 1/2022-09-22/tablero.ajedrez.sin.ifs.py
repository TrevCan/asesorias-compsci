#!/usr/bin/python3

import time


def sleep(seconds):
        time.sleep(seconds)

# por cada fila ( linea)
for i in range(1,9):
    # de izq a derecha
    for x in range(1,9):
        modtotal = (i%2) + (x%2)
        modtotal = modtotal % 2 
        myChar = chr(46-4*modtotal)
        #print(modtotal, end='')
        print(myChar, end='')


        
    print()


