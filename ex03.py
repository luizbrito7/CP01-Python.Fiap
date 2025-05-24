from functions import *
# 3 Utilizando while, imprima os números de 1 a 10.

def ex03() :
    
    x()
    
    while True :
        
        titulo("Exercício 3 - Contagem de 1 a 10")
    
        numero = 1
        while numero <= 10 :
            y(0.5)
            print(numero)
            numero = numero + 1

        print('\n')
        
        menu("Deseja continuar?", [ "Refazer o exercício", "Menu"])
        continuar = leitorCoringa(int, "Informe a opção: ", "Valor inválido informe um INTEIRO...")
        if continuar == 1 :
            x()
            continue
        else:
            x()
            break