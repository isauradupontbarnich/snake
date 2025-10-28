from pyray import *
from raylib import*
import random 
SIDE= 40
WIDTH= 20
HEIGHT= 20
SCORE=0
POMME=0
snake= [
    [1,1],
    [2,1],
    [3,1]]
vitesse=[1,0]
fruit=[WIDTH//2,HEIGHT//2]
pomme=[2*WIDTH,2*HEIGHT]
init_window(SIDE*WIDTH,SIDE*HEIGHT,"Le serpent")
set_target_fps(10)
perdu=False
while not window_should_close() and not perdu:
    begin_drawing()
    clear_background(BLACK)
    # DETECTION DES TOUCHES
    if is_key_pressed(KEY_DOWN):
        if vitesse!=[0,-1]:
            vitesse=[0,1]
    elif is_key_pressed(KEY_UP):
        if vitesse!=[0,1]:
            vitesse=[0,-1]
    elif is_key_pressed(KEY_RIGHT):
        if vitesse!=[-1,0]:
            vitesse=[1,0]
    elif is_key_pressed(KEY_LEFT):
        if vitesse!=[1,0]:
            vitesse=[-1,0]

    #Animation
    vx,vy= vitesse
    hx,hy=snake[-1]
    new_head=[hx+vx,hy+vy]
    if new_head == fruit:
        fruit=[
            random.randint(0,WIDTH-1), random.randint(0, HEIGHT)-1
        ]
        SCORE=SCORE+10
        POMME=POMME+1
        if POMME%5==0:
            pomme=[
            random.randint(0,WIDTH-1), random.randint(0, HEIGHT)-1]
    if new_head==pomme:
        pomme=[2*WIDTH, 2*HEIGHT]
        SCORE= SCORE+20   
    
    else:
        snake=snake[1:]
    snake=snake+[new_head]



    # Condition de fin de Partie
    if new_head[0]<0 or new_head[0]>=WIDTH:
        perdu=True
        draw_text("Game Over", WIDTH//2, HEIGHT//2, 100, ORANGE)
    elif new_head[1]<0 or new_head[1]>=HEIGHT:
        perdu=True
        draw_text("Game Over", WIDTH//2, HEIGHT//2, 100, ORANGE)
    elif new_head in snake [:-1]:
        perdu =True
        draw_text("Game Over", WIDTH//2, HEIGHT//2, 100, ORANGE)



   
    #Dessin
    draw_circle(fruit[0]*SIDE, fruit[1]*SIDE, (SIDE-1)/2,RED)
    draw_circle(pomme[0]*SIDE, pomme[1]*SIDE, (SIDE-1)/2,GREEN)
    for i, (x,y) in enumerate(snake):
        color= PURPLE if i==len(snake)-1 else DARKPURPLE
        draw_rectangle(x*SIDE+1,y*SIDE+1,SIDE-2,SIDE-2, color)
    draw_text(f"Score:{SCORE}", 5,0, 50, WHITE)
    

    end_drawing()

close_window()
