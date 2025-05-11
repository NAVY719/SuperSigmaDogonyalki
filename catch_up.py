from pygame import *

okoshko = display.set_mode((700, 500))
display.set_caption('Шкебеде')

fon = transform.scale(image.load('olivje.jfif'), (700, 500))

s1 = transform.scale(image.load('skebede.jfif'), (100, 100))
s2 = transform.scale(image.load('skebede.jfif'), (100, 100))
x1 = 150
y1 = 300
x2 = 450
y2 = 300
    
clock = time.Clock()
FPS = 100

game = True
#tut bil vlad
while game:
    okoshko.blit(fon, (0, 0)) 
    okoshko.blit(s1, (x1, y1))
    okoshko.blit(s2, (x2, y2))
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if keys_pressed[K_w] and y1 > 0:
        y1 -= 5
    if keys_pressed[K_s] and y1 < 400:
        y1 += 5
    if keys_pressed[K_d] and x1 < 600:
        x1 += 5
    if keys_pressed[K_a] and x1 > 0:
        x1 -= 5
    if keys_pressed[K_UP] and y2 > 0:
        y2 -= 5
    if keys_pressed[K_DOWN] and y2 < 400:
        y2 += 5
    if keys_pressed[K_RIGHT] and x2 < 600:
        x2 += 5
    if keys_pressed[K_LEFT] and x2 > 0:
        x2 -= 5
    clock.tick(FPS)
    display.update()
