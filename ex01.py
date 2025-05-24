from functions import *
        
#  1 Escreva um programa que receba um número inteiro e informe se ele é par ou ímpar usando if.

def ex01() : 

    x()
    
    while True :
        
        titulo("Exercício 1 - Par ou Ímpar?")
    
        num = leitorCoringa(int, 'Digite um número inteiro: ', 'Valor inválido. Digite um número inteiro.')
        
        if num % 2 == 0:
            print(yellow + f'\nO número {num} é par.\n' + default)
        else:
            print(yellow + f'\nO número {num} é ímpar.\n' + default)

        menu("Deseja continuar?", [ "Refazer o exercício", "Menu"])
        
        continuar = leitorCoringa(int, "Informe a opção: ", "Valor inválido informe um INTEIRO...")
        if continuar == 1 :
            x()
            continue
        else:
            x()
            break
