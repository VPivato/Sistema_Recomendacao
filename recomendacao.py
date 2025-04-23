from math import sqrt

# Base de dados
avaliacoes_usuario = {'Ana':
                  {'Freddy x Jason': 2.5,
                   'O Ultimato Bourne': 3.5,
                   'Star Trek': 3.0,
                   'Exterminador do Futuro': 3.5,
                   'Norbit': 2.5,
                   'Star Wars': 3.0},

              'Marcos':
                  {'Freddy x Jason': 3.0,
                   'O Ultimato Bourne': 3.5,
                   'Star Trek': 1.5,
                   'Exterminador do Futuro': 5.0,
                   'Star Wars': 3.0,
                   'Norbit': 3.5},

              'Pedro':
                  {'Freddy x Jason': 2.5,
                   'O Ultimato Bourne': 3.0,
                   'Exterminador do Futuro': 3.5,
                   'Star Wars': 4.0},

              'Claudia':
                  {'O Ultimato Bourne': 3.5,
                   'Star Trek': 3.0,
                   'Star Wars': 4.5,
                   'Exterminador do Futuro': 4.0,
                   'Norbit': 2.5},

              'Adriano':
                  {'Freddy x Jason': 3.0,
                   'O Ultimato Bourne': 4.0,
                   'Star Trek': 2.0,
                   'Exterminador do Futuro': 3.0,
                   'Star Wars': 3.0,
                   'Norbit': 2.0},

              'Janaina':
                  {'Freddy x Jason': 3.0,
                   'O Ultimato Bourne': 4.0,
                   'Star Wars': 3.0,
                   'Exterminador do Futuro': 5.0,
                   'Norbit': 3.5},

              'Leonardo':
                  {'O Ultimato Bourne': 4.5,
                   'Norbit': 1.0,
                   'Exterminador do Futuro': 4.0}
              }

# Base de dados invertida
avaliacoes_filme = {'Freddy x Jason':
                  {'Ana': 2.5,
                   'Marcos:': 3.0,
                   'Pedro': 2.5,
                   'Adriano': 3.0,
                   'Janaina': 3.0},

              'O Ultimato Bourne':
                  {'Ana': 3.5,
                   'Marcos': 3.5,
                   'Pedro': 3.0,
                   'Claudia': 3.5,
                   'Adriano': 4.0,
                   'Janaina': 4.0,
                   'Leonardo': 4.5},

              'Star Trek':
                  {'Ana': 3.0,
                   'Marcos:': 1.5,
                   'Claudia': 3.0,
                   'Adriano': 2.0},

              'Exterminador do Futuro':
                  {'Ana': 3.5,
                   'Marcos:': 5.0,
                   'Pedro': 3.5,
                   'Claudia': 4.0,
                   'Adriano': 3.0,
                   'Janaina': 5.0,
                   'Leonardo': 4.0},

              'Norbit':
                  {'Ana': 2.5,
                   'Marcos:': 3.0,
                   'Claudia': 2.5,
                   'Adriano': 2.0,
                   'Janaina': 3.5,
                   'Leonardo': 1.0},

              'Star Wars':
                  {'Ana': 3.0,
                   'Marcos:': 3.5,
                   'Pedro': 4.0,
                   'Claudia': 4.5,
                   'Adriano': 3.0,
                   'Janaina': 3.0}
              }

# Minha modificação sobre a função apresentada no curso, achei mais legível
def distancia_euclidiana(base_de_dados, usuario1, usuario2):
    filmes_em_comum = []
    somatorio = 0

    for filme in base_de_dados[usuario1]: # Itera entre todos os filmes assistidos pelo usuario1
        if filme in base_de_dados[usuario2]: # Se usuario2 também assistiu ao mesmo filme
            filmes_em_comum.append(filme) # Adiciona à lista "filmes em comum"
            somatorio += pow(base_de_dados[usuario1][filme] - base_de_dados[usuario2][filme], 2) # Cálculo do somatório da diferença ao quadrado

    if len(filmes_em_comum) == 0: # Se não existem filmes em comum
        return 0 # Retorna 0 (%) de semelhança

    return 1 / (1 + sqrt(somatorio)) # Termina o cálculo da D.E. e transforma em % (0-1)



