
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500

    
    canvas = start_drawing("Scene", scene_width, scene_height)

   
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    
  
    finish_drawing(canvas)

def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3, 
    scene_width, scene_height, width=0, fill="sky blue")

def draw_ground(canvas, scene_width, scene_height) :
    draw_rectangle(canvas, 0, 0,
    scene_width, scene_height / 3, width=0, fill="tan1")

    

    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)


def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")
    center = 730
    bottom = 400
    height = 100
    draw_sun(canvas, center, bottom,height)
def draw_sun(canvas, center, bottom, height):
    swidth = 80
    sheight = 80
    left = center - swidth / 2
    right = center + swidth / 2
    top = bottom + sheight
    draw_oval(canvas, left, top, right, bottom, outline='gray20', width =1, fill="gold1")

    


    diameter = 30
    space = 5
    interval = diameter + space

    
    y = 0
    for row in range(5):
        x = 0
        for cell in range(23):
            draw_line(canvas, x, y,
                    x + diameter, y + diameter, fill="green")
            x += interval
        y += interval

    finish_drawing(canvas)

main()