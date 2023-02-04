import math
import matplotlib.pyplot as plt
import random

# [1 ,2 ,3 ,4 ,5]
# .foreach 
# (g) => lg = [g] * (8*g)
# 1 => [1 1 1 1 1 1 1 1 ]
# get angle
# ang = 360/len(lg)

def circles(c_list: list):
    g_d_list = []  # graph data list

    PRIME_EVEN = 8
    PRIME_ODD = 9
    SPACE_CIRCLE = 3
    CIRCLE_SIZE = 1
    COLOR = "r"

    for j,g in enumerate(c_list):
        # create length of circle list. In this instance
        # i'm multiplying by 8 each time but could be any number.
        lg = [g] * ((PRIME_EVEN if j%2==0 else PRIME_ODD)*g)
        ang = 360/len(lg)  # calculate the angle of each entry in circle list.
        ang_list = []
        for i in range(len(lg)+1):
            ang_list.append(ang*i)
        for i, c in enumerate(lg):
            # calculate the x and y axis points or each circle. in this instance
            # i'm expanding circles by multiples of ten but could be any number.
            x_axis = 0 + (SPACE_CIRCLE*g) * math.cos(math.radians(ang_list[i+1]))
            y_axis = 0 + (SPACE_CIRCLE*g) * math.sin(math.radians(ang_list[i+1]))
            # tuple structure ((axis tuple), circle size, circle colour)
            g_d_list.append(((x_axis, y_axis), CIRCLE_SIZE))

    fig, ax = plt.subplots()
    for c in range(len(g_d_list)):
        circle = plt.Circle(g_d_list[c][0], radius=g_d_list[c][1], fc=COLOR)
        ax.add_patch(circle)
    plt.axis('scaled')
    plt.axis('off')  # optional if you don't want to show axis
    plt.show()

circles([random.randint(1,10) for x in range(10)])