from functions import *

# 5 Faça um programa que peça um número entre 1 e 10 e continue pedindo até que o usuário digite um número válido (use while e if).

def ex05() :
    
    x()
    
    while True :
        
        titulo("Exercício 5 - Validador Númerico (1 a 10)")
        
        num = leitorCoringa(float, 'Informe um número entre 1 e 10: ', 'Valor inválido. Digite um número INTEIRO')
        
        if num < 1 or num > 10 :
            print(red + '\nNúmero inválido, informe um número entre 1 e 10\n' + default)
            y(2)
            x()
            continue
        else:
            print(yellow + '\nNúmero válido digitado, fim do programa\n' + default)
        
        menu("Deseja continuar?", [ "Refazer o exercício", "Menu"])
        continuar = leitorCoringa(int, "Informe a opção: ", "Valor inválido informe um INTEIRO...")
        if continuar == 1 :
            x()
            continue
        else:
            x()
            break