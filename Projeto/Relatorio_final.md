![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZiDv_Bcm27tWtBE42HS24Pp8niBqAjtG0wg&s)
# <span style="font-family: 'Georgia', serif;">Relatório do Projeto do Sistema de Consulta e Análise de Publicações Científicas</span>
---
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<span style="font-family: 'Georgia', serif; font-size: 16px;">**Grupo:**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Docentes:**
<br>

<span style="font-family: 'Georgia', serif; font-size: 16px;">Afonso Trindade, A107204&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;José Carlos Ramalho  
<span style="font-family: 'Georgia', serif; font-size: 16px;">Pedro Lousinha, A107197&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Luis Filipe Cunha  
<span style="font-family: 'Georgia', serif; font-size: 16px;">Duarte Franco, A107233 <br>
<br>
<br>
<br>
## <span style="font-family: 'Georgia', serif; font-size: 20px;">Introdução</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Este projeto consistiu no desenvolvimento de uma aplicação que visa Consulta e Análise de Publicações Científicas.</span>  </p> <br>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O sistema permite o carregamento da base de dados, criação de publicações, atualização de publicações, consulta de publicações, análise de publicações por autor, análise de publicações por palavras-chave, armazenamento dos dados, importação de dados e exportação parcial de dados.  O sistema apresenta relatórios que incluem gráficos da distribuição de publicações por ano, publicações por mês de um determinado ano, número de publicações por autor (top 20 autores), publicações de um autor por anos, palavras-chave pela sua frequência (top 20 palavras-chave) e palavras-chave mais frequente por ano.</span>
</p><br>
<span style="font-family: 'Georgia', serif; font-size: 20px; font-weight: bold">Análise e Requisitos</span><br>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Inicialmente, começou-se por analisar o problema proposto. Foi sugerida a criação de uma aplicação na qual fosse possível consultar, introduzir e alterar conteúdo numa base de dados fornecida, com uma estrutura definida. Assim, o primeiro passo foi o desenvolvimento de uma interface gráfica funcional que permitisse cumprir todos os requisitos.</span> </p> <br>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Para  se aceder às informações contidas na base de dados, é necessário introduzir o nome do ficheiro de texto com formato json já existente, havendo uma tentativa inicial de importar um ficheiro <em>“ata_medica_papers.json”</em>. A partir daí são apresentadas várias opções: <strong>“Carregar Base de Dados”</strong>, que permite ao usuário a importação de um ficheiro json, para manipulação através da interface, e <strong>“Guardar Base de Dados”</strong>, que permite a exportação de uma qualquer base de dados, num formato json, salvando quaisquer alterações efetuadas.</span> </p> <br>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Outras opções são ainda <strong>“Adicionar Publicação”</strong> e <strong>“Editar Publicação”</strong>, que permitem, respetivamente, criar uma entrada no DataSet atual conforme alguns critérios específicos, e editar qualquer entrada no documento.</span> </p> <br>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;"><strong>“Pesquisar Publicações”</strong>, <strong>“Listar Autores”</strong> e <strong>“Análise de Keywords”</strong> permitem uma compreensão geral da estrutura e conteudo do DataSet, dando a possibilidade de pesquisar por publicações segundo vários critérios, e listar autores e palavras-chave de cada entrada, para obter uma visão geral da informação no documento.</span> </p> <br>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;"><strong>“Estatísticas”</strong> permite a visualização, em gráficos, de vários aspetos do documento (Palavras-chave mais mencionadas, autores com mais publicações, etc.) de uma forma mais intuitiva e lúdica.</span> </p> <br>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;"><strong>“Eliminar Publicação”</strong> cria a possibilidade para remoção de entradas no DataSet.</span> </p> <br>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;"><strong>“Sair”</strong> é a opção final da interface visual, fechando a interface e guardando quaisquer alterações feitas ao documento, se algum tiver sido carregado.</span> </p> <br>

## <span style="font-family: 'Georgia', serif; font-size: 20px;">Estrutura de dados</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Para ser possível o desenvolvimento do algoritmo, foi necessário definir a estrutura de dados adequada para o trabalho. Este passo é essencial na criação de uma linha de raciocínio para a definição das funções que constituem o código.</span> </p> <br>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Deste modo, a base de dados é definida por uma lista de dicionários, em que cada um corresponde a uma publicação. Por sua vez, cada publicação inclui "keys". Cada publicação é constituída por título, resumo, palavras-chave, autores, DOI, PDF, data de publicação e URL. Já os autores, são constituídos por uma lista de dicionários, onde cada dicionário contém informações sobre nome, afiliação e ORCID.</span> </p> <br>


