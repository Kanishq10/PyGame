import pygame
import os
width,height= 720,720
GScreen=pygame.display.set_mode((width,height))   #window
pygame.display.set_caption("Naruto")     #for title of screen
Picture=pygame.image.load(os.path.join('resources','naruto.jpg'))
Song=os.path.join('resources','s1.mp3')

FPS=60
def drawfn():
    GScreen.fill((255,255,255))   #for fill the rgb color to window
    GScreen.blit(Picture,(0,0))   #for inserting a picture  ,(x,y coordinates)
    pygame.display.update()     #update display color


def main():   #function for running the window
    pygame.mixer.init()
    pygame.mixer.music.load(Song)
    pygame.mixer.music.play(-1)
    run=True
    Clock=pygame.time.Clock()

    while run:
        Clock.tick(FPS)       #loop will lock on 60fps ,otherwise it will be dependent on machine
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            drawfn()


if __name__=="__main__":
    main()
