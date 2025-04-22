from recomendacao import *

base = carrega_movielens()

print(get_recomendacoes(base, "1"))