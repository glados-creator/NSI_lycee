import math
import matplotlib.pyplot as plt
import random

def circles(c_list: list):
    g_d_list = []  # graph data list

    for g in c_list:
        # create length of circle list. In this instance
        # i'm multiplying by 8 each time but could be any number.
        lg = [g] * (8*g)
        ang = 360/len(lg)  # calculate the angle of each entry in circle list.
        ang_list = []
        for i in range(len(lg)+1):
            ang_list.append(ang*i)
        for i, c in enumerate(lg):
            # calculate the x and y axis points or each circle. in this instance
            # i'm expanding circles by multiples of ten but could be any number.
            x_axis = 0 + (10*g) * math.cos(math.radians(ang_list[i+1]))
            y_axis = 0 + (10*g) * math.sin(math.radians(ang_list[i+1]))
            # tuple structure ((axis tuple), circle size, circle colour)
            g_d_list.append(((x_axis, y_axis), 1, 'r'))

    fig, ax = plt.subplots()
    for c in range(len(g_d_list)):
        circle = plt.Circle(g_d_list[c][0], radius=g_d_list[c][1], fc=g_d_list[c][2])
        ax.add_patch(circle)
    plt.axis('scaled')
    plt.axis('off')  # optional if you don't want to show axis
    plt.show()

circles([random.randint(1,10) for x in range(3)])