# ↓ Solução apresentada no curso (faz uso de list comprehension)
# ↓ Achei o cálculo do somatório extremamente ilegível
# ↓ Por isso optei pela versão acima. O resultado é o mesmo
def euclidiana(base_de_dados, usuario1, usuario2):
    filmes_em_comum = []

    for filme in base_de_dados[usuario1]:  # Itera entre todos os filmes assistidos pelo usuario1
        if filme in base_de_dados[usuario2]:  # Se usuario2 também assistiu ao mesmo filme
            filmes_em_comum.append(filme)  # Adiciona à lista "filmes em comum"

    if len(filmes_em_comum) == 0:  # Se não existem filmes em comum
        return 0  # Retorna 0 (%) de semelhança

    # Calcula o somatório para fazer a D.E.
    soma = sum([pow(base_de_dados[usuario1][item] - base_de_dados[usuario2][item], 2) for item in base_de_dados[usuario1] if item in base_de_dados[usuario2]])
    return 1 / (1 + sqrt(soma)) # Termina o cálculo da D.E. e transforma em % (0-1)



# Retorna uma lista dos usuários similares no formato [(similaridade0-1, usuario)] em relação a um determinado usuário alvo
def get_similares(base_de_dados, usuario):
    similares = [(distancia_euclidiana(base_de_dados, usuario, outro), outro) # Adiciona à lista um item no formato [(similaridade0-1, nome)]
                 for outro in base_de_dados if outro != usuario] # Para cada usuario que não seja ele mesmo
    similares.sort() # Ordena a lista em ordem crescente
    similares.reverse() # Inverte para ordem decrescente
    return similares[0:30] # Retorna apenas os trinta primeiros valores (base do movielens tem mais de 100k)



# Retorna uma lista dos filmes que determinado usuário alvo NÃO assistiu no formato [(nota_prevista0-5, filme)]
def get_recomendacoes_usuarios(base_de_dados, usuario):
    totais = {}
    soma_similaridades = {}

    # Ao sair desse for, os dicionários totais e soma_similaridades vão estar preenchidos no formato {filme: valor}
    for outro in base_de_dados: # Percorre a lista de usuários na base de dados
        if outro == usuario: continue # Pula o bloco de código abaixo caso outro == usuario
        similaridade = distancia_euclidiana(base_de_dados, usuario, outro) # Calcula a similaridade (0-1) entre o usuário "alvo" e usuário "outro"
        if similaridade <= 0: continue # Pula o bloco de código abaixo caso não haja filmes em comum (similaridade 0)

        for filme in base_de_dados[outro]: # Itera os filmes assistidos por "outro"
            if filme not in base_de_dados[usuario]: # Se "usuario" não assistiu, calcular previsão de nota
                totais.setdefault(filme, 0) # Define chave-valor padrão para o filme no dicionário totais, evita erros
                totais[filme] += base_de_dados[outro][filme] * similaridade # Vai adicionando ao valor de determinado filme um total ponderado

                soma_similaridades.setdefault(filme, 0) # Define chave-valor padrão para o filme no dicionário soma_similaridades, evita erros
                soma_similaridades[filme] += similaridade # Vai adicionando ao valor de determinado filme a similaridade usuario x outro

    rankings = [(total / soma_similaridades[filme], filme) for filme, total in totais.items()] # Calcula a nota prevista e retorna uma
                                                                                               # lista no formato [(nota_prevista, filme)]
    rankings.sort() # Ordena a lista em ordem crescente
    rankings.reverse() # Inverte para ordem decrescente
    return rankings[0:30] # Retorna apenas os trinta primeiros valores (base do movielens tem mais de 100k)



# Carrega a base de dados baixada do movielens e faz o tratamento, retorna a base de dados no formato {usuario: {titulo: nota}}
def carrega_movielens(path="movielens/"):
    filmes = {}
    for linha in open(path+"u.item"): # Abre o arquivo de id:filme e lê linha por linha
        (id, titulo) = linha.split("|")[0:2] # Salva os dois primeiros valores [0:2] separados pelo delimitador "|" em suas respectivas variáveis
        filmes[id] = titulo # Adiciona chave-valor ao dicionário

    base_de_dados = {}
    for linha in open(path+"u.data"): # Abre o arquivo de id_usuario:id_filme:nota e lê linha por linha
        (usuario, id_filme, nota) = linha.split("\t")[0:3] # Salva os três primeiros valores [0:3] separados pelo delimitador "\t" (tab) em suas respectivas variáveis
        base_de_dados.setdefault(usuario, {}) # Inicializa um modelo para o dicionário, evita erros
        base_de_dados[usuario][filmes[id_filme]] = float(nota) # Atribui ao usuario/filme a nota, no formato {usuario: {titulo: nota}}

    return base_de_dados



