#PROJETO PROGRAMAÇÃO
import os
import json #importa o formato do documento do dataset
import matplotlib.pyplot as matp #importa as funcionalidades do matplotlib
import PySimpleGUI as sg
from typing import Dict, List


################################################################################## FUNÇÕES ###############################################################################################
Paper_file = []

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregaFicheiro(nome):
    global current_filename  # Add this to track the loaded filename
    try:
        with open(nome, "r", encoding="utf-8") as file:
            ficheiro = json.load(file)
        print(f"Ficheiro '{nome}' carregado com sucesso!")
        current_filename = nome  # Store the name of the loaded file
        return ficheiro
    except FileNotFoundError:
        print(f"Ficheiro '{nome}' não encontrado.")
        return []
    except json.JSONDecodeError:
        print(f"Ficheiro '{nome}' não é um JSON válido.")
        return []

def save_on_exit():
    try:
        if 'current_filename' in globals():  # Check if a file was loaded
            guardaFicheiro(current_filename, Paper_file)
            print("Alterações guardadas com sucesso!")
        else:
            print("Nenhum ficheiro foi carregado para guardar alterações.")
    except Exception as e:
        print(f"Erro ao guardar alterações: {e}")

Paper_file = carregaFicheiro("ata_medica_papers.json")

def guardaFicheiro(nome, dados): #função de exportação de datasets
    try:
        with open(nome, "w", encoding="utf-8") as file:
            json.dump(dados, file, ensure_ascii=False, indent=4) #guarda os dados num ficheiro de nome "nome". ensure_ascii=False significa que podemos meter simbolos especiais (~), indent significa que cria uma margem pequena no inicio do ficheiro
        print(f"Ficheiro '{nome}' guardado com sucesso!")
    except Exception as e: #para qualquer erro, mostra ao utilizador o erro que ocorreu
        print(f"Erro a guardar ficheiro '{nome}': {e}")


def exportSearch(nome, dados): #função de exportação de uma lista de pesquisa
    try:
        with open(nome, "w", encoding="utf-8") as file:
            json.dump(dados, file, ensure_ascii=False, indent=4)
        print(f"Resultados de pesquisa exportados para o ficheiro '{nome}'!")
    except Exception as e:
        print(f"Erro a exportar resultados de pesquisa para '{nome}': {e}")

def insPaper(abstract, keywords, autores, link1, pdf, data, title, link2): #função de criação de artigos
    Paper = {"abstract": abstract,
             "keywords": keywords,
             "authors": autores,
             "doi" : link1,
             "pdf" : pdf,
             "publish_date" : data,
             "title" : title,
             "url" : link2} #cria um dicionario com todos os dados relevantes a um artigo
    Paper_file.append(Paper) #insere o artigo no ficheiro (sem o guardar)
    print(f"Paper '{title}' publicado com sucesso!")

def editarPaper(titulo, title, abstract, keywords, authors, data): #função de edição de artigos
    for i in Paper_file:
        if i["title"] == titulo: #verifica se cada artigo é o que se pretende alterar
            artigo = i
    if title == "s": #se o utilizador quiser alterar o titulo escreve "s"
        title = input("Qual deve ser o novo título?")
        Paper_file[Paper_file.index(artigo)]["title"] = title
    if abstract == "s": #se o utilizador quiser alterar a sinpose escreve "s"
        abstract = input("Qual deve ser a nova sinopse?")
        Paper_file[Paper_file.index(artigo)]["abstract"] = abstract
    if keywords == "s": #se o utilizador quiser alterar as palavras-chave escreve "s"
        keywords = input("Quais devem ser as novas palavras-chave? (separadas por vírgulas)")
        Paper_file[Paper_file.index(artigo)]["keywords"] = keywords
    if authors == "s": #se o utilizador quiser alterar os autores escreve "s"
        resposta = input("Deseja adicionar, remover, ou editar algum autor? (a/r/e)")
        if resposta == "a": #se o utilizador quiser adicionar um autor escreve "a"
            numauth = int(input("Quantos autores quer adicionar?"))
            while numauth > 0: #conta o número de autores que já foram adicionados
                autor = input("Nomeie um autor")
                afiliação = input("Qual a afiliação desse autor?")
                pessoa = {"name" : autor,
                          "affiliation" : afiliação} #cria um dicionário com toda a informação relevante a um autor
                numauth -= 1
                Paper_file[Paper_file.index(artigo)]["authors"].append(pessoa) #insere o autor no artigo
        elif resposta == "r": #se o utilizador quiser remover um autor escreve "r"
            print(Paper_file[Paper_file.index(artigo)]["authors"]) #mostra ao utilizador os autores no artigo
            removido = int(input("Qual o número do autor que pretende remover? (1-x)"))
            Paper_file[Paper_file.index(artigo)]["authors"].remove(Paper_file[Paper_file.index(artigo)]["authors"][removido - 1]) #remove o autor escolhido pelo utilizador
        elif resposta == "e": #se o utilizador quiser editar um autor escreve "e"
            print(Paper_file[Paper_file.index(artigo)]["authors"])
            alterado = int(input("qual o número do autor que pretende alterar? (1-x)"))
            modo = input("Pretende alterar o nome, a afiliação, ou ambos? (1,2,3)") 
            if modo == "1":  #se o utilizador quiser alterar o nome do autor
                novonome = input("Escolha um novo nome!")
                Paper_file[Paper_file.index(artigo)]["authors"][alterado - 1]["name"] = novonome
            elif modo == "2":  #se o utilizador quiser alterar a afiliação do autor
                novaafiliacao = input("Escolha uma nova afiliação!")
                Paper_file[Paper_file.index(artigo)]["authors"][alterado - 1]["affiliation"] = novaafiliacao
            elif modo == "3":  #se o utilizador quiser alterar o nome e afiliação do autor
                novonome = input("Escolha um novo nome!")
                Paper_file[Paper_file.index(artigo)]["authors"][alterado - 1]["name"] = novonome
                novaafiliacao = input("Escolha uma nova afiliação!")
                Paper_file[Paper_file.index(artigo)]["authors"][alterado - 1]["affiliation"] = novaafiliacao
    if data == "s": #se o utilizador quiser alterar a data de publicação escreve "s"
        data = input("Qual deve ser a nova data de publicação?(YYYY-MM-DD)")
        Paper_file[Paper_file.index(artigo)]["publish_date"] = data

    return f"Processo concluido com sucesso: {Paper_file[Paper_file.index(artigo)]}"

def searchPaper(resposta: int): #função de pesquisa de artigos
    listapesquisa = []
    if resposta == 1: #se o utilizador quiser pesquisar por titulo
        title = input("Insira um título para pesquisar!")
        for i in Paper_file:
            if "title" in i: #verifica se o artigo tem título
                if i["title"] == title:
                    listapesquisa.append(i)

    elif resposta == 2: #se o utilizador quiser pesquisar por palavras-chave
        keywords = input("Insira palavras-chave para pesquisar!" )       
        for i in Paper_file:
            if "keywords" in i: #verifica se o artigo tem palavras-chave
                if keywords in i["keywords"].split(","):
                    listapesquisa.append(i)
                    
    elif resposta == 3: #se o utilizador quiser pesquisar por data de publicação
        data = input("Insira uma data para pesquisar!" )
        for i in Paper_file:  
            if "publish_date" in i: #verifica se o artigo tem data de publicação
                if data in i["publish_date"]: 
                    listapesquisa.append(i)


    elif resposta == 4: #se o utilizador quiser pesquisar por autor
        author = input("Insira um autor para pesquisar!" )  
        for i in Paper_file:     
            for x in i["authors"]: 
                if "name" in x: #verifica se o autor tem nome
                    if x["name"] == author:
                        listapesquisa.append(i)

    elif resposta == 5: #se o utilizador quiser pesquisar por afiliação
        affiliation = input("Insira uma afiliação para pesquisar!" )  
        for i in Paper_file:
            for x in i["authors"]:
                if "affiliation" in x: #verifica se o autor tem afiliação
                    if x["affiliation"] == affiliation:
                        listapesquisa.append(i)

    else:  #se o utilizador não submeter uma opção válida
        return "Essa resposta não é valida!"
    
    if len(listapesquisa) > 0: #verifica se algum ficheiro foi encontrado com os parametros estabelecidos
        return listapesquisa
    else:
        return "Nenhum ficheiro encontrado!"

