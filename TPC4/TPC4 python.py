<<<<<<< HEAD
import random

def menu1():
    return (f"""
(1) Criar Lista 
(2) Ler Lista
(3) Soma
(4) Média
(5) Maior
(6) Menor
(7) estaOrdenada por ordem crescente
(8) estaOrdenada por ordem decrescente
(9) Procura um elemento
(0) Sair""")

print (menu1())
escolha = int(input())

lista = []

while escolha != 0:
    if escolha == 1:
        lista = []
        elementos = random.randint(1,100)
        for x in range(elementos):
            lista.append(random.randint(0,100))
            
    elif escolha == 2:
        lista = []
        N = int(input("Escolha um número de elementos para a sua lista!"))
        for x in range (N):
            lista.append(int(input("Escolha o elemento que deseja adicionar!")))


    print (f"""{lista}""")

    if escolha == 3:
        soma = 0
        for x in lista:
            soma += x       
        print (f"""A soma dos elementos da lista é {soma}!""")

    elif escolha == 4:
        soma = 0
        for x in lista:
            soma += x
        media = soma/len(lista) 
        print (f"""A média dos elementos da lista é {media}!""")

    elif escolha == 5:
        maior = 0
        for x in lista:
            if x > maior:
                maior = x
        print (f"""O maior dos elementos da lista é {maior}!""")
        
    elif escolha == 6:
        menor = 100
        for x in lista:
            if x < menor:
                menor = x
        print (f"""O menor dos elementos da lista é {menor}!""")

    elif escolha == 7:
        if len(lista)>1:
            crescente = True
            for x in range(len(lista)-1):
                if lista[x]>lista[x+1]:
                    crescente = False
                    break
            if crescente == True:
                print("Sim!")
            else:
                print("Não!")
        else:
            print("Sim!")

    elif escolha == 8:
        if len(lista)>1:
            decrescente = True
            for x in range(len(lista)-1):
                if lista[x]<lista[x+1]:
                    decrescente = False
                    break
            if decrescente == True:
                print("Sim!")
            else:
                print("Não!")
        else:
            print("Sim!")

    elif escolha == 9:
        print("Procure um elemento!")
        num = int(input())
        if num in lista:
            print(lista.index(num))
        else:
            print ("-1")

    print(menu1())
    escolha = int(input())

print(f"""A tua última lista foi {lista}!
Adeus!""")
=======
import random

def menu1():
    return (f"""
(1) Criar Lista 
(2) Ler Lista
(3) Soma
(4) Média
(5) Maior
(6) Menor
(7) estaOrdenada por ordem crescente
(8) estaOrdenada por ordem decrescente
(9) Procura um elemento
(0) Sair""")

print (menu1())
escolha = int(input())

lista = []

while escolha != 0:
    if escolha == 1:
        lista = []
        elementos = random.randint(1,100)
        for x in range(elementos):
            lista.append(random.randint(0,100))
            
    elif escolha == 2:
        lista = []
        N = int(input("Escolha um número de elementos para a sua lista!"))
        for x in range (N):
            lista.append(int(input("Escolha o elemento que deseja adicionar!")))


    print (f"""{lista}""")

    if escolha == 3:
        soma = 0
        for x in lista:
            soma += x       
        print (f"""A soma dos elementos da lista é {soma}!""")

    elif escolha == 4:
        soma = 0
        for x in lista:
            soma += x
        media = soma/len(lista) 
        print (f"""A média dos elementos da lista é {media}!""")

    elif escolha == 5:
        maior = 0
        for x in lista:
            if x > maior:
                maior = x
        print (f"""O maior dos elementos da lista é {maior}!""")
        
    elif escolha == 6:
        menor = 100
        for x in lista:
            if x < menor:
                menor = x
        print (f"""O menor dos elementos da lista é {menor}!""")

    elif escolha == 7:
        if len(lista)>1:
            crescente = True
            for x in range(len(lista)-1):
                if lista[x]>lista[x+1]:
                    crescente = False
                    break
            if crescente == True:
                print("Sim!")
            else:
                print("Não!")
        else:
            print("Sim!")

    elif escolha == 8:
        if len(lista)>1:
            decrescente = True
            for x in range(len(lista)-1):
                if lista[x]<lista[x+1]:
                    decrescente = False
                    break
            if decrescente == True:
                print("Sim!")
            else:
                print("Não!")
        else:
            print("Sim!")

    elif escolha == 9:
        print("Procure um elemento!")
        num = int(input())
        if num in lista:
            print(lista.index(num))
        else:
            print ("-1")

    print(menu1())
    escolha = int(input())

print(f"""A tua última lista foi {lista}!
Adeus!""")
>>>>>>> 1c5ec8b631a9e49651a7f627025cef7a19701098
