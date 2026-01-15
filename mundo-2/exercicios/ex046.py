# Contagem regressiva para o Ano Novo
from os import system
from time import sleep
import emoji

system('cls')
for c in range(10, -1, -1): # Contagem regressiva de 10 até 0
    print(c)
    sleep(1)
print(emoji.emojize('Feliz Ano Novo! :fireworks:'))
system('pause')