[![amostra-base-de-dados.png](https://i.postimg.cc/Xv2FWxML/amostra-base-de-dados.png)](https://postimg.cc/Lq1hBt8g)
<span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 1. Amostra da base de dados *ata_medica_papers.json*
<br>
<br>
<br>
<br>

## <span style="font-family: 'Georgia', serif; font-size: 20px;">Conceção do Algoritmo</span>
### <span style="font-family: 'Georgia', serif; font-size: 18px;">Bibliotecas</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O primeiro passo consistiu na importação de módulos necessários para o desenvolvimento do código. Foram importados módulos em json e os, para além de módulos necessários para a criação de gráficos, criação de uma janela e manipulação de datas.</span> </p> <br>
* <span style="font-family: 'Georgia', serif; font-size: 16px;"><strong>import matplotlib.pyplot as matp</strong>: importa a biblioteca Matplotlib, que é usada para criar gráficos e visualizações em Python;</span>

* <span style="font-family: 'Georgia', serif; font-size: 16px;">**import json**: converte dicionários e listas Python em strings JSON, como o dataset se encontrava guardado em um ficheiro JSON, esta biblioteca foi usada para conseguir ler e escrever os dados das publicações;</span>

* <span style="font-family: 'Georgia', serif; font-size: 16px;">**import os**: permite aceder a funcionalidades dependentes do Sistema Operativo.</span>

* <span style="font-family: 'Georgia', serif; font-size: 16px;">**import PySimpleGUI as sg** : ajuda na criação de um layout de GUI (interface gráfica), janela, texto e botões, com Python;</span>

* <span style="font-family: 'Georgia', serif; font-size: 16px;">**from typing import Dict, List**: importa os tipos Dict (dicionário) e List (lista) do módulo typing;</span> <br>

### <span style="font-family: 'Georgia', serif; font-size: 18px;">Linha de comandos</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Este é um programa em Python que realiza operações de gestão de tarefas através da linha de comandos. Começa-se por importar as bibliotecas necessárias, como ‘od‘, ‘json‘ e ‘matplotlib.pyplot as matp’.</span> </p> <br>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">De seguida, inicializamos com <strong>Paper_file</strong> como uma lista vazia. Já a função <strong>clear_console()</strong> tem como objetivo limpar o ecrã do terminal onde o script está a ser executado. Este verifica o sistema operacional com a expressão os.name, e dependendo do sistema, executa um comando específico para limpar o ecrã: no Windows, usa os.system('cls') e, em sistemas Unix-like (como Linux e macOS), usa os.system('clear'). <br>
Em seguida, várias funções são definidas para executar operações específicas, como: </span> </p> <br>

#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Menu principal</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Ao selecionar a opção <strong>"Command Line Interface"</strong>, surge no terminal do VS Code um menu principal que apresenta todas as opções disponíveis. Essas opções, exigem que o utilizador introduza a opção correspondente à tarefa desejada. Caso selecione a opção <strong>’Visual Interface’</strong> abrirá a interface, que vai ser abordada mais à frente.</span> </p>  <br>

[![menu-inicial.png](https://i.postimg.cc/nc7KZmGm/menu-inicial.png)](https://postimg.cc/hfDQ1fw4)
<span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 2. Interface inicial </span>

#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Carregar Base de Dados</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa deve ser capaz de carregar para a memória interna o conjunto de dados presente num ficheiro com a seguinte estrutura:</span> </p> <br>


```py
[
    {
        "abstract": "Resumo do conteúdo da publicação",
        "keywords": "Palavras-chave relacionadas com a publicação",
        "authors": [
            {
                "name": "Nome do autor", 
                "affiliation": "Nome da afiliação do autor",
                "orcid": "Identificador aberto de investigador e contribuidor"
                
            }
        ],
        "doi": "Identificador do objeto digital",
        "pdf": "Caminho do ficheiro PDF da publicação",
        "publish_date": "Data da publicação (AAAA-MM-DD)",
        "title": "Título da publicação",
        "url": "Endereço web da publicação"
    }
]
```
<br>
<span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 3. Estrutura das publicações</span>
<br>

#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Criar Publicações</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa deve permitir que o utilizador crie uma nova publicação, especificando título, resumo, palavras-chave, DOI, autores (com nome, afiliação e ORCID), caminho para o PDF, data da publicação e URL da publicação.</span> </p>

#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Atualizar Publicações</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa deve permitir que o utilizador atualize as informações de uma dada publicação. Estas informações incluem título, resumo, palavras-chave, autores (nome, afiliação e ORCID), DOI, caminho para o PDF, data da publicação e URL da publicação.</span> </p>

#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Consultar Publicações</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa deve permitir que o utilizador consulte as publicações através de filtros por título, autor, afiliação, data de publicação e palavras-chave. Após encontrar as publicações, deve ser possível ordená-las pelos títulos ou pelas datas de publicação.</span> </p>

#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Analisar Publicações por Autor</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa deve listar os autores, permitindo ao utilizador visualizar as publicações correspondentes a um
dado autor. Esta listagem deve ser ordenada pela frequência de publicações e/ou por ordem alfabética.</span> </p>



[![Menu analizar autores.png](https://i.postimg.cc/zD0k9y9q/image.png)](https://postimg.cc/PNvZD5X7) <br>
<span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 4. Menu de consulta de autores



#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Analisar Publicações por Palavras-Chave</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa deve permitir a visualização das palavras-chave existentes no conjunto de dados, possibilitando que o utilizador visualize as publicações correspondentes a uma dada palavra-chave. As palavras-chave devem ser ordenadas pela sua frequência e/ou por ordem alfabética.</span> </p>




[![image.png](https://i.postimg.cc/SxZg0DjQ/image.png)](https://postimg.cc/JskNZ3bS) <br>
<span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 5. Menu de Análise de Publicações por Palavras-Chave


#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Estatísticas das Publicações</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa deve exibir estatísticas referentes às publicações presentes no conjunto de dados, apresentando gráficos para os seguintes tópicos:</span> </p>
<span style="font-family: 'Georgia', serif; font-size: 16px;">
* Distribuição de publicações por ano. <br>
* Distribuição de publicações por mês de um determinado ano. <br>
* Número de publicações por autor (top 20 autores). <br>
* Distribuição de publicações de um autor por anos. <br>
* Distribuição de palavras-chave pela sua frequência (top 20 palavras-chave). <br>
* Distribuição de palavras-chave mais frequentes por ano.</span> <br>




[![estat-sticas-linha-comandos.png](https://i.postimg.cc/7YfCsh3G/estat-sticas-linha-comandos.png)](https://postimg.cc/RNxVqMb4) <br>
<span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 6. Menu de Estatísticas das Publicações




#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Armazenamento dos Dados</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa deve guardar as informações alteradas ou adicionadas em memória no ficheiro de suporte.</span> </p>

#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Importação de Dados</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa deve permitir que, a qualquer momento, seja possível importar novos registros de outro conjunto de dados com a mesma estrutura mencionada anteriormente.</span> </p>

#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Exportação Parcial de Dados</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa deve permitir exportar os registos resultantes de uma pesquisa para um ficheiro.</span> </p>

### <span style="font-family: 'Georgia', serif; font-size: 18px;">Interface gráfica</span>

#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Carregar Base de dados</span>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">De acordo com os requisitos estabelecidos no enunciado, a funcionalidade de carregamento da base de dados (BD) a partir de um arquivo de texto, com extensão JSON, é fundamental para a operação do sistema.</span> </p>




[![menu-carregar-base-de-dados.png](https://i.postimg.cc/NM81wvcH/menu-carregar-base-de-dados.png)](https://postimg.cc/R6F3c8qS)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 7. Menu da IG para carregar um *data-set*</span>


<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Ao acionar o botão <strong>"Carregar Base de Dados"</strong> na interface principal, será aberta uma nova janela solicitando ao usuário que procure no seu Browser a base de dados que deseja utilizar, sendo esta de formato, obrigatoriamente, JSON. A leitura e carregamento desses dados ocorrerão em seguida.
É crucial ressaltar que o botão <strong>"Carregar"</strong> permanecerá inativo até que o usuário selecione um arquivo de base de dados válido.
Uma vez que a base de dados tenha sido carregada com sucesso, uma mensagem de confirmação será exibida na interface principal, garantindo ao usuário que a operação foi concluída com êxito. Esta abordagem visa assegurar a integridade e a validade dos dados utilizados pelo sistema.

#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Gravar Base de dados</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">A aplicação possibilita a gravação da base de dados utilizada, sendo este processo crucial para o pleno funcionamento das outras funcionalidades. Enquanto a base de dados não tiver sido salva, uma janela de erro é exibida na interface para lembrar o utilizador da necessidade de salvar a base de dados antes de prosseguir com as operações da aplicação.</span> </p>
<br>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Após a gravação bem-sucedida da base de dados, uma mensagem de confirmação será exibida na interface, comunicando ao utilizador que a operação foi concluída com êxito. Essa mensagem de confirmação tem o objetivo de proporcionar ao utilizador a certeza de que os dados foram salvos com sucesso e estão prontos para serem utilizados nas funcionalidades subsequentes da aplicação.
Essa abordagem visa garantir a consistência e a segurança dos dados, promovendo uma experiência de utilização mais fluida e eficiente.</span> </p>




[![msg-guardar-base-de-dados.png](https://i.postimg.cc/ncKqWDxh/msg-guardar-base-de-dados.png)](https://postimg.cc/TpwyLhhz)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 8. Mensagem de aviso da conclusão da gravação da base de dados</span>



#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Adicionar Nova Publicação</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Ao clicar no botão <strong>"Adicionar Publicação"</strong>, uma nova janela será aberta, apresentando diversos campos destinados ao preenchimento de informações relacionadas à tarefa a ser adicionada.</span> </p>




[![menu-de-adicionar-publica-o.png](https://i.postimg.cc/T1nG0xZp/menu-de-adicionar-publica-o.png)](https://postimg.cc/tnRLRKRj)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 9. Menu da IG para adicionar uma nova publicação</span>



#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Pesquisar Publicação</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">A aplicação oferece uma funcionalidade que permite a consulta de uma tarefa com base em critérios como título, autor, afiliação, data e keywords.</span> </p>




[![menu-de-pesquisa-de-publica-o.png](https://i.postimg.cc/4xkHXNJF/menu-de-pesquisa-de-publica-o.png)](https://postimg.cc/6ycp0K4d)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 10. Menu da IG para pesquisar publicação, e os critérios de pesquisa disponíveis</span>


#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Listar Autores</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa inclui uma funcionalidade de listagem de autores acessada através do botão <strong>"Listar Autores"</strong> na interface principal.
Nesta opção, é possível escolher entre diversas opções, tais como ordenar por ordem alfabética e ordenar por número de ocorrências.</span> </p>




[![menu-listar-autores.png](https://i.postimg.cc/kgHMv74v/menu-listar-autores.png)](https://postimg.cc/FYjQ950Y)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 11. Menu opções para a ordem da lista de autores </span>




#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Editar Publicação</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Para editar uma publicação, seleciona-se um critério de pesquia, e introduz-se a informação da publicação que se pretende editar.</span> </p>




[![menu editar pesquisa.png](https://i.postimg.cc/tTGJ3BcR/image.png)](https://postimg.cc/3y937F7z)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 12. Menu da IG para pesquisar publicação para editar. </span>
<br>
[![msg-publica-es-encontradas.png](https://i.postimg.cc/7LHGdsVB/msg-publica-es-encontradas.png)](https://postimg.cc/4Y0xh1jt)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 13. Menu de opção para escolher publicação para editar, caso os critérios inseridos tenham mais do que um resultado. </span>


<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Após a publicação já ter sido localizada, vai aparecer esta janela na qual lhe permitirá editar todos os parâmetros da publicação permitida.</span> </p>




[![menu-edi-o.png](https://i.postimg.cc/wjJSyzSr/menu-edi-o.png)](https://postimg.cc/75HBdFP1)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 14. Menu edição, onde o utilizador edita os parâmetros desejados </span>



#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Eliminar publicação</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa oferece uma função para eliminar tarefas. Assim , ao clicar no botão <strong>"Eliminar Publicações"</strong>, o utilizador terá de passar para um processo de pesquisa e consulta da tarefa que deseja eliminar, onde pode identificar a publicação a partir de vários parâmetros com título, autor, afiliação, data e keywords.</span> </p>




[![menu eliminar pesquisa.png](https://i.postimg.cc/5NkCYdw8/image.png)](https://postimg.cc/ZCpR2Qsq)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 15. Menu da IG para pesquisar publicação para eliminar </span>




<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Depois de identificar a tarefa desejada, o utilizador deve clicar nessa mesma tarefa para esta ser eliminada com sucesso.</span> </p>



[![image.png](https://i.postimg.cc/RZdV6cry/image.png)](https://postimg.cc/Yv4wTLCz)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 16. Menu de confirmação da eliminação do artigo </span>



#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Análise de keywords</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa inclui uma funcionalidade de listagem de autores acessada através do botão <strong>"Análise de keywords"</strong> na interface principal.
Nesta opção, é possível escolher entre diversas opções, tais como ordenar por ordem alfabética e ordenar por número de ocorrências.</span> </p>




[![menu-analise-de-keywords.png](https://i.postimg.cc/kgmLrZHP/menu-analise-de-keywords.png)](https://postimg.cc/Mv99Vsx9)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 17. Menu de opções para a ordenam das palavras-chave </span>



#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Análise Estatística</span>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Após carregar no botão <strong>“Estatísticas”</strong> irá aparecer uma nova janela em que aparecem todas as possibilidades de gráficos, sendo elas  distribuição de publicações por ano, distribuição de publicações por mês de um determinado ano, número de publicações por autor (top 20 autores), publicações de um autor por anos, palavras-chave pela sua frequência (top 20 palavras-chave) e por palavras-chave mais frequentes por ano.</span> </p>




[![image.png](https://i.postimg.cc/bvzXnM09/image.png)](https://postimg.cc/YvyyKdsv)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 18. Menu de opções a análise gráfica das estatísticas das publicações </span>



##### <span style="font-family: 'Georgia', serif; font-size: 16px;">Distribuição de publicações por ano</span></span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa é capaz de exibir um gráfico com a distribuição de publicações por ano.</span> </p>




[![Imagem-Whats-App-2025-01-06-s-00-00-29-7c9ba60c.jpg](https://i.postimg.cc/K8nn3pQf/Imagem-Whats-App-2025-01-06-s-00-00-29-7c9ba60c.jpg)](https://postimg.cc/VJkS3Rx0)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 19. Gráfico da estatística de publicações por ano </span>




##### <span style="font-family: 'Georgia', serif; font-size: 16px;">Distribuição mensal de publicações</span>
<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa é capaz de exibir um gráfico com a distribuição mensal de publicações num dado ano.</span> </p>


[![estatistica-publicacao-por-ano-menu.png](https://i.postimg.cc/d15TFz6H/estatistica-publicacao-por-ano-menu.png)](https://postimg.cc/CBfKHrWk)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 20. Menu de escolha do ano que se pretende estudar </span>
[![estatistica-publicacoes-num-ano.png](https://i.postimg.cc/KjYBgZ4h/estatistica-publicacoes-num-ano.png)](https://postimg.cc/Q9RH2Zpf)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 21. Gráfico de estatística das publicações no ano selecionado </span>



#### <span style="font-family: 'Georgia', serif; font-size: 16px;">Número de publicação por autor (Top20)</span>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa é capaz de exibir um gráfico com o número de publicações de um autor, mas apenas o Top 20</span> </p>




[![Imagem-Whats-App-2025-01-06-s-00-48-32-9bbfb721.jpg](https://i.postimg.cc/DwWHRM17/Imagem-Whats-App-2025-01-06-s-00-48-32-9bbfb721.jpg)](https://postimg.cc/Bj0mKNhz)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 22. Gráfico dos 20 autores com o maior número de publiacações </span>




##### <span style="font-family: 'Georgia', serif; font-size: 16px;">Distribuição de publicações por ano de um dado autor</span>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa é capaz de exibir um gráfico com a distribuição de publicações por ano após ser selecionado um autor específico.</span> </p>


[![estatistica-menu-selecionar-autor.png](https://i.postimg.cc/CxZ1nRN4/estatistica-menu-selecionar-autor.png)](https://postimg.cc/nXJZ6cNs)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 23. Menu de escolha do autor que se pretende estudar </span>
[![estatistica-publicacoes-de-autor.png](https://i.postimg.cc/Fz9zYGWf/estatistica-publicacoes-de-autor.png)](https://postimg.cc/N9zBV8wY)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 24. Gráfico de estatística das publicações do autor selecionado </span>


##### <span style="font-family: 'Georgia', serif; font-size: 16px;">Distribuição de palavras-chave pela sua frequência</span>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa é capaz de exibir um gráfico com a distribuição das palavras-chave pela sua frequência.</span> </p>



[![Imagem-Whats-App-2025-01-06-s-00-57-05-31e7eadc.jpg](https://i.postimg.cc/9FDLfq0p/Imagem-Whats-App-2025-01-06-s-00-57-05-31e7eadc.jpg)](https://postimg.cc/ykzmQxFg)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 25. Gráfico de distribuição das publicações ordenadas por frequência </span>




##### <span style="font-family: 'Georgia', serif; font-size: 16px;">Número de palavras-chave ao longo dos anos</span>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O programa é capaz de exibir um gráfico com o número de palavras-chave após ao longo dos anos.</span> </p>




[![Imagem-Whats-App-2025-01-06-s-00-09-33-a41d6733.jpg](https://i.postimg.cc/3wbJ8pzh/Imagem-Whats-App-2025-01-06-s-00-09-33-a41d6733.jpg)](https://postimg.cc/WDgPSD2Y)
<br> <span style="font-family: 'Georgia', serif; font-size: 13px;">Figura 26. Gráfico de distribuição da palavra-chave mais usada ao longo dos anos. </span>



## <span style="font-family: 'Georgia', serif; font-size: 20px;">Desafios e Soluções</span>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Durante o desenvolvimento do projeto, a equipa deparou-se com alguns desafios, que foram solucionados de diversas formas, recorrendo ao engenho e conhecimento dos integrantes, bem como a técnicas lecionadas no decorrer da disciplina. Alguns dos desafios foram:</span> </p>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;"><strong>Não usar ‘break’ no decorrer da interface gráfica</strong> - No sentido de não utilizar a função ‘break’ para encerramento de janelas, a equipa recorreu a elementos como ‘continue’, e loops ‘while’ recorrentes, assim como a função ‘window.close()’;</span> </p> <br>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;"><strong>Formatação da interface gráfica</strong> - Para uma melhor apresentação e capacidade intuitiva da interface gráfica, uma das necessidades seria uma boa formatação. Para isto, foi necessário implementar elementos como ‘expand_x/y = True’, ‘window.Maximize()’, e páginas “scrollable”.</span> </p><br>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;"><strong>Dificuldades em acessar e manipular a base e dados</strong> - Durante o projeto, a equipa teve de garantir que, em qualquer situação, a base de dados poderia ser corretamente manipulada, mesmo no caso de um ficheiro corrompido ou de um documento incompleto ou mal-formatado.</span> </p><br>

## <span style="font-family: 'Georgia', serif; font-size: 20px;">Conclusão</span>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">O objetivo deste projeto consistia no desenvolvimento de uma aplicação que visa gerir o sistema de gestão de publicações científicas. Consideramos ter conseguido elaborar com sucesso uma aplicação capaz de executar todos os requisitos propostos. A criação da mesma exigiu inúmeras horas de trabalho e pesquisa, exacerbadas pela existência de diversos problemas inesperados, que levaram a múltiplas tentativas-erro.</span> </p>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Apesar disso, consideramos esta aplicação funcional com uma interface de fácil uso e interpretação. Para o desenvolvimento dos algoritmos, foram essenciais todas as ferramentas adquiridas nesta UC, incluindo a manipulação de estruturas de dados e a construção de interfaces gráficas, complementadas pela pesquisa na internet para contrariar eventuais adversidades.</span> </p>

<p style="text-align: justify;">
<span style="font-family: 'Georgia', serif; font-size: 16px;">Assim, podemos concluir que este projeto se revelou extremamente útil na consolidação da matéria abordada na UC, aplicando-a num contexto mais prático e adequado ao dia-a-dia. Além disso, permitiu-nos compreender a utilidade, inter-relação e importância das ferramentas adquiridas na UC.</span> </p>