def searchPaper2(sublista: list, resposta: int): #função de pesquisa de artigos
    listapesquisa = []
    if resposta == 1: #se o utilizador quiser pesquisar por titulo
        title = input("Insira um título para pesquisar!")
        for i in sublista:
            if "title" in i: #verifica se o artigo tem título
                if i["title"] == title:
                    listapesquisa.append(i)

    elif resposta == 2: #se o utilizador quiser pesquisar por palavras-chave
        keywords = input("Insira palavras-chave para pesquisar!" )       
        for i in sublista:
            if "keywords" in i: #verifica se o artigo tem palavras-chave
                if keywords in i["keywords"].split(","):
                    listapesquisa.append(i)
                    
    elif resposta == 3: #se o utilizador quiser pesquisar por data de publicação
        data = input("Insira uma data para pesquisar!" )
        for i in sublista:  
            if "publish_date" in i: #verifica se o artigo tem data de publicação
                if data in i["publish_date"]: 
                    listapesquisa.append(i)


    elif resposta == 4: #se o utilizador quiser pesquisar por autor
        author = input("Insira um autor para pesquisar!" )  
        for i in sublista:     
            for x in i["authors"]: 
                if "name" in x: #verifica se o autor tem nome
                    if x["name"] == author:
                        listapesquisa.append(i)

    elif resposta == 5: #se o utilizador quiser pesquisar por afiliação
        affiliation = input("Insira uma afiliação para pesquisar!" )  
        for i in sublista:
            for x in i["authors"]:
                if "affiliation" in x: #verifica se o autor tem afiliação
                    if x["affiliation"] == affiliation:
                        listapesquisa.append(i)

    else:  #se o utilizador não submeter uma opção válida
        return "Essa resposta não é valida!"
    
    if len(listapesquisa) > 0: #verifica se algum ficheiro foi encontrado com os parametros estabelecidos
        return listapesquisa
    else:
        return "Nenhum ficheiro encontrado!"

def eliminar_publicacao(titulo: str) -> bool:
    #Elimina uma publicação da base de dados
    try:
        for pub in Paper_file:
            if pub['title'] == titulo:
                Paper_file.remove(pub)
                return True
        else: 
            return False
    except Exception as e:
        print(f"Erro ao eliminar publicação: {e}")
        return False

def elimPaper():
    pesquisa = []
    print("""Menu de Eliminação
      [1] Pesquisar por título
      [2] Pesquisar por palavras-chave
      [3] Pesquisar por data
      [4] Pesquisar por autor
      [5] Pesquisar por afiliação""")
    resposta = int(input("Escolha uma opção: "))
    pesquisa = searchPaper(resposta)
    while len(pesquisa) > 9:
        print(f"""O resultado da pesquisa retornou {len(pesquisa)} items. Adicione outro critério de pesquisa.
            [1] Pesquisar por título
            [2] Pesquisar por palavras-chave
            [3] Pesquisar por data
            [4] Pesquisar por autor
            [5] Pesquisar por afiliação""")
        resposta = int(input("Escolha uma opção: "))
        pesquisa = searchPaper2(pesquisa, resposta)
    if type(pesquisa) != type(["a", "b", "c"]):
        print(pesquisa)
        print("A pesquisa não retornou nenhum paper que possa ser eliminado.")
        return 0
    else:
        print("Menu de Eliminação")
        for i in range(len(pesquisa)):
            print(f'[{i+1}] {pesquisa[i]["title"]}')
        print("\n" + "[0] Cancelar operação")
        resposta = int(input("Escolha o paper a eliminar: "))-1
        while resposta not in range(len(pesquisa)):
            if resposta == -1: return 0
            else:
                resposta = int(input("Escolha inválida. Tente outra vez: "))-1
        target = pesquisa[resposta]
        Paper_file.remove(target)
        return 0


def listarauth(resposta): #função de listar autores
    listauth = {}
    authors = {}
    for i in Paper_file:
        if 'authors' in i:
            authors = i["authors"]
            for x in authors:
                if isinstance(x, Dict):
                    if x["name"] not in listauth: #verifica se o autor já foi adicionado à lista
                        listauth[str(x["name"])] = [1]
                        if 'title' in i:
                            listauth[str(x["name"])].append(i['title']) #adiciona o autor à lista e define o número de ocorreências como 1
                    else:
                        listauth[str(x["name"])][0] += 1
                        if 'title' in i:
                            listauth[str(x["name"])].append(i['title']) #acrescenta 1 ao número de ocorrências do autor, se este já estiver na lista
    if resposta == "1": #o utilizador escolhe de que forma quer ordenar os dados: 1-por número de artigos por autor (maior->menor), 2-por ordem alfabética dos autores
        listaordenada = sorted(listauth.items(), key = lambda autor: autor[1]) #função normal lambda
    elif resposta == "2":
        listaordenada = sorted(listauth.items(), key = lambda autor: autor[0])
    else:
        return listauth
    return listaordenada

def listarkeywords(resposta): #função de listar palavras-chave
    listkeys = {}
    for i in Paper_file:
        if "keywords" in i:
            for x in i["keywords"].split(","): #prepara os dados para análise, cada vírgula representa uma separação nas keywords
                x = x.strip() #retira espaços em branco no início e no fim das palavras-chave, para " criança" e "criança" não serem contadas como variáveis diferentes
                if x not in listkeys: #verifica se a keyword já foi adicionada à lista
                    listkeys[str(x)] = {"Ocorrências" : 1,
                                        "Artigos" : [i["title"]]} #cria um novo dicionário dentro de listkeys, que tem o nome da keyword atual, e define o número de ocorrências como 1, adicionando o artigo presente à lista de artigos
                else:
                    listkeys[str(x)]["Ocorrências"] += 1 #+1 ao número de ocorrências da keyword
                    listkeys[str(x)]["Artigos"].append(i["title"]) #adiciona o titulo do artigo a lista de artigos desta keyword
    if resposta == "1":
        listaordenada = sorted(listkeys.items(), key = lambda chave: chave[1]["Ocorrências"], reverse = True) #ordena listkeys, a partir do número de ocorrências de cada keyword (maior->menor)
        listasimplificada = [(i[0], i[1]["Ocorrências"]) for i in listaordenada] #cria uma nova lista, sem os nomes dos artigos de cada keyword

        return listasimplificada
    elif resposta == "2":
        listaordenada = sorted(listkeys.items(), key = lambda chave: chave[0]) #ordena listkeys, por ordem alfabética de keywords
        listasimplificada = [(i[0], i[1]["Ocorrências"]) for i in listaordenada] #cria uma nova lista, sem os nomes dos artigos de cada keyword

        return listasimplificada
    else:
        listasimplificada = [(i[0], i[1]["Ocorrências"]) for i in listkeys] #se nenhuma das opções normais for selecionada, o programa devolve uma lista simplificada, mas não ordenada

        return listasimplificada
    
