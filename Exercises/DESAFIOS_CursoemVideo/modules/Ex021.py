import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.play()
pygame.mixer.music.pause()
pygame.event.wait()
