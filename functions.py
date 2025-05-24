import os
from time import sleep
# from main import main

# Cores
default = "\033[0m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
green = "\033[1;32m"
red = "\033[1;31m"

# Cabeçalho default
def header() :
    
    print(yellow + r"""
     ______     __  __     _________   ___   ___      ______       ___   __      
    /_____/\   /_/\/_/\   /________/\ /__/\ /__/\    /_____/\     /__/\ /__/\    
    \:::_ \ \  \ \ \ \ \  \__.::.__\/ \::\ \\  \ \   \:::_ \ \    \::\_\\  \ \   
     \:(_) \ \  \:\_\ \ \    \::\ \    \::\/_\ .\ \   \:\ \ \ \    \:. `-\  \ \  
      \: ___\/   \::::_\/     \::\ \    \:: ___::\ \   \:\ \ \ \    \:. _    \ \ 
       \ \ \       \::\ \      \::\ \    \: \ \\::\ \   \:\_\ \ \    \. \`-\  \ \
        \_\/        \__\/       \__\/     \__\/ \::\/    \_____\/     \__\/ \__\/
    """ + default)
    
# Função para limpar o terminal 
def x():
    from os import system
    import platform
    a = platform.system()

    if a == 'Windows':
        system('cls')

    elif a == 'Linux':
        system('clear')
    
    return header()

# Função para dar um timer entre limpar o terminal 
def y(timer) :
    sleep(timer)

# Função para fazer um título de exercício 
def titulo(titulo) :
    print('-' * 40)
    print(f'{titulo:^40}')
    print('-' * 40)
    print('\n')

# Função que inputar um valor com o tipo primitivo específico   
def leitorCoringa(tipoPrimitivo, msg, msgError) :
        
    while True : 
        try :
            x  = tipoPrimitivo(input(f'{msg}').replace(',','.'))
        except :
            print(red + f'\n{msgError}\n'+ default)
            y(1)
        else : 
            return x; 
        
def menu(pergunta, opcao) : 

    print(f'{pergunta}')
    print('\n')
    j = 1
    for i in opcao :
        print(blue + f'({j}) --- {i}'+ default) 
        j+=1
    print('\n')

# Função para fazer um título de exercício 
def titulo(titulo) :
    print(green + '-' * 40)
    print(f'{titulo:^40}')
    print('-' * 40 + default)
    print('\n')