def graph():
    print("""Escolha um gráfico para visualizar:
1) Gráfico de publicações por ano
2) Gráfico de publicações por mês, num ano
3) Gráfico de publicações por autor (Top 20)
4) Gráfico de publicações de um autor ao longo dos anos
5) Gráfico de ocorrências de palavras-chave (Top 20)
6) Lista de palavras-chave com maior ocorrência em cada ano""")
    resposta = input("Que gráfico pretende construir?")

    if resposta == "1":
        listdatas = {}
        for i in Paper_file:
            if "publish_date" in i:
                x = i["publish_date"] #x= YYYY/MM/DD
                if x[0:4] not in listdatas: #verifica se o ano em que o artigo foi publicado já existe em listadatas
                    listdatas[x[0:4]] = 1 #cria uma constante (x[0:4]) e dá-lhe o valor de 1
                else:
                    listdatas[x[0:4]] += 1 #+1 para o número de ocorrências de artigos num ano, se o ano já existir na lista
            elif "publish_date" not in i and "N/A" not in listdatas: #se o artigo não tiver data, e se ainda não houver uma constante de data indefinida em listadatas, cria essa constante e dá-lhe o valor de 1
                listdatas["N/A"] = 1
            else:
                listdatas["N/A"] += 1 #+1 para "N/A"
        matp.title("Distribuição de artigos por ano") #define titulo do grafico
        matp.xlabel("ANOS") #define nome da abcissa
        matp.ylabel("Publicações") #define nome da ordenada
        listaordenada = sorted(listdatas.items(), key = lambda param: param[0]) #ordena a lista de datas, de acordo com o número de publicações por ano (menor->maior)
        datas = [i[0] for i in listaordenada] #cria um alista apenas com os anos, já ordenados
        Publicações = [int(i[1]) for i in listaordenada] #cria uma lista, apenas com as ocorrências, já ordenadas
        matp.bar(datas, Publicações, label = "Nº de Artigos", color = "b") #define x = datas, y = Publicações, nome da variável = "Nº de Artigos", cor do grafico = blue, identificador de dados = círculo ("o")
        matp.legend() #ativa a legenda (nome da variável)
        matp.show() #ativa o gráfico

    if resposta == "2":
        listdatas = {}
        ano = input("Que ano deseja visualizar?")
        for i in Paper_file:
            if "publish_date" in i:
                x = i["publish_date"] #x= YYYY/MM/DD
                if x[0:4] == ano and x[5:7] not in listdatas: #verifica se o mês em que o artigo foi publicado já existe em listadatas e se o artigo pertence ao ano correto
                    listdatas[x[5:7]] = 1
                elif x[0:4] == ano:
                    listdatas[x[5:7]] += 1
        matp.title("Distribuição de artigos num ano")
        matp.xlabel("MESES")
        matp.ylabel("Publicações")
        listaordenada = sorted(listdatas.items(), key = lambda param: param[0])
        autores = [i[0] for i in listaordenada]
        Publicações = [int(i[1]) for i in listaordenada]
        matp.bar(autores, Publicações, label = "Nº de Artigos", color = "r") #cor do grafico = "red"
        matp.legend()
        matp.show()
    
    if resposta == "3":
        listatop = listarauth("1") #cria uma lista dos autores com mais publicações
        listatop20 = listatop[len(listatop)-20:len(listatop)] #escolhe os 20 autores com mais publicações
        matp.title("Distribuição de artigos por autor (Top 20)")
        matp.xlabel("Autor")
        matp.ylabel("Publicações")
        listaordenada = sorted(listatop20, key = lambda param: param[1])
        print(listaordenada)
        datas = [i[0] for i in listaordenada]
        Publicações = [int(i[1][0]) for i in listaordenada]
        matp.barh(datas, Publicações, label = "Nº de Artigos", color = "r")
        matp.legend()
        matp.show()

    if resposta == "4":
        listinha = searchPaper(4) #cria uma lista com os artigos de um autor
        listdatas = {}
        for i in listinha:
            if "publish_date" in i:
                x = i["publish_date"]
                if x[0:4] not in listdatas:
                    listdatas[x[0:4]] = 1
                else:
                    listdatas[x[0:4]] += 1
            elif "publish_date" not in i and "N/A" not in listdatas:
                listdatas["N/A"] = 1
            else:
                listdatas["N/A"] += 1
        matp.title("Distribuição de artigos por ano")
        matp.xlabel("ANOS")
        matp.ylabel("Publicações")
        listaordenada = sorted(listdatas.items(), key = lambda param: param[0])
        datas = [i[0] for i in listaordenada]
        Publicações = [int(i[1]) for i in listaordenada]
        matp.bar(datas, Publicações, label = "Nº de Artigos", color = "b")
        matp.legend()
        matp.show()

    if resposta == "5":
        listinha = listarkeywords("1")[:20] #cria uma lista das top 20 keywords em termos de utilização
        matp.title("Distribuição de ocorrências de palavras-chave")
        matp.xlabel("Palavras-chave")
        matp.ylabel("Publicações")
        listinha.reverse() #inverte o sentido da lista de keywords
        print (listinha)
        keys = [i[0] for i in listinha]
        Publicações = [int(i[1]) for i in listinha]
        matp.barh(keys, Publicações, label = "Nº de Artigos", color = "b")
        matp.legend()
        matp.show()

    if resposta == "6":
        listapares = {}
        for i in Paper_file:
            if "publish_date" in i:
                x = i["publish_date"]
                year = x[0:4]
            else:
                year = "N/A"
            if year not in listapares:
                listapares[year] = {}
            if "keywords" in i:
                for n in i["keywords"].split(","):
                    n = n.strip()
                    if n not in listapares[year]:
                        listapares[year][n] = 1
                    else:
                        listapares[year][n] += 1
        listaanos = {}
        for ano, keywords in listapares.items():
            if len(keywords) > 0:
                listaordenada = sorted(keywords.items(), key=lambda param: param[1], reverse=True)
                listaanos[ano] = [listaordenada[0]]
                listaanos2 = sorted(listaanos.items(), key=lambda param: param[0], reverse=True)
        for i in listaanos2:
            print (i)

######################################################################### COMMAND LINE INTERFACE #############################################################################################

def CLI():
    level = (-1)
    while level != ('0'):
        print("""Menu de Utilizador
        [1] Carregar Base de Dados
        [2] Adicionar Publicação    
        [3] Pesquisar Publicação
        [4] Análise de Palavras-Chave
        [5] Guardar base de Dados
        [6] Editar Publicação
        [7] Eliminar Publicação
        [8] Listar Autores
        [9] Estatísticas
        [0] Sair  
        [H] Ajuda""")

        level = input("Escolha a opção: ")
        if level == '1':
            nome = input("Insira o nome do ficheiro que pretende carregar: ")
            save_on_exit()
            carregaFicheiro(nome)
        elif level == '2':
            abstract=input("Escreva o abstrato do artigo: ")
            keywords=input("Escreva as palavras-chave do artigo (separadas por vírgulas): ")
            autores=[]
            nomeautor = "abc"
            aux = 1
            print("Para interromper a introdução de mais autores, definir nome de novo autor como 0.")
            while nomeautor[0] != "0":
                nomeautor = input(f"Inserir o nome do autor {aux}: ")
                afiliação = input(f"Inserir a afiliação do autor {aux}: ")
                orcid = input(f"Inserir o orcid do autor {aux}:")
                if nomeautor[0] == 0 and aux == 1:
                    print("O artigo tem de ter pelo menos um autor.")
                    nomeautor = "abc"
                elif nomeautor[0] == "0" and aux != 1:
                    aux += 1
                else:
                    autores.append({"name": nomeautor, "affiliation": afiliação, "orcid": orcid})
                    aux += 1
            link1=input("Insira o link para o DOI do artigo: ")
            pdf=input("Insira o link para um ficheiro pdf do artigo: ")
            data=input("Escreva a data de publicação do artigo (YYYY-MM-DD): ")
            title=input("Escreva o título do artigo: ")
            link2=input("Insira o link para o artigo: ")
            insPaper(abstract, keywords, autores, link1, pdf, data, title, link2)
        elif level == '3':
            print("""Menu de Pesquisa
        [1] Pesquisar por título
        [2] Pesquisar por palavras-chave
        [3] Pesquisar por data
        [4] Pesquisar por autor
        [5] Pesquisar por afiliação""")
            resposta = int(input("Que opção pretende tomar: "))
            aux = searchPaper(resposta)
            print(aux)
        elif level == '4':
            resposta = input('''Pretende ordenar os resultados:
        [1] Por ordem decrescente de ocorrências
        [2] Por ordem crescente alfabética  ''')
            if resposta == '1' or '2':
                print(listarkeywords(resposta))
            else:
                print(f'Input {resposta} inválido')
        elif level == '5':
            nome = input("Escreva o nome do ficheiro que vai guardar: ")
            guardaFicheiro(f"{nome}.json", Paper_file)
        elif level == '6':        
            titulo = searchPaper(1)[0]["title"]
            title = input("Deseja alterar o título do artigo? s/n: ")
            abstract = input("Deseja alterar o abstrato do artigo? s/n: ")
            keywords = input("Deseja alterar as palavras-chave do artigo? s/n: ")
            authors = input("Deseja alterar os autores do artigo? s/n: ")
            data = input("Deseja alterar a data do artigo? s/n: ")
            editarPaper(titulo, title, abstract, keywords, authors, data)
        elif level == '7':
            titulo = input("Escreva o titulo do artigo que vai eliminar: ")
            if eliminar_publicacao(titulo):
                print(f"""O artigo "{titulo}" foi eliminado.""")
            else:
                print(f"""O artigo "{titulo}" não foi encontrado.""")
        elif level == '8':
            print(listarauth('1'))
        elif level == '9':
            graph()
        elif level == '0':
            save_on_exit()
        elif level == 'H':
            print('''LISTA DE COMANDOS DISPONÍVEIS:
        [Carregar Base de Dados] - Permite a importação de um DataSet, sobrepondo-se ao antigo, se xistente, e guardando todas as alterações efetuadas
        [Adicionar Publicação] - Permite a adição de uma publicação no DataSet atual, sendo necessário preencher todos os campos   
        [Pesquisar Publicação] - Retorna um grupo de todas as publicações que conteem um certo elemento (keyword, autor, etc.)
        [Análise de Palavras-Chave] - Retorna uma lista de todas as palavras-chave no DataSet, podendo ser ordenada por ordem alfabética ou número de ocorrências
        [Guardar base de Dados] - Permite guardar a base de dados, num documento com o nome do documento carregado, sobrepondo-se a este se ainda existir
        [Editar Publicação] - Permite a pesquisa de uma publicação específica, e a alteração dos seus parâmetros
        [Eliminar Publicação] - Permite eliminar uma publicação específica do DataSet
        [Listar Autores] -  Retorna uma lista de todos os autores, o número de artigos que publicaram, e os seus títulos
        [Estatísticas] - Permite a visualização de gráficos para compreensão estatística do DataSet
        [Sair] - Fecha o programa, guardando todas as alterações efetuadas ao DataSet, da mesma forma que "Guardar base de Dados" \n ''')
        else:
            print(f'Input "{level}" inválido.')


############################################################################### VISUAL INTERFACE ##########################################################################################

