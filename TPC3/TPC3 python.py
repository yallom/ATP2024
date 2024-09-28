def jogo1(A):
    N = 21
    while N > 0:
        N -= A
        print(f"""Retiraste {A} fósforos! 
        Sobram {N}!""")
        N -= (5-A)
        A = int(input(f"""O computador retira {5-A}!
        Sobram {N}"""))
    return ("Perdeste")

import random

def jogo2():
    N = 21
    t = 0
    while N > 0:
        if N == 21:
            B = random.randint(1,4)
            N -= B
            t += 1
        elif N % 5 != 1 and t == 2:
            B = (5-X-B)
            N -= B
            t += 1
        elif N % 5 != 1:
            B = (5-X)
            N -= B
            t += 1
        else:
            B = random.randint(1,4)
            N -= B
            t += 1
        
        if N > 0:
            X = int(input(f"""O computador retira {B}!
            Sobram {N}"""))
            N -= X
            t += 1
            print(f"""Retiraste {X} fósforos! 
            Sobram {N}!""")
    if t%2 == 1:
        return ("Ganhaste")
    else:
        return ("Perdeste")



print("""Vamos jogar o jogo do fósforo!

Quem apanhar o último fósforo perde!

Podes tirar entre 1 e 4 fósforos!

Queres jogar primeiro? (s/n)""")
resposta = input("Queres jogar primeiro? (s/n)")
if resposta == "s":
    print("Ok! Escolhe um número de 1 a 4")
    A = int(input())
    print(jogo1(A))
else:
    print("Ok! O computador vai escolher um número de 1 a 4!")
    print(jogo2())