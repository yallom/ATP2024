#TPC5: Aplicação Para Gerir Um Cinema


listaCinemas = {}
listaSalas = {}


def CriarCinema(nomeCinema):
    if nomeCinema not in listaCinemas:
        listaCinemas[nomeCinema] = []
        return "Cinema adicionado com sucesso!"
    else:
        return f"O cinema {nomeCinema} já existe!"

def CriarSala(salaNome,filme,lugares,vendidos):
    if salaNome not in listaSalas:
        sala = {"lugares" : lugares,
                "vendidos" : list(vendidos.split(" ")),
                "filme" : filme, 
                "nomeSala" : salaNome}
        listaSalas[salaNome] = sala
        return "Sala criada com sucesso!"

def inserirSala(cinema,sala):
    if cinema in listaCinemas:
        if all (i["nomeSala"] != sala["nomeSala"] for i in listaCinemas[cinema]) and sala in listaSalas:
            if all (i["filme"] != sala["filme"] for i in listaCinemas[cinema]):
                listaCinemas[cinema].append(listaSalas[sala])
                return f"Sala {sala} adicionada ao cinema {cinema}!"
    return "Sala já existe ou cinema não encontrado!"

def listar(cinema):
    if cinema in listaCinemas:
        lista = [i["filme"] for i in listaCinemas[cinema]]
        return lista
    return "Cinema não encontrado!"

def disponivel(cinema,filme,lugar):
    if cinema in listaCinemas:
        for i in listaCinemas[cinema]:
            if i["filme"] == filme:
                if int(lugar) <= int(i["lugares"]):
                    if lugar in i ["vendidos"]:
                        return False
                    else:
                        return True
                else:
                    return "Esse lugar não existe!"
        return "Esse filme não está disponível!"

def vendebilhete(cinema,filme,lugar):
    if cinema in listaCinemas:
        for i in listaCinemas[cinema]:
            if i["filme"] == filme:
                if int(lugar) <= int(i["lugares"]):
                    if lugar not in i["vendidos"]:
                        i["vendidos"].append(lugar)
                        return f"Lugar {lugar} vendido para o filme '{filme}' no cinema '{cinema}'."
                    else:
                        return "Esse lugar já está ocupado!"
                else:
                    return "Esse lugar não existe!"
        return "Esse filme não está disponível!"
    return "Esse cinema não existe!"
def listardisponibilidades(cinema):
    if cinema in listaCinemas:
        listadisp = []
        for i in listaCinemas[cinema]:
            disp = [i["nomeSala"], i["filme"], int(i["lugares"]) - len(i["vendidos"])]
            listadisp.append(disp)
        return listadisp
    return "Cinema não encontrado!"


Logout = False


while Logout == False:

    print (f"""Olá!
Escolha um modo de utilização!
       
1)Listar filmes
2)Escolher lugar para ver um filme
3)Comprar bilhete para filme
4)Ver lugares de todos os filmes em exibição
5)Inserir nova sala e filme a um cinema
6)Criar cinema
7)Criar sala
0)Sair""")

    resposta = input()


    if resposta == "1":
        nomeCinema = input("Escolha um cinema para ver!")
        print(listar(nomeCinema))

    elif resposta == "2":
        nomeCinema = input("Escolha um cinema para ver!")
        filme = input("Escolha um filme para ver!")
        lugar = input("Escolha um lugar para ver!")
        print (disponivel(nomeCinema,filme,lugar))

    elif resposta == "3":
        nomeCinema = input("Escolha um cinema para ver!")
        filme = input("Escolha um filme para ver!")
        lugar = input("Escolha um lugar para ver!")
        print (vendebilhete(nomeCinema,filme,lugar))

    elif resposta == "4":
        nomeCinema = input("Escolha um cinema para ver!")
        print (listardisponibilidades(nomeCinema))

    elif resposta == "5":
        nomeCinema = input("Escolha um cinema para ver!")
        salaNome = input("Escolha uma sala para adicionar!")
        print (inserirSala(nomeCinema,salaNome))

    elif resposta == "6":
        nomeCinema = input("Escolha um nome para o novo cinema!")
        print (CriarCinema(nomeCinema))
    
    elif resposta == "7":
        sala = input("Escolha um nome para a sala!")
        filme = input("Escolha um filme para ver!")
        lugares = input("Escolha o número de lugares da sala!")
        vendidos = input("Escolha os lugares cujos bilhetes já foram vendidos!")
        print (CriarSala(sala,filme,lugares,vendidos))
    elif resposta == "0":
        print ("Ok, adeus!")
        Logout = True


