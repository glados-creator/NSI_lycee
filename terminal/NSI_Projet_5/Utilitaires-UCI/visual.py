import tkinter as tk
import math
import time
import random
import visual_DATA

RADIUS = 20
WIN_COLOR = "yellow"
BEST_COLOR = "blue"
LINK_COLOR = "black"
ACCELERATION = 1.2
OFFSETX = 100
OFFSETY = 100
SCALE = 1.0
MAX_TIME = 0.17
CIRCLE_SPACE = 1
CHANGE = False
MAX_DEPTH = 5
time_start = 0

def random_color():
    """
    Returns a random color in the Tkinter color specification, e.g. "#ff0000".
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"#{r:02x}{g:02x}{b:02x}"

tree_data = (0,False,visual_DATA.DATA)

# tree_data = (None,None,{
#      1 : (0,False,{
#         1 : (0,False,None)        ,2 : (0,False,None)        ,3 : (0,False,None)        ,4 : (0,False,None)
#      })
#     ,2 : (0,False,{
#         1 : (0,False,None)        ,2 : (0,False,None)        ,3 : (0,False,None)        ,4 : (0,False,None)
#     })
#     ,3 : (0,False,{
#         1 : (0,False,None)        ,2 : (0,False,None)        ,3 : (0,False,None)        ,4 : (0,False,None)
#     })
#     ,4 : (0,False,{
#         1 : (0,False,None)        ,2 : (0,False,None)        ,3 : (0,False,None)        ,4 : (0,False,None)
#     })
# })

root = tk.Tk()
canvas = tk.Canvas(root, bg="grey")
canvas.pack(expand=True, fill=tk.BOTH)

def draw_tree(node, x: int, y : int,angle=0,depth=0):
    global OFFSETX, OFFSETY, SCALE, canvas, tree_data,MAX_TIME,time_start,MAX_DEPTH,CIRCLE_SPACE

    # Check if depth or time limit has been reached
    if time.perf_counter() - time_start > MAX_TIME or depth > MAX_DEPTH:
        return
    LINK_WIDTH = 2 * SCALE
    RADIUS = 10
    
    # calculate the scaled offset values
    s_x = (x + OFFSETX) * SCALE
    s_y = (y + OFFSETY) * SCALE
    # calculate screenspace x and y
    DRAWN = False
    # Check if the node is within the screen boundaries
    if (s_x >0 and s_y > 0 and s_x < canvas.winfo_width() and s_y < canvas.winfo_height() ):
        DRAWN = True
        # draw the move
        canvas.create_text(
            s_x,
            s_y,
            text="value "+str(node[0])+"\nwin "+str(node[1])+"\n"+"angle "+str(angle),
            fill="white",
            font=("Arial", int(14*SCALE))
        )

        # draw the node
        canvas.create_oval(
            s_x - RADIUS * SCALE,
            s_y - RADIUS * SCALE,
            s_x + RADIUS * SCALE,
            s_y + RADIUS * SCALE
        )

    if node[2] is None:
        return
    
    num_children = len(node[2].keys())
    # Calculate the adjusted child angle within the range [120; 240]
    child_angle = 120 / num_children
    # if angle == 0 we can take the whole circle
    if depth == 0:
        child_angle = 360 / num_children
    for i, move in enumerate(node[2].keys()):
        (value, is_win, children) = node[2][move]
        # recursively draw the children nodes
        child_angle_offset = i * child_angle
        if depth == 0:
            c_angle_ad =  120 + (child_angle_offset + angle)
        else:
            c_angle_ad =  angle + (child_angle_offset + 120)%120
        c_rad_ad_angle = c_angle_ad* (math.pi / 180)
        # calculate the position of the child node using n-star pattern
        c_x = x + math.cos(c_rad_ad_angle) * (10**CIRCLE_SPACE)
        c_y = y + math.sin(c_rad_ad_angle) * (10**CIRCLE_SPACE)
        # screenspace child x y
        cs_x = (c_x + OFFSETX) * SCALE
        cs_y = (c_y + OFFSETY) * SCALE
        # Call draw_tree recursively for the child node
        draw_tree(node[2][move], c_x, c_y,angle=c_angle_ad,depth=depth+1)

        if DRAWN or (cs_x >0 and cs_y > 0 and cs_x < canvas.winfo_width() and cs_y < canvas.winfo_height()):
            # draw the link
            if is_win:
                line_color = WIN_COLOR
            elif value == node[0]:
                line_color = BEST_COLOR
            else:
                line_color = "black"
            
            canvas.create_line(
                ((x + OFFSETX) + math.cos(c_rad_ad_angle)) *SCALE,
                ((y + OFFSETY) + math.sin(c_rad_ad_angle)) *SCALE,
                ((c_x + OFFSETX) - math.cos(c_rad_ad_angle)) *SCALE,
                ((c_y + OFFSETY) - math.sin(c_rad_ad_angle)) *SCALE,
                width=LINK_WIDTH,
                fill=line_color
                )


def draw_screen():
    global canvas, root, tree_data, SCALE, OFFSETX, OFFSETY,time_start,CHANGE

    if CHANGE:
        canvas.delete("all")
        draw_tree(tree_data, 0, 0)

    canvas.create_rectangle(0,0,100,120,fill="grey")
    canvas.create_text(40, 10, text=f"Scale: {SCALE:.2f}")
    canvas.create_text(40, 30, text=f"Accel: {ACCELERATION:.2f}")
    canvas.create_text(40, 50, text=f"CIRCL_SPC: {CIRCLE_SPACE:.2f}")
    canvas.create_text(40, 70, text=f"OffsetX: {OFFSETX}")
    canvas.create_text(40, 90, text=f"OffsetY: {OFFSETY}")
    canvas.create_text(
        40,
        110,
        text=f"Time: {time.perf_counter() - time_start:.2f} sec",
    )
    time_start = time.perf_counter()
    canvas.update()

    root.after(30, draw_screen)

def on_key_press(event):
    global OFFSETX, OFFSETY, SCALE, ACCELERATION,CHANGE,CIRCLE_SPACE
    CHANGE = True
    SCALE_STEP = 1.1
    SCALE_MAX = 10
    SCALE_MIN = 0.1
    ACCELERATION_STEP = 0.1
    ACCELERATION_MIN = 1
    ACCELERATION_MAX = 20
    CIRCLE_SPACE_MIN = 0
    CIRCLE_SPACE_MAX = 5
    key = event.keysym.lower()
    
    # Handle arrow keys
    if key == 'left':
        OFFSETX -= int(10 * SCALE * ACCELERATION)
    elif key == 'right':
        OFFSETX += int(10 * SCALE * ACCELERATION)
    elif key == 'up':
        OFFSETY -= int(10 * SCALE * ACCELERATION)
    elif key == 'down':
        OFFSETY += int(10 * SCALE * ACCELERATION)
    elif key == "escape":
        exit()

    # Handle M and P keys for scaling
    elif key == 'm':
        SCALE = min(SCALE / SCALE_STEP, SCALE_MAX)
    elif key == 'p':
        SCALE = max(SCALE * SCALE_STEP, SCALE_MIN)
    
    elif key == 'k':
        CIRCLE_SPACE = min(CIRCLE_SPACE-1, CIRCLE_SPACE_MAX)
    elif key == 'i':
        CIRCLE_SPACE = max(CIRCLE_SPACE+1, CIRCLE_SPACE_MIN)

    # Handle ZQSD keys with acceleration
    if key == 'd':
        OFFSETX += 10
    elif key == 'q':
        OFFSETX -= 10
    elif key == 'z':
        OFFSETY -= 10
    elif key == 's':
        OFFSETY += 10

    # Handle O and L keys for adjusting mouse acceleration
    elif key == 'l':
        ACCELERATION = max(ACCELERATION - ACCELERATION_STEP, ACCELERATION_MIN)
    elif key == 'o':
        ACCELERATION = min(ACCELERATION + ACCELERATION_STEP, ACCELERATION_MAX)
    
    # Handle N key to reset offset
    elif event.keysym == 'n':
        OFFSETX = 0
        OFFSETY = 0

def on_mouse_move(event):
    pass

if __name__ == "__main__":
    # Bind event handlers
    canvas.bind("<Motion>", on_mouse_move)
    canvas.focus_set()

    # Start
    root.bind("<Key>", on_key_press)
    root.after(40, draw_screen)
    root.mainloop()
