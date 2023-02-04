# -*- coding: UTF-8 -*-
# programme principal
from turtle import *
import time

def square(l,y):
    x = y -1
    if x <= 0:
        exitonclick()
        exit(0)
    for _ in range(0,5):
        forward(l)
        left(90)
    forward(l/2)
    left(45)
    print(f"calling x={x}")
    square(l/1.5,x)

if __name__ == "__main__":
    up()
    goto(-100,-100)
    down()
    square(int(input("l : ")),int(input("x : ")))
