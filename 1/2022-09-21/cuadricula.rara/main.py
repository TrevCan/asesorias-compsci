#!/usr/bin/python

import os
import time

sleep_time = 0.5

max_x = 79
min_x = 1
max_y = 20
min_y = 1
x = 1
y = 1
blankSeparator='.'
star='*'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def sleep(seconds):
    time.sleep(seconds)


def showGrid(x,y):
    if(x < 1):
        x = max_x + x 
    elif(x > max_x):
        x = x - max_x

    if(y < 1):
        y = max_y + y
    elif(y > max_y):
        y = y - max_y


    for yp in range(min_y,y):
        print(blankSeparator*max_x)

    print(blankSeparator*(x-min_x), end='')
    print(star, end='')
    print(blankSeparator*(max_x-x))
    for yp in range(min_y,max_y-y):
        print(blankSeparator*max_x)

def inRangeAbsoluteX(x):
    return x in range(min_x,max_x+1)

def inRangeAbsoluteY(y):
    return x in range(min_y,max_y+1)

def inRange(x, minG, maxG):
    return x in range(minG,maxG+1)

def askN():
    n = int ( input('Dame un valor entre 1 y 20:\t') )
    while not inRange(n, 1, 20):
        n = int ( input('Valor debe estar entre 1 y 20:\t') )

    return n

def animate(posx,posy,posnx,posny):
    if posx != posnx:
        step = 1
        # move to the left
        if not posx < posnx:
            step = -1
            print('min111')
        for x in range(posx,posnx+1,step):
            clear()
            showGrid(x,posy)
            sleep(sleep_time)
    else:
        step = 1
        # move up
        if not posy < posny:
            step = -1
        for y in range(posy,posny+1,step):
            clear()
            showGrid(posx,y)
            sleep(sleep_time)

def menu():

    n=askN()
    
    y = 1 
    x = 1
    nx = x
    ny = y
        
    print("""
    1) [W] arriba	
    2) [A] izquierda	
    3) [S] down
    4) [D] derecha	
    5) [ ] exit	
    """)

    while True:

        option = input('elija una opcion:\t')
        option = option.lower()
        match option:
            case '1' | 'w':
                ny = y - n
                print('w')
            case '2' | 'a':
                nx = x - n
                print('a')
            case '3' | 's':
                ny = y + n
                print('s')
            case '4' | 'd':
                nx = x + n
                print('d')
            case _:
                print('Exiting...')
                exit()
        print('@(',x  ,y,  ')')
        print('@(',nx ,ny, ')')
        animate(x,y,nx,ny)
        x = nx
        y = ny



menu()
