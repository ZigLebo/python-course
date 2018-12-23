import sys, pygame, time
pygame.init()
size=width,hidth=800,600
speed=[1,1]
white=255,255,255
screen=pygame.display.set_mode(size)
dvd=pygame.image.load("1200px-DVD_logo.svg.png")
dvdrect=dvd.get_rect()
while 1:
    for event in pygame
screen.fill(white)
screen.blit(dvd, dvdrect)
pygame.display.flip()
