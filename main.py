from functions import *

x() 
    

while True :
    
    menu('Lista de Exercícios --', [
        "Par ou Ímpar?",
        "Verificador de Idade",
        "Contagem de 1 a 10",
        "Calculadora de Fatorial",
        "Validador Númerico (1 a 10)",
        "Contagem Regressiva (10 a 1)",
        "Analisador de Sequência Numérica",
        "Filtro de Múltiplos (3 ou 5)"
    ])
    
    exercise = leitorCoringa(int, "Informe o número para acessar o exercício: ", "Valor inválido informe um INTEIRO...")
    
    match exercise :
        case 1: 
            from ex01 import ex01
            ex01()
        case 2:
            from ex02 import ex02
            ex02()
        case 3:
            from ex03 import ex03
            ex03()
        case 4:
            from ex04 import ex04
            ex04()
        case 5:
            from ex05 import ex05
            ex05()
        case 6:
            from ex06 import ex06
            ex06()
        case 7:
            from ex07 import ex07
            ex07()
        case 8:
            from ex08 import ex08
            ex08()
        case _:
            x()
            print(red + "\nOpção inválida, tente novamente.\n" + default)
            y(1)
            continue
        
    menu("Deseja continuar?", [ "Listar exercícios", "Sair do programa"])
    
    continuar = leitorCoringa(int, "Informe a opção: ", "Valor inválido informe um INTEIRO...")

    
    if continuar == 1 :
        x()
        continue
    elif continuar == 2:
        print(green + "\nObrigado por usar o programa!\n" + default)
        print("Aluno: Luiz Gustavo Gonçalves Brito")
        print("RM: 562192\n")
        break
    else :
        x()
        print(red + "\nOpção inválida, tente novamente.\n" + default)
        y(1)
        continue