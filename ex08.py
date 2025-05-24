from functions import *

# 8 Implemente um programa que leia números inteiros e imprima apenas os números que são múltiplos de 3 ou de 5, até que o usuário digite zero para parar (use while e if).

from functions import x

def ex08():
    
    x()
    
    while True :
        
        titulo("Exercício 8 - Múltiplos de 3 ou 5")
        
        num = 1

        while num != 0 :
            num =leitorCoringa(int, "Informe um número inteiro (0 para parar): ", "Valor inválido. Digite um número inteiro.")
            
            if num % 5 == 0 or num % 3 == 0 :
                print(yellow + f"\n{num} é múltiplo de 3 ou 5\n" + default)   
            else : 
                print(red + f"\n{num} não é múltiplo de 3 ou 5\n" + default)
        
        menu("Deseja continuar?", [ "Refazer o exercício", "Menu"])
        continuar = leitorCoringa(int, "Informe a opção: ", "Valor inválido informe um INTEIRO...")
        if continuar == 1 :
            x()
            continue
        else:
            x()
            break
