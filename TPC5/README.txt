TPC5
Gestão de Cinemas

Este TPC consiste na gestão de vários cinemas, cada um deles com um nome e várias salas, em que cada sala tem um número máximo de lugares, exibe um filme específico, tem X lugares ocupados, e tem um nome.

Para este TPC foram utilizados dicionários na construção de salas, cinemas, e listas de salas e cinemas. Para execução de muitas das funções, foram utilizadas as funcionalidades de "keys" dos dicionários para fins de organização e acesso de dados.

Neste TPC, é apresentado um menu com várias funcionalidades:

1)Listar filmes
2)Escolher lugar para ver um filme
3)Comprar bilhete para filme
4)Ver lugares de todos os filmes em exibição
5)Inserir nova sala e filme a um cinema
6)Criar cinema
7)Criar sala
0)Sair

1- procura, em todas as salas de um determinado cinema, o filme em exibição nessa sala, usando a key "filme", e juntando-os todos numa lista, que devolve

2- verifica, se num cinema, um filme em específico está disponível, e se estiver, procura saber se a sala onde este se exibirá tem um lugar livre na posição especificada, conferindo se esse lugar existe e se ainda não está ocupado

3- Compra um bilhete para um filme, num cinema, para um lugar específico, se esse lugar existir e ainda não tiver sido ocupado

4- Lista a disponibilidade de todas as salas num cinema, na estrutura [sala, filme, número de lugares livres]

5- Insere num cinema uma nova sala, com todos os dados relevantes

6- Cria um novo cinema, inserindo-o na lista de cinemas

7- Cria uma nova sala, com toda a informação relevante, inserindo-a na lista de salas

0- Sai do programa

