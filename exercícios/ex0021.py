# PYTHON
# Faça um programa que abra e reproduzar audio de um mp3.

import pygame
pygame.init()
pygame.mixer.music.load('som.dat')
pygame.mixer.music.play()
pygame.event.wait()