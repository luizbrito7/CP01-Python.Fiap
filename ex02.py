from functions import *

# 2 Faça um programa que leia a idade do usuário e exiba "Maior de idade" se for maior ou igual a 18, e "Menor de idade" caso contrário.

def ex02() :
    
    x()
    
    while True :
        
        titulo("Exercício 2 - Verificador de Idade")

        idade = leitorCoringa(int, 'Digite sua idade: ', 'Valor inválido. Digite um número inteiro.')
        
        if idade < 0 :
            print(red + '\nIdade inválida, informe um número positivo\n' + default)
            y(2)
            x()
            continue

        if idade >= 18 : 
            print(yellow + '\nMaior de idade\n' + default)
        else:
            print(yellow + '\nMenor de idade\n' + default)

        menu("Deseja continuar?", [ "Refazer o exercício", "Menu"])
        
        continuar = leitorCoringa(int, "Informe a opção: ", "Valor inválido informe um INTEIRO...")
        if continuar == 1 :
            x()
            continue
        else:
            x()
            break