class SistemaPubs:
    #Sistema principal para gestão de publicações científicas
    def __init__(self):
        self.publicacoes = []
        self.ficheiro_padrao = "ata_medica_papers.json"
        self.carregar_base_dados()

    def carregar_base_dados(self, nome_ficheiro: str = None) -> bool:
        #Carrega a base de dados do ficheiro JSON
        try:
            with open(nome_ficheiro or self.ficheiro_padrao, 'r', encoding='utf-8') as f:
                self.publicacoes = json.load(f)
            print(f"Base de dados carregada com sucesso!")
            return True
        except FileNotFoundError:
            print(f"Ficheiro não encontrado.")
            return False
        except json.JSONDecodeError:
            print(f"Erro na formatação do ficheiro JSON.")
            return False

    def guardar_base_dados(self, nome_ficheiro: str = None) -> bool:
        #Guarda a base de dados num ficheiro JSON
        try:
            with open(nome_ficheiro or self.ficheiro_padrao, 'w', encoding='utf-8') as f:
                json.dump(self.publicacoes, f, ensure_ascii=False, indent=4)
            print(f"Base de dados guardada com sucesso!")
            return True
        except Exception as e:
            print(f"Erro ao guardar a base de dados: {e}")
            return False

    def criar_publicacao(self, dados: Dict) -> bool:
        #Cria uma nova publicação na base de dados
        try:
            # Validação básica dos dados
            campos_obrigatorios = ['title', 'abstract', 'keywords', 'authors', 'doi', 'pdf', 'publish_date', 'url']
            if not all(campo in dados for campo in campos_obrigatorios):
                print("Dados incompletos para criar publicação")
                return False
            
            # Validação dos autores
            for autor in dados['authors']:
                if not all(campo in autor for campo in ['name', 'affiliation', 'orcid']):
                    print("Dados de autor incompletos")
                    return False

            self.publicacoes.append(dados)
            return True
        except Exception as e:
            print(f"Erro ao criar publicação: {e}")
            return False

    def editarPaper(self, titulo, title, abstract, keywords, authors, data): #função de edição de artigos
        for i in self.publicacoes:
            if i["title"] == titulo: #verifica se cada artigo é o que se pretende alterar
                artigo = i
        if title == "s": #se o utilizador quiser alterar o titulo escreve "s"
            title = input("Qual deve ser o novo título?")
            self.publicacoes[self.publicacoes.index(artigo)]["title"] = title
        if abstract == "s": #se o utilizador quiser alterar a sinpose escreve "s"
            abstract = input("Qual deve ser a nova sinpose?")
            self.publicacoes[self.publicacoes.index(artigo)]["abstract"] = abstract
        if keywords == "s": #se o utilizador quiser alterar as palavras-chave escreve "s"
            keywords = input("Quais devem ser as novas palavras-chave?")
            self.publicacoes[self.publicacoes.index(artigo)]["keywords"] = keywords
        if authors == "s": #se o utilizador quiser alterar os autores escreve "s"
            resposta = input("Deseja adicionar, remover, ou editar algum autor? (a/r/e)")
            if resposta == "a": #se o utilizador quiser adicionar um autor escreve "a"
                numauth = int(input("Quantos autores quer adicionar?"))
                while numauth > 0: #conta o número de autores que já foram adicionados
                    autor = input("Nomeie um autor")
                    afiliação = input("Qual a afiliação desse autor?")
                    pessoa = {"name" : autor,
                            "affiliation" : afiliação} #cria um dicionário com toda a informação relevante a um autor
                    numauth -= 1
                    self.publicacoes[self.publicacoes.index(artigo)]["authors"].append(pessoa) #insere o autor no artigo
            elif resposta == "r": #se o utilizador quiser remover um autor escreve "r"
                print(self.publicacoes[self.publicacoes.index(artigo)]["authors"]) #mostra ao utilizador os autores no artigo
                removido = int(input("Qual o número do autor que pretende remover? (1-x)"))
                self.publicacoes[self.publicacoes.index(artigo)]["authors"].remove(self.publicacoes[self.publicacoes.index(artigo)]["authors"][removido - 1]) #remove o autor escolhido pelo utilizador
            elif resposta == "e": #se o utilizador quiser editar um autor escreve "e"
                print(self.publicacoes[self.publicacoes.index(artigo)]["authors"])
                alterado = int(input("qual o número do autor que pretende alterar? (1-x)"))
                modo = input("Pretende alterar o nome, a afiliação, ou ambos? (1,2,3)") 
                if modo == "1":  #se o utilizador quiser alterar o nome do autor
                    novonome = input("Escolha um novo nome!")
                    self.publicacoes[self.publicacoes.index(artigo)]["authors"][alterado - 1]["name"] = novonome
                elif modo == "2":  #se o utilizador quiser alterar a afiliação do autor
                    novaafiliacao = input("Escolha uma nova afiliação!")
                    self.publicacoes[self.publicacoes.index(artigo)]["authors"][alterado - 1]["affiliation"] = novaafiliacao
                elif modo == "3":  #se o utilizador quiser alterar o nome e afiliação do autor
                    novonome = input("Escolha um novo nome!")
                    self.publicacoes[self.publicacoes.index(artigo)]["authors"][alterado - 1]["name"] = novonome
                    novaafiliacao = input("Escolha uma nova afiliação!")
                    self.publicacoes[self.publicacoes.index(artigo)]["authors"][alterado - 1]["affiliation"] = novaafiliacao
        if data == "s": #se o utilizador quiser alterar a data de publicação escreve "s"
            data = input("Qual deve ser a nova data de publicação?")
            self.publicacoes[self.publicacoes.index(artigo)]["publish_date"] = data

        return f"Processo concluido com sucesso: {self.publicacoes[self.publicacoes.index(artigo)]}"
    
    def searchSpecific(self,title):
        try:
            for artigo in self.publicacoes:
                if 'title' in artigo:
                    if artigo['title'] == title:
                        return artigo
            print('Artigo não encontrado!')
            return {}
        except Exception as e:
            print(f"Erro ao eliminar publicação: {e}")
            return {}
        
    def eliminar_publicacao(self, titulo: str) -> bool:
        #Elimina uma publicação da base de dados
        try:
            for pub in self.publicacoes:
                if pub['title'] == titulo:
                    self.publicacoes.remove(pub)
                    return True
            return False
        except Exception as e:
            print(f"Erro ao eliminar publicação: {e}")
            return False


    def eliminar_publicacao_interface(self):
        layout_search = [
            [sg.Text('Pesquisar por:')],
            [sg.Radio('Título', 'SEARCH', key='titulo', default=True),
            sg.Radio('Autor', 'SEARCH', key='autor'),
            sg.Radio('Afiliação', 'SEARCH', key='afiliacao'),
            sg.Radio('Data', 'SEARCH', key='data'),
            sg.Radio('Keywords', 'SEARCH', key='keywords')],
            [sg.Text('Termo de pesquisa:'), sg.Input(key='search_term')],
            [sg.Button('Pesquisar',button_color=('white', '#2B5B84')), sg.Button('Cancelar',button_color=('white', '#2B5B84'))]
        ]
        
        window_search = sg.Window('Pesquisar Publicação para Eliminar', layout_search, location=(None, None), resizable=True, finalize=True)
        window_search.set_min_size((400, 150))
        
        while True:
            event, values = window_search.read()
            
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window_search.close()
                return
                
            if event == 'Pesquisar':
                criterio = next(k for k, v in values.items() if v and k in ['titulo', 'autor', 'afiliacao', 'data', 'keywords'])
                resultados = self.pesquisar_publicacoes(criterio, values['search_term'])
                
                if not resultados:
                    sg.popup('Nenhuma publicação encontrada!')
                    continue
                    
                layout_results = [[sg.Text('Publicações Encontradas:', font=('Helvetica', 12, 'bold'))]]
                for pub in resultados:
                    title_text = f"Título: {pub['title']}\nAutores: {', '.join(a['name'] for a in pub['authors'])}"
                    layout_results.append([
                        sg.Multiline(title_text, size=(50, 2), disabled=True),
                        sg.Button('Eliminar', key=f"DEL_{pub['title']}",button_color=('white', '#2B5B84'))
                    ])
                layout_results.append([sg.Button('Fechar',button_color=('white', '#2B5B84'))])
                
                scrollable_layout = [[sg.Column(layout_results, scrollable=True, vertical_scroll_only=True, size=(600, 400))]]
                
                window_results = sg.Window('Resultados da Pesquisa', 
                                        scrollable_layout, 
                                        location=(None, None),
                                        resizable=True,
                                        finalize=True)
                window_results.set_min_size((650, 450))
                
                loop = True
                while loop:
                    event_res, _ = window_results.read()
                    if event_res is None or event_res in (sg.WIN_CLOSED, 'Fechar'):
                        window_results.close()
                        loop = False
                        
                    elif event_res.startswith('DEL_'):
                        title = event_res[4:]
                        if sg.popup_yes_no('Tem certeza que deseja eliminar esta publicação?') == 'Yes':
                            if self.eliminar_publicacao(title):
                                sg.popup('Publicação eliminada com sucesso!')
                                window_results.close()
                                loop = False
                            else:
                                sg.popup('Erro ao eliminar publicação!')
                
                window_results.close()
        
            window_search.close()

    def pesquisar_publicacoes(self, criterio, valor) -> List[Dict]:
        #Pesquisa publicações por diferentes critérios
        resultados = []
        try:
            if criterio == "titulo":
                for i in self.publicacoes:
                    if "title" in i: #verifica se o artigo tem título
                        if valor in i["title"] :
                            resultados.append(i)
            elif criterio == "autor":
                for i in self.publicacoes:     
                    for x in i["authors"]: 
                        if "name" in x: #verifica se o autor tem nome
                            if x["name"] == valor:
                                resultados.append(i)
            elif criterio == "afiliacao":
                for i in self.publicacoes:
                    for x in i["authors"]:
                        if "affiliation" in x: #verifica se o autor tem afiliação
                            if x["affiliation"] == valor:
                                resultados.append(i)
            elif criterio == "data":
                for i in self.publicacoes:  
                    if "publish_date" in i: #verifica se o artigo tem data de publicação
                        if valor in i["publish_date"]: 
                            resultados.append(i)
            elif criterio == "keywords":
                for i in self.publicacoes:
                    keywords = i.get('keywords', '').strip()
                    keywords_list = [k.strip() for k in keywords.split(',') if k.strip()]
                    if valor in keywords_list:
                        resultados.append(i)
            return resultados
        except Exception as e:
            print(f"Erro na pesquisa: {e}")
            return []

    def ordenar_resultados(self, resultados: List[Dict], criterio: str) -> List[Dict]:
        #Ordena os resultados por título ou data
        try:
            if criterio == "titulo":
                return sorted(resultados, key=lambda x: x['title'])
            elif criterio == "data":
                return sorted(resultados, key=lambda x: x['publish_date'])
            return resultados
        except Exception as e:
            print(f"Erro ao ordenar resultados: {e}")
            return resultados

    def analisar_autores(self, ordenacao) -> List[tuple]:
        contagem_autores = {}
        try:
            for pub in self.publicacoes:
                # Verifica se 'authors' existe e é uma lista
                if 'authors' in pub and isinstance(pub['authors'], list):
                    for autor in pub['authors']:
                        if isinstance(autor, dict) and 'name' in autor:
                            nome = autor['name']
                            if nome not in contagem_autores:
                                contagem_autores[nome] = {'Ocorrências': 1, 'Artigos': [pub['title']]}
                            else:
                                contagem_autores[nome]['Ocorrências'] += 1
                                contagem_autores[nome]['Artigos'].append(pub['title'])
                else:
                    print(f"Formato inválido em 'authors': {pub.get('authors')}")

            # Ordena conforme solicitado
            if ordenacao == "alfabetica":
                return sorted(contagem_autores.items())
            elif ordenacao == "frequencia":
                return sorted(contagem_autores.items(), 
                            key=lambda x: x[1]['Ocorrências'], 
                            reverse=True)
        except Exception as e:
            print(f"Erro na análise de autores: {e}")
            return []



    def analisar_keywords(self, ordenacao) -> List[tuple]:
        #Análise de palavras-chave e suas ocorrências
        listkeys = {}
        for i in self.publicacoes:
            if "keywords" in i:
                for x in i["keywords"].split(","): #prepara os dados para análise, cada vírgula representa uma separação nas keywords
                    x = x.strip() #retira espaços em branco no início e no fim das palavras-chave, para " criança" e "criança" não serem contadas como variáveis diferentes
                    if x not in listkeys: #verifica se a keyword já foi adicionada à lista
                        listkeys[str(x)] = {"Ocorrências" : 1,
                                            "Artigos" : [i["title"]]} #cria um novo dicionário dentro de listkeys, que tem o nome da keyword atual, e define o número de ocorrências como 1, adicionando o artigo presente à lista de artigos
                    else:
                        listkeys[str(x)]["Ocorrências"] += 1 #+1 ao número de ocorrências da keyword
                        listkeys[str(x)]["Artigos"].append(i["title"]) #adiciona o titulo do artigo a lista de artigos desta keyword
        
            # Ordena conforme solicitado
        if ordenacao == "alfabetica":
            return sorted(listkeys.items(), key=lambda x: x[0])
        elif ordenacao == "frequencia":  # frequencia
            return sorted(listkeys.items(), 
                        key=lambda x: x[1]['Ocorrências'], 
                        reverse=True)


    def graph(self, tipo, escolha: str = None):
        if tipo == "1":
            listdatas = {}
            for i in self.publicacoes:
                if "publish_date" in i:
                    x = i["publish_date"] #x= YYYY/MM/DD
                    if x[0:4] not in listdatas: #verifica se o ano em que o artigo foi publicado já existe em listadatas
                        listdatas[x[0:4]] = 1 #cria uma constante (x[0:4]) e dá-lhe o valor de 1
                    else:
                        listdatas[x[0:4]] += 1 #+1 para o número de ocorrências de artigos num ano, se o ano já existir na lista
                elif "publish_date" not in i and "N/A" not in listdatas: #se o artigo não tiver data, e se ainda não houver uma constante de data indefinida em listadatas, cria essa constante e dá-lhe o valor de 1
                    listdatas["N/A"] = 1
                else:
                    listdatas["N/A"] += 1 #+1 para "N/A"
            matp.title("Distribuição de artigos por ano") #define titulo do grafico
            matp.xlabel("ANOS") #define nome da abcissa
            matp.ylabel("Publicações") #define nome da ordenada
            listaordenada = sorted(listdatas.items(), key = lambda param: param[0]) #ordena a lista de datas, de acordo com o número de publicações por ano (menor->maior)
            datas = [i[0] for i in listaordenada] #cria um alista apenas com os anos, já ordenados
            Publicações = [int(i[1]) for i in listaordenada] #cria uma lista, apenas com as ocorrências, já ordenadas
            matp.bar(datas, Publicações, label = "Nº de Artigos", color = "b") #define x = datas, y = Publicações, nome da variável = "Nº de Artigos", cor do grafico = blue, identificador de dados = círculo ("o")
            matp.legend() #ativa a legenda (nome da variável)
            matp.show() #ativa o gráfico

        if tipo == "2":
            listdatas = {}
            for i in self.publicacoes:
                if "publish_date" in i:
                    x = i["publish_date"] #x= YYYY/MM/DD
                    if x[0:4] == escolha and x[5:7] not in listdatas: #verifica se o mês em que o artigo foi publicado já existe em listadatas e se o artigo pertence ao ano correto
                        listdatas[x[5:7]] = 1
                    elif x[0:4] == escolha:
                        listdatas[x[5:7]] += 1
            if listdatas == []:
                return False
            matp.title("Distribuição de artigos num ano")
            matp.xlabel("MESES")
            matp.ylabel("Publicações")
            listaordenada = sorted(listdatas.items(), key = lambda param: param[0])
            autores = [i[0] for i in listaordenada]
            Publicações = [int(i[1]) for i in listaordenada]
            matp.bar(autores, Publicações, label = "Nº de Artigos", color = "r") #cor do grafico = "red"
            matp.legend()
            matp.show()
        
        if tipo == "3":
            listatop = self.analisar_autores("frequencia") #cria uma lista dos autores com mais publicações
            listatop20 = listatop[:20] #escolhe os 20 autores com mais publicações
            listatop20.reverse()
            matp.title("Distribuição de artigos por autor (Top 20)")
            matp.xlabel("Autor")
            matp.ylabel("Publicações")
            datas = [i[0] for i in listatop20]
            Publicações = [int(i[1]['Ocorrências']) for i in listatop20]
            matp.barh(datas, Publicações, label = "Nº de Artigos", color = "r")
            matp.legend()
            matp.show()

        if tipo == "4":
            listinha = self.pesquisar_publicacoes('autor',escolha) #cria uma lista com os artigos de um autor
            listdatas = {}
            for i in listinha:
                if "publish_date" in i:
                    x = i["publish_date"]
                    if x[0:4] not in listdatas:
                        listdatas[x[0:4]] = 1
                    else:
                        listdatas[x[0:4]] += 1
                elif "publish_date" not in i and "N/A" not in listdatas:
                    listdatas["N/A"] = 1
                else:
                    listdatas["N/A"] += 1
            matp.title("Distribuição de artigos por ano")
            matp.xlabel("ANOS")
            matp.ylabel("Publicações")
            listaordenada = sorted(listdatas.items(), key = lambda param: param[0])
            datas = [i[0] for i in listaordenada]
            Publicações = [int(i[1]) for i in listaordenada]
            matp.bar(datas, Publicações, label = "Nº de Artigos", color = "b")
            matp.legend()
            matp.show()

        if tipo == "5":
            listinha = self.analisar_keywords("frequencia")[:20]#cria uma lista das top 20 keywords em termos de utilização
            matp.title("Distribuição de ocorrências de palavras-chave")
            matp.xlabel("Palavras-chave")
            matp.ylabel("Publicações")
            listinha.reverse() #inverte o sentido da lista de keywords
            keys = [i[0] for i in listinha]
            Publicações = [int(i[1]['Ocorrências']) for i in listinha]
            matp.barh(keys, Publicações, label = "Nº de Artigos", color = "b")
            matp.legend()
            matp.show()

        if tipo == "6":
            listapares = {}
            for i in self.publicacoes:
                if "publish_date" in i:
                    x = i["publish_date"]
                    year = x[0:4]
                else:
                    year = "N/A"
                if year not in listapares:
                    listapares[year] = {}
                if "keywords" in i:
                    for n in i["keywords"].split(","):
                        n = n.strip()
                        if n not in listapares[year]:
                            listapares[year][n] = 1
                        else:
                            listapares[year][n] += 1
            listaanos = {}
            for ano, keywords in listapares.items():
                if len(keywords) > 0:
                    listaordenada = sorted(keywords.items(), key=lambda param: param[1], reverse=True)
                    listaanos[ano] = [listaordenada[0]]
                    listaanos2 = sorted(listaanos.items(), key=lambda param: param[0], reverse=True)
            for i in listaanos2:
                print (i)
            matp.title("Top 20 Palavras-chave")
            matp.xlabel("Anos")
            matp.ylabel("Palavras-chave")
            anos = [int(i[0]) for i in listaanos2]
            keys = [i[1][0][0] for i in listaanos2]
            matp.plot(anos, keys, label = "Nº de Artigos", color = "b", marker = 'o')
            matp.legend()
            matp.show()
            return listaanos2

    def exportar_resultados(self, resultados: List[Dict], nome_ficheiro: str) -> bool:
        #Exporta resultados de pesquisa para um ficheiro
        try:
            with open(nome_ficheiro, 'w', encoding='utf-8') as f:
                json.dump(resultados, f, ensure_ascii=False, indent=4)
            print(f"Resultados exportados com sucesso para {nome_ficheiro}")
            return True
        except Exception as e:
            print(f"Erro ao exportar resultados: {e}")
            return False

