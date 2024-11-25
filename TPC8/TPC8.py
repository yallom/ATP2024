MyFaceBook = [{'id': 'p1', 
               'conteudo': 'A tarefa de avaliação é talvez a mais ingrata das tarefas que um professor tem de realizar...', 
               'autor': 'jcr', 
               'dataCriacao': '2023-07-20', 
               'comentarios': [{'comentario': 'Completamente de acordo...',
                         'autor': 'prh'},
                        {'comentario': 'Mas há quem goste...',
                         'autor': 'jj'}]}]


listaPosts = []

def quantosPost(redeSocial):
    return len(redeSocial)

def postsAutor(redeSocial, autor):
    lista = []
    for i in redeSocial:
        if i["autor"] == autor:
            lista.append(i)
    return lista

def autores(redeSocial):
    lista = []
    for i in redeSocial:
        if i["autor"] not in lista:
            lista.append(i["autor"])
    return  lista

def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    for i in redeSocial:
        num = i["id"]
    id = int(num[1:]) + 1
    comentarios2 = comentarios.split(":")
    comentarios3 = []
    for i in comentarios2:
        res = i.spli("/")
        comentarios3.append(res)
    comments = {}
    for elem in comentarios3:
        comments.append({"comentario": elem[0],
                    "autor": elem[1]})

    Post = {"id": f"p{id}",
            "conteudo": conteudo,
            "autor": autor,
            "data": dataCriacao,
            "comentarios": comments}
    redeSocial.append(Post)
    return redeSocial

def remPost(redeSocial, id):
    if any (i["id"] == id for i in redeSocial):
        for i in redeSocial:
            if i["id"] == id:
                redeSocial.remove(i)
    else:
        return "Esse id não está disponível!"
    return redeSocial

def postsPorAutor(redeSocial):
    distrib = {}
    for i in redeSocial:
        if all(distrib[x]["autor"] != i["autor"] for x in distrib):
            distrib[i["autor"]] = {"autor": i["autor"],
                                               "posts": 1}
        else:
            distrib[i["autor"]]["posts"] += 1
    return distrib

def comentadoPor(redeSocial, autor):
    lista = []
    for i in redeSocial:
        for x in i["comentarios"]:
            if i["comentarios"][i["comentarios"].index(x)]["autor"] == autor:
                if i not in lista:
                    lista.append(i)
    return lista


Logout = False

while Logout == False:
    print("""Olá!
O que quer fazer?
1) Ver número de posts numa rede social
2) Ver todos os posts de um autor numa rede social
3) Ver todos os autores que já postaram numa rede social
4) Postar numa rede social
5) remover um post de uma rede social
6) Ver distribuição de posts por autor numa rede social
7) Ver posts nos quais um autor comentou, numa rede social
0) Sair""")

    escolha = input("Escolha uma opção!")

    if escolha == "0":
        Logout = True
        print("Ok, adeus!")

    if escolha == "1":
        rede = input("Escolha uma rede social!")
        print(quantosPost(rede))
    
    if escolha == "2":
        rede = input("Escolha uma rede social!")
        autor = input("Escolha um autor!")
        print(postsAutor(rede, autor))

    if escolha == "3":
        rede = input("Escolha uma rede social!")
        print(autores(rede))

    if escolha == "4":
        rede = input("Escolha uma rede social!")
        conteudo = input("Escreva o que quer postar!")
        data = input("Insira a data de hoje")
        comentarios = input("Escreva os comentários no seguinte formato: comentário/autor :: comentário/autor...")
        print(insPost(rede, conteudo, autor, data, comentarios))

    if escolha == "5":
        rede = input("Escolha uma rede social!")
        id = input("Escolha um id de post!")
        print(remPost(rede, id))

    if escolha == "6":
        rede = input("Escolha uma rede social!")
        print(postsPorAutor(rede))

    if escolha == "7":
        rede = input("Escolha uma rede social!")
        autor = input("Escolha um autor!")
        print(comentadoPor(rede, autor))

    
