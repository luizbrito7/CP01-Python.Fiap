from functions import *

def ex06():
    
    x()
    
    while True :
        
        titulo("Exercício 6 - Contagem Regressiva (10 a 1)")
        
        num = 10
        while num > 0 :
            y(0.5)
            print(num)
            num = num - 1
        
        print('\n')
        
        menu("Deseja continuar?", [ "Refazer o exercício", "Menu"])
        continuar = leitorCoringa(int, "Informe a opção: ", "Valor inválido informe um INTEIRO...")
        if continuar == 1 :
            x()
            continue
        else:
            x()
            break
        num = 10
        while num >= 1 : 
            print(num)
            num-=1 