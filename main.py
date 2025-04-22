from recomendacao import *

"""Filtragem baseada em usuários: Ideal para conjuntos menores de dados. Calcula tudo toda vez que a função é chamada.
   Adequada para conjunto de dados denso, onde os usuários avaliaram muitos produtos."""

"""Filtragem baseada em itens: Ideal para conjuntos maiores/comerciais de dados. A similaridade entre produtos é calculada
   antecipadamente (em momentos de baixo tráfego) e salva em algum lugar. É recalculada periodicamente, evitando operações repetidas.
   Adequada para conjunto de dados esparso, onde os usuários avaliaram uma pequena porcentagem dos produtos disponíveis"""

lista_itens = calcula_itens_similares(avaliacoes_filme)

print(get_recomendacoes_usuarios(avaliacoes_usuario, "Leonardo"))
print(get_recomendacoes_itens(avaliacoes_usuario, lista_itens, "Leonardo"))