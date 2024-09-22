import pgzrun
import random

WIDTH=500
HEIGHT= 500

alien=Actor("alien.png")
alien.x= 200
alien.y=300

def draw():
    screen.fill("blue")
    alien.draw()

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("good shot")
        alien.pos=(random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50))
    else:
        print("you missed me")



pgzrun.go()