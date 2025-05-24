from functions import *

# 7 Escreva um programa que leia uma sequência de números inteiros positivos (termina quando o usuário digitar um número negativo), e informe o maior número e a quantidade de números pares digitados (use while e if).

def ex07():
    
    while True :
        
        x()     
    
        titulo("Exercício 7 - Analisador de Sequência Numérica")
        
        print(yellow + "\nPara encerrar o programa digite um número negativo\n" + default)
        
        num = leitorCoringa(int, "Informe um número: ", "Valor inválido. Digite um número inteiro positivo.")

        qtdPares = 0
        maior = num 

        while num >= 0 :
            num = leitorCoringa(int, "Informe um número: ", "Valor inválido. Digite um número inteiro positivo.")

            if num % 2 == 0 :
                qtdPares+=1
            
            if num > maior  :
                maior = num
            
        print("\nQuantidade de pares digitados:", qtdPares)
        print("Maior número digitado:", maior, "\n")
        
        menu("Deseja continuar?", [ "Refazer o exercício", "Menu"])
        continuar = leitorCoringa(int, "Informe a opção: ", "Valor inválido informe um INTEIRO...")
        if continuar == 1 :
            x()
            continue
        else:
            x()
            break