def criar_interface_grafica():
    sg.theme('LightGrey1')
    
    title_font = ('Helvetica', 24, 'bold')
    button_font = ('Helvetica', 12, 'bold')
    padding = (10, 10)
    button_size = (25, 2)
    
    title_section = [
        [sg.Text('Sistema de Gestão de Publicações Científicas', 
                font=title_font, 
                justification='center', 
                pad=((0, 0), (20, 30)))]
    ]
    
    data_section = [
        [sg.Button('Carregar Base de Dados', 
                  size=button_size, 
                  font=button_font, 
                  pad=padding,
                  button_color=('white', '#2B5B84')),
         sg.Button('Guardar Base de Dados', 
                  size=button_size, 
                  font=button_font, 
                  pad=padding,
                  button_color=('white', '#2B5B84'))]
    ]
    
    manage_section = [
        [sg.Button('Adicionar Publicação', 
                  size=button_size, 
                  font=button_font, 
                  pad=padding,
                  button_color=('white', '#2B5B84')),
         sg.Button('Editar Publicação', 
                  size=button_size, 
                  font=button_font, 
                  pad=padding,
                  button_color=('white', '#2B5B84'))]
    ]
    
    search_section = [
        [sg.Button('Pesquisar Publicações', 
                  size=button_size, 
                  font=button_font, 
                  pad=padding,
                  button_color=('white', '#2B5B84')),
         sg.Button('Listar Autores', 
                  size=button_size, 
                  font=button_font, 
                  pad=padding,
                  button_color=('white', '#2B5B84'))]
    ]
    
    analysis_section = [
        [sg.Button('Análise de Keywords', 
                  size=button_size, 
                  font=button_font, 
                  pad=padding,
                  button_color=('white', '#2B5B84')),
         sg.Button('Estatísticas', 
                  size=button_size, 
                  font=button_font, 
                  pad=padding,
                  button_color=('white', '#2B5B84'))]
    ]
    
    action_section = [
        [sg.Button('Eliminar Publicação', 
                  size=button_size, 
                  font=button_font, 
                  pad=padding,
                  button_color=('white', '#2B5B84')),
         sg.Button('Sair', 
                  size=button_size, 
                  font=button_font, 
                  pad=padding,
                  button_color=('white', '#2B5B84'))]
    ]
    
    layout = [
        [sg.Column(title_section, element_justification='center', expand_x=True)],
        [sg.HorizontalSeparator(pad=((0, 0), (0, 20)))],
        [sg.Text(size = (6,2)),sg.Column(data_section, element_justification='center', expand_x=True), sg.Button('?', size = (4,2), auto_size_button=True, font = ('Helvetica', 12, 'bold'), button_color=('white', '#2B5B84'))],
        [sg.Column(manage_section, element_justification='center', expand_x=True)],
        [sg.Column(search_section, element_justification='center', expand_x=True)],
        [sg.Column(analysis_section, element_justification='center', expand_x=True)],
        [sg.Column(action_section, element_justification='center', expand_x=True)]
    ]
    
    window = sg.Window('Sistema de Publicações', 
                      layout,
                      finalize=True,
                      size=(800, 600),
                      resizable=False,
                      element_justification='center')
    window.set_min_size((700, 500))
    
    return window

