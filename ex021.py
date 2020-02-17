# Faça um programa que abra e reproduza o áudio de um arquivo em MP3
import pygame

pygame.init()
# Carregando o arquivo de áudio
pygame.mixer.music.load('ex021.mp3')
# Toca o arquivo de áudio
pygame.mixer.music.play()
# Espera o evento terminar
pygame.event.wait()
