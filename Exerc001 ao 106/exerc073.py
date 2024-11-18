''''
 Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times_brasileiros = (
    "Flamengo",
    "Corinthians",
    "Palmeiras",
    "Santos",
    "Atlético Mineiro",
    "Grêmio",
    "Cruzeiro",
    "Internacional",
    "São Paulo",
    "Fluminense",
    "Botafogo",
    "Vasco da Gama",
    "Athletico Paranaense",
    "Chapecoense",
    "Fortaleza",
    "Ceará",
    "Bahia",
    "Sport",
    "América-MG",
    "Coritiba",
    "Goiás"
)
cinco_primeiros = times_brasileiros[0:5]
ultimos_quatro = times_brasileiros[-4:]
times_ordem_alfabetica = sorted(times_brasileiros)
posicao_chapecoenche = times_brasileiros.index("Chapecoense") + 1

print(f'Times em ordem de classificação: ')
for t in times_brasileiros:
    print('>',(t))

print(f'Os cinco primeiros colocados são {", ".join(cinco_primeiros)}.')

print(f'Os ultimos quatro colocados são {", ".join(ultimos_quatro)}.')

print(f'Time em ordem alfabética: \n {"\n".join(times_ordem_alfabetica)}')

print(f'O Chapecoenche entra na posição {posicao_chapecoenche}ª do campeonato')