# Calcula a similaridade de todos os items com todos os items, retorna um dicionário no formato {filme: [(similaridade0-1, titulo)]}
def calcula_itens_similares(base_de_dados):
    resultado = {}
    for item in base_de_dados: # Para cada filme em base dados
        notas = get_similares(base_de_dados, item) # Atribui a notas todas as similaridades
        resultado[item] = notas # Adiciona ao dicionario
    return resultado



# Com base em um usuário e o cálculo de itens similares, retorna as recomendações em uma lista [(nota_prevista, filme)]
def get_recomendacoes_itens(base_usuario, similaridade_itens, usuario): # similaridade_itens é o metodo calcula_itens_similares()
    notas_usuario = base_usuario[usuario] # Filmes assistidos pelo usuário e suas notas
    notas = {}
    total_similaridade = {}
    for (item, nota) in notas_usuario.items(): # Itera os filmes assistidos pelo usuário e suas notas e separa-os em suas respectivas variáveis
        for (similaridade, item2) in similaridade_itens[item]: # Pega a lista [(similaridade0-1, titulo)] para o filme que está sendo iterado
            if item2 in notas_usuario: continue # Pula se usuario já assistiu
            notas.setdefault(item2, 0)
            notas[item2] += similaridade * nota # Calcula o somatório de forma ponderada, basado na similaridade do filme
            total_similaridade.setdefault(item2, 0)
            total_similaridade[item2] += similaridade # Somatório da similaridade
    rankings = [(score / total_similaridade[item], item) for (item, score) in notas.items()] # [(nota_prevista, filme)] para cada filme que usuário não assistiu
    rankings.sort() # Ordena crescente
    rankings.reverse() # Ordena decrescente
    return rankings



# Retorna a quantidade de filmes avaliados pelo usuário em relação a uma base de dados
def quantidade_filmes_avaliados(base_de_dados, usuario):
    cont = 0
    for filme in base_de_dados[usuario]: cont += 1 # Soma 1 para cada filme avaliado
    return cont



# Retorna uma lista [(nota, filme)] em ordem decrescente (do melhor avaliado até o pior) para os filmes que o usuario avaliou
# Caso o parâmetro decrescente=False, retorna uma lista do filme pior avaliado até o melhor (crescente)
def filmes_avaliados(base_de_dados, usuario, decrescente=True):
    filmes = [(nota, filme) for (filme, nota) in base_de_dados[usuario].items()] # Itera os filmes avaliados e armazena no formato [(nota, filme)]
    # "Nota" precisa ser o primero elemento da lista, caso contrario, seria ordenado por ordem alfabética
    filmes.sort() # Crescente
    if decrescente: filmes.reverse() # Inverte se decrescente=True
    return filmes



# Mostra uma espécie de perfil para o usuário determinado, com os filmes melhores/pior avaliados por ele, e algumas recomendações
def perfil(base_de_dados, usuario):
    print(f"Usuário: {usuario}")
    print(f"Filmes Avaliados: {quantidade_filmes_avaliados(base_de_dados, usuario)}")

    print("-"*30)
    print("\033[1m\033[34m10 Filmes melhores avaliados por você:\033[0m")
    for (nota, filme) in filmes_avaliados(base_de_dados, usuario)[0:10]:
        print(f"{filme}: {nota}⭐")

    print("-" * 30)
    print("\033[1m\033[31m10 Filmes pior avaliados por você:\033[0m")
    for (nota, filme) in filmes_avaliados(base_de_dados, usuario, decrescente=False)[0:10]:
        print(f"{filme}: {nota}⭐")

    print("-" * 30)
    print("\033[1m\033[35m5 Recomendações para você:\033[0m")
    for (nota_prevista, filme) in get_recomendacoes_usuarios(base_de_dados, usuario)[0:5]:
        print(f"{filme}: {nota_prevista}⭐")