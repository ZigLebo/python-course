import sys, pygame, time
pygame.init()

size = width, height = 800, 600
speed = [5, 4]
black = 0, 0, 0
white=255,255,255

screen = pygame.display.set_mode(size)

ball = pygame.image.load("DVD-Video_bottom-side.jpg")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    ballrect=ballrect.move(speed)
    if ballrect.left<0 or ballrect.right>width:
        speed[0]=-speed[0]
    if ballrect.top<0 or ballrect.bottom>height:
        speed[1]=-speed[1]

    time.sleep(0.01)
    #screen.fill(white)
    screen.blit(ball, ballrect)
    pygame.display.flip()
