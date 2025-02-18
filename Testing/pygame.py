import pygame
import time

#start = time.time()
#end = time.time()
#end-start = final_time

gameScreen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pygame Mouse Click - Test Game')

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("YAY!")
        if event.type == pygame.QUIT:
            exit()



