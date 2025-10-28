from pyray import *

SIDE= 40
WIDTH= 40
HEIGHT= 40

snake= [
    [1,1],
    [2,1],
    [3,1]]
vitesse=[1,0]
init_window(SIDE*WIDTH,SIDE*HEIGHT,"Le serpent")
set_target_fps(10)

while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    #Animation
    vx,vy= vitesse
    hx,hy=snake[-1]
    new_head=[hx+vx,hy+vy]
    snake=snake[1:]+[new_head]
    if is_key_pressed(KEY_DOWN):
        vitesse=[0,1]
    if is_key_pressed(KEY_UP):
        vitesse=[0,-1]
    if is_key_pressed(KEY_RIGHT):
        vitesse=[1,0]
    if is_key_pressed(KEY_LEFT):
        vitesse=[-1,0]


   
    #Dessin
    for i, (x,y) in enumerate(snake):
        color= PURPLE if i==len(snake)-1 else DARKPURPLE
        draw_rectangle(x*SIDE+1,y*SIDE+1,SIDE-2,SIDE-2, color)
    
    

    end_drawing()

close_window()
