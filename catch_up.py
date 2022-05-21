from pygame import *
#create game window
window = display.set_mode((700, 500))
display.set_caption("Catch me if you can...")
#set scene background
background = transform.scale(image.load("background.png"), (700, 500))
#creat 2 sprites and place them on the scene
sprite1 = transform.scale(image.load("sprite1.png"), (100, 100))
sprite2 = transform.scale(image.load("sprite2.png"), (100, 100))
sprite3 = transform.scale(image.load("sprite2.png"), (100, 100))
#handle "click on the "Close the window"" event 
game = 1
sprite1x = 100
sprite1y = 300
sprite2x = 600
sprite2y = 300
sprite3x = 400
sprite3y = 300
speed = 10
clock = time.Clock()
fps = 60
def main():
    pass
while game:
    window.blit(background, (0, 0))
    window.blit(sprite1, (sprite1x, sprite1y))
    window.blit(sprite2, (sprite2x, sprite2y))
    window.blit(sprite3, (sprite3x, sprite3y))
    for events in event.get():
        if events.type == QUIT:
            game = 0
    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and sprite2x > 5:
        sprite2x -= speed
    if keys_pressed[K_RIGHT] and sprite2x < 595:
        sprite2x += speed
    if keys_pressed[K_DOWN] and sprite2y < 395:
        sprite2y += speed
    if keys_pressed[K_UP] and sprite2y > 5:
        sprite2y -= speed
    if keys_pressed[K_a] and sprite1x > 5:
        sprite1x -= speed
    if keys_pressed[K_d] and sprite1x < 595:
        sprite1x += speed
    if keys_pressed[K_s] and sprite1y < 395:
        sprite1y += speed
    if keys_pressed[K_w] and sprite1y > 5:
        sprite1y -= speed
    if keys_pressed[K_j] and sprite1x > 5:
        sprite1x -= speed
    if keys_pressed[K_d] and sprite1x < 595:
        sprite1x += speed
    if keys_pressed[K_s] and sprite1y < 395:
        sprite1y += speed
    if keys_pressed[K_w] and sprite1y > 5:
        sprite1y -= speed
    display.update()
    clock.tick(fps)