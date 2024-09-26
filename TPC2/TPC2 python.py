
#O Jogador adivinha o número do PC

import random
t = 1

def PCescolhe(adivinha, t):
    
    num = random.randint(0,100)

    while adivinha != num:
        if adivinha < num:
            print("Demasiado baixo! Tenta de novo!")
            adivinha = int(input())
            t = t + 1
        if adivinha > num:
            print("Demasiado alto! Tenta de novo!")
            adivinha = int(input())
            t = t + 1
    
    print (f"""Acertaste em {t} tentativas! 
O número era {num}!!!""")
    t=1
    
#O PC adivinha o número do Jogador



def Jogadorescolhe(x,t):
    
    PCnum = 50

    while PCnum != x and 0>x>100:
        if PCnum > x:
            PCnum = PCnum // 2
            t = t + 1
        else:
            PCnum = PCnum * 3
            PCnum = PCnum // 2
            t = t + 1
            if PCnum > 100:
                PCnum = 100
    PCnum = 50
    print(f"""o teu número era {x}!
O PC acertou em {t} tentativas!""")
    t = 1

    
escolha = int(input("""1) Adivinhar o número do PC                    
2) Deixar o PC adivinhar o teu número"""))
if escolha == 1:

    x = int(input("""O meu número está entre 0 e 100! 
        Adivinha qual é!"""))
    print (PCescolhe(x,t))

else:
    x = int(input("""Escolhe o teu número!"""))
    print(Jogadorescolhe(x,t))

