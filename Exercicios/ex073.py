"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time do Ceará.
"""
tabela = ('Flamengo','Internacional','Atlético MG','São Paulo','Fluminense',
          'Grêmio','Palmeiras','Santos','Athletico-PR','Bragantino',
          'Ceará','Corinthians','Atlético Goianiense','Bahia','Sport',
          'Fortaleza','Vasco da Gama','Goiás','Coritiba','Botafogo')
print('=-'*20)
print('Os Cinco Primeiros Times')
print(tabela[0:5])
print('=-'*20)
print('Os 4 últimos times')
print(tabela[16:])
print('=-'*20)
print('Todos os Times em Ordem Alfabetica')
print(sorted(tabela))
print('=-'*20)
print(f'O Ceará está na {tabela.index("Ceará")+1}º Posição')