def Visual():
    #Função principal que inicia o sistema
    sistema = SistemaPubs()
    window = criar_interface_grafica()
    loop_main = True
    
    while loop_main:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Sair':
            sistema.guardar_base_dados()
            loop_main = False

        if event == 'Carregar Base de Dados':
            layout = [
                [sg.Text("Carregar Ficheiro")],
                [sg.Input(key='Nome do ficheiro a carregar:', enable_events=True),
                 sg.FileBrowse('Procurar', file_types=(("JSON Files", "*.json"), ("Text Files", "*.txt"), ("All Files", "*.*")), 
                             button_color=('white', '#2B5B84'))],
                [sg.Button('Carregar', button_color=('white', '#2B5B84'), bind_return_key=True), 
                 sg.Button('Cancelar', button_color=('white', '#2B5B84'))]
            ]

            janela_load = sg.Window('Carregar Publicação', layout)
            loop_aux = True
            while loop_aux:
                evento_load, valores = janela_load.read()
                if evento_load in (sg.WIN_CLOSED, 'Cancelar'):
                    janela_load.close()
                    loop_aux = False
                elif evento_load == "Carregar":
                    fnome = valores['Nome do ficheiro a carregar:']
                    if fnome: 
                        if sistema.carregar_base_dados(fnome):
                            sg.popup("Base de dados carregada com sucesso!", title="Sucesso")
                            janela_load.close()
                            loop_aux = False
                        else:
                            sg.popup("Erro ao carregar a base de dados.", title="Erro")
                    else:
                        sg.popup("Por favor, selecione um arquivo.", title="Aviso")
        
        elif event == 'Guardar Base de Dados':
            if sistema.guardar_base_dados():
                sg.popup("Base de dados guardada com sucesso!", title="Sucesso")
            else:
                sg.popup("Erro ao guardar a base de dados.", title="Erro")
        
        elif event == 'Adicionar Publicação':
            layout = [
                [sg.Text('Título:', font=('Helvetica',12,'bold')), sg.Input(key='titulo',size=(20,8),expand_x=True)],
                [sg.Text('Resumo:', font=('Helvetica',12,'bold')), sg.Multiline(key='abstract',size=(20,5),expand_x=True)],
                [sg.Text('Palavras-chave\n (separadas por vírgula):', font=('Helvetica',12,'bold')), sg.Input(key='keywords',size=(20,8),expand_x=True)],
                [sg.Text('Autores (JSON, \n ex: [{"name": "Autor", \n "affiliation": "Univ",\n "orcid": "0000"}]):', font=('Helvetica',12,'bold')), sg.Multiline(key='authors',size=(20,5),expand_x=True)],
                [sg.Text('DOI:', font=('Helvetica',12,'bold')), sg.Input(key='doi',size=(20,8),expand_x=True)],
                [sg.Text('PDF URL:', font=('Helvetica',12,'bold')), sg.Input(key='pdf',size=(20,8),expand_x=True)],
                [sg.Text('Data de Publicação\n (YYYY-MM-DD):', font=('Helvetica',12,'bold')), sg.Input(key='publish_date',size=(20,8),expand_x=True)],
                [sg.Text('URL do Artigo:', font=('Helvetica',12,'bold')), sg.Input(key='url',size=(20,8),expand_x=True)],
                [sg.Button('Adicionar',button_color=('white', '#2B5B84')), sg.Button('Cancelar',button_color=('white', '#2B5B84'))]
            ]
            janela_add = sg.Window('Adicionar Publicação', layout, finalize=True, size=(800,430))
            evento_add, valores_add = janela_add.read()
            loop_aux = True
            while loop_aux:
                if evento_add == (sg.WINDOW_CLOSED or 'Cancelar'):
                    janela_add.close()
                    loop_aux = False
                if evento_add == 'Adicionar':
                    try:
                        # Validação e conversão dos dados
                        autores = json.loads(valores_add['authors'])  # Tenta converter autores para JSON
                        if not isinstance(autores, list):
                            raise ValueError("Autores devem ser uma lista de objetos JSON.")
                        
                        dados = {
                            'title': valores_add['titulo'],
                            'abstract': valores_add['abstract'],
                            'keywords': valores_add['keywords'],
                            'authors': autores,
                            'doi': valores_add['doi'],
                            'pdf': valores_add['pdf'],
                            'publish_date': valores_add['publish_date'],
                            'url': valores_add['url']
                        }

                        # Tenta criar a publicação
                        if sistema.criar_publicacao(dados):
                            sg.popup("Publicação adicionada com sucesso!", title="Sucesso")
                            loop_aux = False
                        else:
                            sg.popup("Erro ao adicionar publicação. Verifique os dados.", title="Erro")
                            loop_aux = False
                    except json.JSONDecodeError:
                        sg.popup("Formato inválido para os autores. Insira um JSON válido.", title="Erro")
                        loop_aux = False
                    except ValueError as ve:
                        sg.popup(str(ve), title="Erro")
                        loop_aux = False
                    except Exception as e:
                        sg.popup(f"Erro inesperado: {e}", title="Erro")
                        loop_aux = False
                janela_add.close()
        
        elif event == 'Editar Publicação':
            layout_search = [
                [sg.Text('Pesquisar por:')],
                [sg.Radio('Título', 'SEARCH', key='titulo', default=True),
                sg.Radio('Autor', 'SEARCH', key='autor'),
                sg.Radio('Afiliação', 'SEARCH', key='afiliacao'),
                sg.Radio('Data', 'SEARCH', key='data'),
                sg.Radio('Keywords', 'SEARCH', key='keywords')],
                [sg.Text('Termo de pesquisa:'), sg.Input(key='search_term')],
                [sg.Button('Pesquisar', button_color=('white', '#2B5B84'), bind_return_key=True),
                sg.Button('Cancelar', button_color=('white', '#2B5B84'))]
            ]

            window_search = sg.Window('Pesquisar Publicação para Editar', layout_search, location=(None, None), resizable=True, finalize=True)
            window_search.set_min_size((400, 150))
            loop_2 = True
            while loop_2:
                event, values = window_search.read()
                
                if event in (sg.WIN_CLOSED, 'Cancelar'):
                    window_search.close()
                    loop_2 = False
                    
                if event == 'Pesquisar' and values['search_term']:
                    criterio = next(k for k, v in values.items() if v and k in ['titulo', 'autor', 'afiliacao', 'data', 'keywords'])
                    resultados = sistema.pesquisar_publicacoes(criterio, values['search_term'])
                
                    if not resultados:
                        sg.popup('Nenhuma publicação encontrada!')
                        continue
                    
                    layout_results = [[sg.Text('Publicações Encontradas:', font=('Helvetica', 12, 'bold'))]]
                    for pub in resultados:
                        title_text = f"Título: {pub['title']}\nAutores: {', '.join(a['name'] for a in pub['authors'])}"
                        layout_results.append([
                            sg.Multiline(title_text, size=(50, 2), disabled=True),
                            sg.Button('Editar', key=f"EDIT_{pub['title']}",button_color=('white', '#2B5B84'))
                        ])
                    layout_results.append([sg.Button('Fechar',button_color=('white', '#2B5B84'))])
                    
                    scrollable_layout = [[sg.Column(layout_results, scrollable=True, vertical_scroll_only=True, size=(600, 400))]]
                    
                    window_results = sg.Window('Resultados da Pesquisa', 
                                            scrollable_layout, 
                                            location=(None, None),
                                            resizable=True,
                                            finalize=True)
                    window_results.set_min_size((650, 450))
                    
                    loop = True
                    while loop:
                        event_res, _ = window_results.read()
                        if event_res is None or event_res == 'Fechar':
                            window_results.close()
                            loop = False
                            continue
                            
                        if event_res.startswith('EDIT_'):
                            title = event_res[5:]
                            artigo = sistema.pesquisar_publicacoes('titulo',title)

                            if artigo != {}:
                                layout_editar = []
                                layout_editar.append([sg.Text()])

                                
                                for chave, valor in artigo[0].items():
                                    layout_editar.append([
                                        sg.Text(f'{chave.upper()}:', size=(10, 1), font=('Helvetica', 20, 'bold'), justification='left'),
                                        sg.Multiline(default_text=str(valor), size=(182, 6), expand_x=True, key=f'input_{chave}'), sg.Stretch()
                                    ])

                                

                                layout_editar.append([sg.Text()])
                                layout_editar.append([sg.Button('Confirmar', size=(15,1), font=('Helvetica',12,'bold'),button_color=('white', '#2B5B84')), 
                                                sg.Button('Cancelar', size=(15,1), font=('Helvetica',12,'bold'),button_color=('white', '#2B5B84'))])

                                scrollable_layout = [[sg.Column(layout_editar, scrollable=True, vertical_scroll_only=True, size=(2000, 1000))]]
                                janela_edit_2 = sg.Window('Editar Publicação', scrollable_layout, finalize=True, resizable=True)
                                janela_edit_2.Maximize()
                                loop_aux = True
                                while loop_aux:
                                    evento_edit_2, valores_edit_2 = janela_edit_2.read()
                                    if evento_edit_2 in (sg.WIN_CLOSED, 'Cancelar'):
                                        janela_edit_2.close()
                                        loop_aux = False
                                    elif evento_edit_2 == 'Confirmar':
                                        
                                        for chave in artigo[0].keys():
                                            input_key = f'input_{chave}'
                                            if input_key in valores_edit_2:
                                                artigo[0][chave] = valores_edit_2[input_key].strip()
                                        
                                        sg.popup("Alterações salvas com sucesso!", title="Sucesso")
                                        janela_edit_2.close()
                                        loop_aux = False
                                
                            else:
                                sg.popup('Artigo não encontrado!')
                                
                    
                    window_results.close()
            
                window_search.close()   

           

        elif event == 'Pesquisar Publicações':
            resultados = {}
            layout_pesq = [
                [sg.Text('Critério de Pesquisa:'), sg.Combo(['titulo', 'autor', 'afiliacao', 'data', 'keywords'], key='criterio')],
                [sg.Text('Valor:'), sg.Input(key='valor')],
                [sg.Button('Pesquisar',button_color=('white', '#2B5B84'),bind_return_key=True), sg.Button('Cancelar',button_color=('white', '#2B5B84'))]
            ]
            janela_pesq = sg.Window('Pesquisar Publicações', layout_pesq)
            loop_aux = True
            while loop_aux:
                evento_pesq, valores_pesq = janela_pesq.read()
                if evento_pesq in (sg.WIN_CLOSED, 'Cancelar'):  # Encerrar a janela
                    janela_pesq.close()
                    loop_aux = False

                if evento_pesq == 'Pesquisar':
                    # Realiza a pesquisa
                    resultados = sistema.pesquisar_publicacoes(valores_pesq['criterio'], valores_pesq['valor'])

                    if not resultados:
                        sg.popup('Artigo não encontrado!')
    
                    if resultados:
                        # Exibe os resultados
                        layout_resultados = [
                            [sg.Text('Resultados da Pesquisa:')],
                            [sg.Multiline(json.dumps(resultados, ensure_ascii=False, indent=4), size=(60, 20), disabled=True,expand_x=True,expand_y=True)],
                            [sg.Button('Exportar Resultados',button_color=('white', '#2B5B84')), sg.Button('Fechar',button_color=('white', '#2B5B84'))]
                        ]
                        janela_resultados = sg.Window('Resultados de Pesquisa', layout_resultados, finalize=True)
                        janela_resultados.Maximize()
                        janela_pesq.close()
                        while loop_aux:
                            evento_res, _ = janela_resultados.read()
                            if evento_res in (sg.WIN_CLOSED, 'Fechar'):
                                janela_resultados.close()
                                loop_aux = False

                            if evento_res == 'Exportar Resultados':
                                # Pergunta se deseja exportar
                                layout_exportar = [
                                    [sg.Text('Nome do arquivo para exportar os resultados:')],
                                    [sg.Input(key='fnome'), sg.FileSaveAs(file_types=(("JSON Files", "*.json"),))],
                                    [sg.Button('Exportar',button_color=('white', '#2B5B84')), sg.Button('Cancelar',button_color=('white', '#2B5B84'))]
                                ]
                                janela_exportar = sg.Window('Exportar Resultados', layout_exportar)

                                evento_exp, valores_exp = janela_exportar.read()
                                if evento_exp in (sg.WIN_CLOSED, 'Cancelar'):
                                    janela_exportar.close()
                                    continue

                                if evento_exp == 'Exportar':
                                    # Exporta os resultados para o arquivo especificado
                                    nome_arquivo = valores_exp.get('fnome', '').strip()
                                    if nome_arquivo:
                                        try:
                                            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                                                json.dump(resultados, f, ensure_ascii=False, indent=4)
                                            sg.popup("Resultados exportados com sucesso!", title="Sucesso")
                                        except Exception as e:
                                            sg.popup(f"Erro ao exportar resultados: {e}", title="Erro")
                                    else:
                                        sg.popup("Por favor, insira um nome de arquivo válido.", title="Erro")
                                    janela_exportar.close()

            janela_pesq.close()


        elif event == 'Listar Autores':
            layout = [
                [sg.Text("Escolha o método de ordenação:")],
                [sg.Button("Ordenar por ordem alfabética",button_color=('white', '#2B5B84')), sg.Button("Ordenar por número de ocorrências",button_color=('white', '#2B5B84')), sg.Button("Cancelar",button_color=('white', '#2B5B84'))]
            ]
            janela_auth = sg.Window('Análise de Autores', layout)
            loop_aux = True
            while loop_aux:
                evento_auth, _ = janela_auth.read()
                if evento_auth in (sg.WIN_CLOSED, 'Cancelar'):  # Trata fechamento ou cancelamento
                    janela_auth.close()
                    loop_aux = False
                elif evento_auth == 'Ordenar por ordem alfabética':
                    analise_auth = sistema.analisar_autores("alfabetica")
                    sg.popup_scrolled(
                        json.dumps(analise_auth, ensure_ascii=False, indent=4),
                        title="Análise de Autores - Ordem Alfabética"
                    )
                elif evento_auth == 'Ordenar por número de ocorrências':
                    analise_auth = sistema.analisar_autores("frequencia")
                    sg.popup_scrolled(
                        json.dumps(analise_auth, ensure_ascii=False, indent=4),
                        title="Análise de Autores - Número de Ocorrências"
                    )
            janela_auth.close()
            
        
        elif event == 'Análise de Keywords':
            layout = [
                [sg.Text("Escolha o método de ordenação:")],
                [sg.Button("Ordenar por ordem alfabética",button_color=('white', '#2B5B84')), sg.Button("Ordenar por número de ocorrências",button_color=('white', '#2B5B84')), sg.Button("Cancelar",button_color=('white', '#2B5B84'))]
            ]
            janela_keys = sg.Window('Análise de Palavras-Chave', layout)
            loop_aux = True
            while loop_aux:
                evento_keys, _ = janela_keys.read()
                if evento_keys in (sg.WIN_CLOSED, 'Cancelar'):  # Trata fechamento ou cancelamento
                    janela_keys.close()
                    loop_aux = False
                elif evento_keys == 'Ordenar por ordem alfabética':
                    analise_keywords = sistema.analisar_keywords("alfabetica")
                    sg.popup_scrolled(
                        json.dumps(analise_keywords, ensure_ascii=False, indent=4),
                        title="Análise de Keywords - Ordem Alfabética"
                    )
                elif evento_keys == 'Ordenar por número de ocorrências':
                    analise_keywords = sistema.analisar_keywords("frequencia")
                    sg.popup_scrolled(
                        json.dumps(analise_keywords, ensure_ascii=False, indent=4),
                        title="Análise de Keywords - Número de Ocorrências"
                    )
            janela_keys.close()
        
        elif event == 'Estatísticas':
            layout = [
                [sg.Text('Tipo de Estatística:')],
                [sg.Button('Publicações por ano',button_color=('white', '#2B5B84')), sg.Button('Publicações por mês, num ano',button_color=('white', '#2B5B84'))],
                [sg.Button('Top 20 autores',button_color=('white', '#2B5B84')), sg.Button('Publicações de um autor',button_color=('white', '#2B5B84'))],
                [sg.Button('Top 20 keywords',button_color=('white', '#2B5B84')), sg.Button('Keywords por ano',button_color=('white', '#2B5B84'))],
                [sg.Button('Cancelar',button_color=('white', '#2B5B84'))]
            ]
            janela_est = sg.Window('Gerar Estatísticas', layout)
            estatisticas_ativas = True
            
            while estatisticas_ativas:
                evento_est, valores_est = janela_est.read()
                
                if evento_est in (sg.WIN_CLOSED, 'Cancelar'):
                    estatisticas_ativas = False
                    
                elif evento_est == 'Publicações por ano':
                    sistema.graph("1")
                    estatisticas_ativas = False
                    
                elif evento_est == 'Publicações por mês, num ano':
                    
                    anos = set()
                    for pub in sistema.publicacoes:
                        if 'publish_date' in pub:
                            anos.add(str(pub['publish_date'][0:4]))
                    anos = sorted(list(anos))
                    
                    layout = [
                        [sg.Text('Selecione o ano:'),
                         sg.Combo(anos, default_value=anos[0] if anos else '', key='ano', 
                                readonly=True, size=(20,1))],
                        [sg.Button('Visualizar',button_color=('white', '#2B5B84')), 
                         sg.Button('Cancelar',button_color=('white', '#2B5B84'))]
                    ]
                    janela_stat = sg.Window('Estatísticas', layout)
                    stat_ativo = True
                    
                    while stat_ativo:
                        evento_stat, valor_stat = janela_stat.read()
                        
                        if evento_stat in (sg.WIN_CLOSED, 'Cancelar'):
                            stat_ativo = False
                        elif evento_stat == 'Visualizar':
                            sistema.graph('2', valor_stat['ano'])
                            stat_ativo = False
                    
                    janela_stat.close()
                    estatisticas_ativas = False
                    
                elif evento_est == 'Top 20 autores':
                    sistema.graph('3')
                    estatisticas_ativas = False
                    
                elif evento_est == 'Publicações de um autor':
                    layout = [
                        [sg.Text('Autor que deseja visualizar:'),sg.Input(key = 'autor')],
                        [sg.Button('Visualizar',button_color=('white', '#2B5B84')), sg.Button('Cancelar',button_color=('white', '#2B5B84'))]
                    ]
                    janela_stat = sg.Window('Estatísticas', layout)
                    stat_ativo = True
                    
                    while stat_ativo:
                        evento_stat, valor_stat = janela_stat.read()
                        
                        if evento_stat in (sg.WIN_CLOSED, 'Cancelar'):
                            stat_ativo = False
                        elif evento_stat == 'Visualizar':
                            sistema.graph('4', valor_stat['autor'])
                            stat_ativo = False
                    
                    janela_stat.close()
                    estatisticas_ativas = False
                    
                elif evento_est == 'Top 20 keywords':
                    sistema.graph('5')
                    estatisticas_ativas = False
                    
                elif evento_est == 'Keywords por ano':
                    sistema.graph('6')
                    
            
            janela_est.close()

        elif event == 'Eliminar Publicação':
            sistema.eliminar_publicacao_interface()
        
        elif event == '?':
            sg.popup('''LISTA DE COMANDOS DISPONÍVEIS: \n
        [Carregar Base de Dados] - Permite a importação de um DataSet, sobrepondo-se ao antigo, se xistente, e guardando todas as alterações efetuadas \n
        [Adicionar Publicação] - Permite a adição de uma publicação no DataSet atual, sendo necessário preencher todos os campos \n
        [Pesquisar Publicação] - Retorna um grupo de todas as publicações que conteem um certo elemento (keyword, autor, etc.) \n
        [Análise de Palavras-Chave] - Retorna uma lista de todas as palavras-chave no DataSet, podendo ser ordenada por ordem alfabética ou número de ocorrências \n
        [Guardar base de Dados] - Permite guardar a base de dados, num documento com o nome do documento carregado, sobrepondo-se a este se ainda existir \n
        [Editar Publicação] - Permite a pesquisa de uma publicação específica, e a alteração dos seus parâmetros \n
        [Eliminar Publicação] - Permite eliminar uma publicação específica do DataSet \n
        [Listar Autores] -  Retorna uma lista de todos os autores, o número de artigos que publicaram, e os seus títulos \n
        [Estatísticas] - Permite a visualização de gráficos para compreensão estatística do DataSet \n
        [Sair] - Fecha o programa, guardando todas as alterações efetuadas ao DataSet, da mesma forma que "Guardar base de Dados" ''')
    
    window.close()

