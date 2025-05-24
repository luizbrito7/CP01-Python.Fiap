from functions import *

def ex04() :
    
    x()
    
    while True :
        
        titulo("Exercício 4 - Calculadora de Fatorial")
        
        num = leitorCoringa(int, 'Informe um número inteiro: ', 'Valor inválido. Digite um número inteiro positivo.')

        fatorial = num
        
        if num == 0 : 
            fatorial = 1
            
        else : 
            while num > 1 :
                fatorial = fatorial * (num -1)
                num-=1
    
        print('\n')
        print(yellow + f"{fatorial} é o fatorial do número informado" + default)
        print('\n')
        
    
        menu("Deseja continuar?", [ "Refazer o exercício", "Menu"])
        continuar = leitorCoringa(int, "Informe a opção: ", "Valor inválido informe um INTEIRO...")
        if continuar == 1 :
            x()
            continue
        else:
            x()
            break
