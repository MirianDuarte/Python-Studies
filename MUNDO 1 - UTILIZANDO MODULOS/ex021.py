import pygame 
pygame.init() # iniciando o pygame

pygame.mixer.music.load('audio.mp3') # carregando o arquivo
pygame.mixer.music.play() # inicia a reprodução
input() # aguarda o usuario apertar "enter"
pygame.event.wait() # mantém a execução do programa