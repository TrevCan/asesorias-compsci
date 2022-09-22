#!/usr/bin/python3

import time


def sleep(seconds):
        time.sleep(seconds)



# por cada fila ( linea)
for i in range(1,9):
    # de izq a derecha
    for x in range(1,9):
        if i % 2 == 0:
            if x % 2 == 0:
                print('*', end='')
            else:
                print('.', end='')
        else:
            if x % 2 == 0:
                print('.', end='')
            else:
                print('*', end='')
        
    print()


