#TPC6


listaTurmas = {}

listaAlunos = {}



def criarTurma(nomeTurma):
    nome = nomeTurma
    if nome not in listaTurmas:
        nomeTurma = {"nome.turma": nome,
                    "alunos": [] }
        listaTurmas[nome] = nomeTurma
        return "Turma criada com sucesso!"
    else:
        return "Essa turma já existe!"

def criarAluno(nomeAluno,id,TPC,Proj,Teste):
    nome = nomeAluno
    if nome not in listaAlunos:
        nomeAluno = {"nome.aluno": nome,
                    "id": id,
                    "nota.TPC": TPC,
                    "nota.Projeto": Proj,
                    "nota.Teste": Teste}
        listaAlunos[nome] = nomeAluno
        return "Aluno criado com sucesso!"
    else:
        return "Esse aluno já existe!"
    
def inserirAluno(turma,aluno):
    if turma in listaTurmas:
        if aluno in listaAlunos:
            if aluno not in listaTurmas[turma]:
                listaTurmas[turma]["alunos"].append(listaAlunos[aluno])
                return "Aluno adicionado com sucesso!"
        else:
            return "Esse aluno não existe!"
    else:
        return "Essa turma não existe!"
    
def listarTurma(turma):
    if turma in listaTurmas:
        turmaSimplificada = []
        for aluno in listaTurmas[turma]["alunos"]:
            nome = aluno["nome.aluno"]
            id_aluno = aluno["id"]
            notas = [aluno["nota.TPC"], aluno["nota.Projeto"], aluno["nota.Teste"]]
            turmaSimplificada.append([nome, id_aluno, notas])
            
        return turmaSimplificada
    else:
        return "Essa turma não existe!"
    
def consultarID(id):
    for aluno in listaAlunos:
        if listaAlunos[aluno]["id"] == id:
            return listaAlunos[aluno]
    return "Esse aluno não existe!"

def guardarTurma(turma):
    if turma in listaTurmas:
        with open(f"{turma}.txt", "w") as file:
            file.write(f"Turma: {turma}\n")
            for aluno_key in listaTurmas[turma]["alunos"]:
                aluno_nome = aluno_key["nome.aluno"]
                aluno = listaAlunos[aluno_nome]
                file.write(f"{aluno["nome.aluno"]},{aluno["id"]},{aluno["nota.TPC"]},{aluno["nota.Projeto"]},{aluno["nota.Teste"]}\n")
                
        return f"Turma '{turma}' guardada com sucesso!"
    else:
        return "Essa turma não existe!"
    
def carregarTurma(turma):
    try:
        with open(f"{turma}.txt", "r") as file:
            linhas = file.readlines()
        if not linhas[0].startswith("Turma:"):
            return "Formato inválido no arquivo da turma!"
        nomeTurma = linhas[0].strip().split(": ")[1]
        listaTurmas[nomeTurma] = {"nome.turma": nomeTurma,
                                   "alunos": []}
        
        for linha in linhas[1:]:
            nome, id, tpc, proj, teste = linha.strip().split(",")
            criarAluno(nome, id, tpc, proj, teste)
            inserirAluno(turma,nome)
        return f"Turma '{nomeTurma}' carregada com sucesso!"
    except FileNotFoundError:
        return "O arquivo da turma não foi encontrado!"
    except Exception as erro:
        return f"Ocorreu um erro ao carregar a turma: {erro}" 

    

Logout = False

while Logout == False:
    
    print (f"""Olá!
Escolha um modo de utilização!
       
1)Adicionar turma
2)Adicionar aluno
3)Adicionar aluno a turma
4)Ver alunos numa turma
5)Procurar aluno por ID
6)Guardar turma
7)Carregar turma
0)Sair""")
    
    resposta = input()


    if resposta == "1":
        nomeTurma = input("Escolha um nome para a nova turma!")
        print(criarTurma(nomeTurma))

    elif resposta == "2":
        nomeAluno = input("Escolha um nome para o novo aluno!")
        id = input("Escolha um novo id!")
        TPC = input("Introduza a nota de TPC!")
        Proj = input("Introduza a nota de Projeto!")
        Teste = input("Introduza a nota de Teste!")
        print (criarAluno(nomeAluno,id,TPC,Proj,Teste))

    elif resposta == "3":
        turma = input("Escolha uma turma para adicionar!")
        aluno = input("Escolha um aluno para adicionar!")
        print (inserirAluno(turma,aluno))

    elif resposta == "4":
        turma = input("Escolha uma turma para ver!")
        print (listarTurma(turma))

    elif resposta == "5":
        id = input("Escolha um ID para procurar!")
        print (consultarID(id))

    elif resposta == "6":
        turma = input("Escolha uma turma para guardar!")
        print (guardarTurma(turma))
    
    elif resposta == "7":
        turma = input("Escolha uma turma para carregar!")
        print (carregarTurma(turma))
        
    elif resposta == "0":
        print ("Ok, adeus!")
        Logout = True