#TPC7
import matplotlib.pyplot as matp

tabMeteo1 = [([2022, 1, 20], 2, 16, 0),([2022, 1, 21], 1, 13, 0.2), ([2022, 1, 22], 7, 17, 0.01)]

listaTabelas = {"tabMeteo1" : [([2022, 1, 20], 2, 16, 0),([2022, 1, 21], 1, 13, 0.2), ([2022, 1, 22], 7, 17, 0.01)]}

def medias(tabMeteo):
    res = []
    for i in listaTabelas[tabMeteo]:
        res.append(i[0])
        res.append((i[1]+i[2])/2)
    return res

def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")
    file.write(linha(t))
    file.close()
    return

def linha(t):
    res = ""
    for x in listaTabelas[t]:
        res += f"{x[0][0]}::{x[0][1]}::{x[0][2]}:: {x[1]}:: {x[2]}:: {x[3]}::\n"
    return res

def carregaTabMeteo(fnome):
    res = []
    f = open(fnome)
    for linha in f:
        if linha != "":
            campos = linha.split("::")
            data = (int(campos[0]), int(campos[1]), int(campos[2]))
            dados = (data, float(campos[3]), float(campos[4]), float(campos[5]))
            res.append(dados)
    f.close()
    return res

def minMin(tabMeteo):
    min = listaTabelas[tabMeteo][0][1]
    for i in listaTabelas[tabMeteo]:  ###  OU _, i,*_   ---> repete as variáveis seguintes como "_", _ não pode ser usadoa como variável, mas se fosse utilizado outro símbolo tá joinha
        if i[1] < min:
            min = i[1]
        
    return min

def ampterm(tabMeteo):
    res = []
    for i in listaTabelas[tabMeteo]:
        dados = i[0], i[2] - i[1]
        res.append(dados)
    return res 

def maxChuva(tabMeteo):
    max_prec = float(listaTabelas[tabMeteo][0][3])
    max_data = listaTabelas[tabMeteo][0][0]
    for i in listaTabelas[tabMeteo]:
        if i[3] > max_prec:
            max_data = i[0]
            max_prec = i[3]        
    return (max_data, max_prec)

def diasChuvosos(tabMeteo, p):
    res = []
    for i in listaTabelas[tabMeteo]:
        if float(i[3]) > float(p):
            dados=i[0], i[3]
            res.append(dados)    
    return res

def maxPeriodoCalor(tabMeteo, p):
    res = 0
    consecutivo = 0
    for i in listaTabelas[tabMeteo]:
        if float(i[3]) < float(p):
            res += 1
            if res > consecutivo:
                consecutivo = res
        else:
            res = 0
    return consecutivo

def graph(t):
    print("""Escolha um gráfico para visualizar:
1) Gráfico de temperaturas
2) Gráfico de pluviosidade""")
    resposta = input("Que gráfico pretende construir?")

    if resposta == "1":
        matp.title("Temperatura mínima e máxima")
        matp.xlabel("DATAS")
        matp.ylabel("Temperatura (Cº)")
        datas = [str(i[0]) for i in listaTabelas[t]]
        tempMIN = (float(i[1]) for i in listaTabelas[t])
        tempMAX = (float(i[2]) for i in listaTabelas[t])
        matp.plot(datas, tempMIN, label = "tempMin", color = "b", marker = "o")
        matp.plot(datas, tempMAX, label = "tempMax", color = "r", marker = "o")
        matp.legend()
        matp.show()
    elif resposta == "2":
        matp.title("Pluviosidade")
        matp.xlabel("DATAS")
        matp.ylabel("Precipitação (mm / m^2)")
        datas = [str(i[0]) for i in listaTabelas[t]]
        precip = [float(i[3]) for i in listaTabelas[t]]
        matp.bar(datas, precip, color = "pink")
        matp.show()
    else:
        return("Opção inválida!")


Logout = False

while Logout == False:
    
    print("""Olá!
O que quer fazer?
1) Ver temperaturas médias
2) Guardar uma tabela meteorológica
3) Carregar uma tabela meteorológica
4) Ver temperatura mínima
5) Ver amplitudes térmicas
6) Ver precipitação máxima
7) Ver dias com precipitação acima de um valor
8) Ver dias com precipitação abaixo de um valor
9) Construir gráficos de temperatura e precipitação
0) Sair""")

    escolha = input("Escolha uma opção!")

    if escolha == "0":
        Logout = True
        print("Ok, adeus!")

    if escolha == "1":
        tabela = input("Escolha uma tabela meteorológica!")
        print(medias(tabela))
    
    if escolha == "2":
        tabela = input("Escolha uma tabela meteorológica!")
        fnome = input("Escolha um nome para o ficheiro!")
        print(guardaTabMeteo(tabela, fnome))

    if escolha == "3":
        fnome = input("Escolha o nome do ficheiro que deseja carregar!")
        print(carregaTabMeteo(fnome))

    if escolha == "4":
        tabela = input("Escolha uma tabela meteorológica!")
        print(minMin(tabela))

    if escolha == "5":
        tabela = input("Escolha uma tabela meteorológica!")
        print(ampterm(tabela))

    if escolha == "6":
        tabela = input("Escolha uma tabela meteorológica!")
        print(maxChuva(tabela))

    if escolha == "7":
        tabela = input("Escolha uma tabela meteorológica!")
        valor = input("Escolha um valor referência!")
        print(diasChuvosos(tabela, valor))

    if escolha == "8":
        tabela = input("Escolha uma tabela meteorológica!")
        valor = input("Escolha um valor referência!")
        print(maxPeriodoCalor(tabela, valor))

    if escolha == "9":
        tabela = input("Escolha uma tabela meteorológica!")
        graph(tabela)
    

    

