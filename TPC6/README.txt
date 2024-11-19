TPC6
Gestão de Turmas e Alunos

Este TPC consiste na gestão de várias turmas, cada uma delas com um nome e vários alunos, em que cada aluno tem um nome, ID escolar, e notas de TPCs, Projetos, e Testes.

Para este TPC foram utilizados dicionários na construção de alunos, turmas, e listas de alunos e turmas. Para execução de muitas das funções, foram utilizadas as funcionalidades de "keys" dos dicionários para fins de organização e acesso de dados. Note-se que o programa está otimizado para utilização com ficheiros .txt, em vez de .json, que seriam mais eficientes e necessitariam de menos complexidade nos algoritmos que dizem respeito à criação e acesso de ficheiros.

Neste TPC, é apresentado um menu com várias funcionalidades:

1)Adicionar turma
2)Adicionar aluno
3)Adicionar aluno a turma
4)Ver alunos numa turma
5)Procurar aluno por ID
6)Guardar turma
7)Carregar turma
0)Sair

1- Cria uma turma, adicionando-a à lista de turmas

2- Cria um aluno, adicionando-o à lista de alunos

3- Adiciona um aluno a uma turma, utilizando a informação acerca desse aluno guardada na lista de alunos, acedendo aos seus dados com a key correspondente ao seu nome

4- Devolve uma lista de todos os alunos numa turma, bem como as suas informações, no formato [nome, ID, nota TPC, nota Projeto, nota Teste]

5- Procura na lista de alunos por um aluno cujo ID corresponda ao dado

6- Guarda a turma num formato facilmente acessível e fácil de ler, num formato .txt

7- Carrega uma turma, a partir de um ficheiro local, e armazenando-a nas variáveis locais

0- Sai do programa