############################################################################# MASTER ###############################################################################################################


def init():
    sg.theme('LightGrey1')  # Modern, clean theme
    
    title_font = ('Helvetica', 24, 'bold')
    button_font = ('Helvetica', 12, 'bold')
    padding = (10, 10)
    button_size = (25, 2)

    title_section = [
        [sg.Text('Sistema de Gestão de Publicações Científicas', 
                font=title_font, 
                justification='center', 
                pad=((0, 0), (20, 30)))]
    ]
    
    choice_section = [
        [sg.Button('Visual Interface', 
                  size=button_size, 
                  font=button_font, 
                  pad=padding,
                  button_color=('white', '#2B5B84')),
         sg.Button('Command Line Interface', 
                  size=button_size, 
                  font=button_font, 
                  pad=padding,
                  button_color=('white', '#2B5B84'))]
    ]

    layout = [[sg.Column(title_section, element_justification='center', expand_x=True)],
        [sg.HorizontalSeparator(pad=((0, 0), (0, 20)))],
        [sg.Column(choice_section, element_justification='center', expand_x=True)],
        [sg.Button('Cancelar', size=button_size, font=button_font, pad=padding, button_color=('white', '#2B5B84'))]]
    window = sg.Window('Sistema de Gestão de Publicações Científicas', layout, finalize = True, size=(740,300), element_justification='center')
    window.set_min_size((740, 300))
    
    return window

def main():
    init_window = init()
    loop_main = True

    while loop_main:
        event, values = init_window.read()
        
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            loop_main = False
        elif event == 'Visual Interface': 
            init_window.close()
            Visual()
            loop_main = False
        elif event == 'Command Line Interface':
            init_window.close()
            CLI()
            loop_main = False

if __name__ == "__main__":
    main()

