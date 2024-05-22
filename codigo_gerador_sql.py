from faker import Faker # type: ignore
from random import randint, uniform, choice

qtd = 100

fake = Faker('pt-BR')
nomes = [fake.unique.name() for i in range(qtd)]

nomes_copia = nomes[:]

for nome in nomes_copia:
    nome_atual = nome
    nomes.remove(nome)


prefixo_ra = '220'

ras = [(prefixo_ra + str(ra)) for ra in range(qtd)]

prefixo_historico_a = 'HA'

ids_historico_a = [(prefixo_historico_a + str(ra)) for ra in range(qtd)]

prefixo_id = '230'



ids = [(prefixo_id + str(id)) for id in range(qtd)]

prefixo_historico_p = 'HP'

ids_historico_p = [(prefixo_historico_p + str(id)) for id in range(qtd)]



prefixo_tcc = 'TCC'

tcc_ids = [(prefixo_tcc + str(id)) for id in range(qtd)]



departamentos = ["Civil", "Eletrica", "Mecanica", "Quimica", "Robotica", "Producao", "Computacao", "Fisica", "Matematica", "Administracao"]



prefixo_curso = 'C0'

ids_curso = [(prefixo_curso + str(id)) for id in range(10)]

cursos = ["Engenharia Civil", "Engenharia Eletrica", "Engenharia Mecanica", "Engenharia Quimica", "Engenharia de Robos", 
                 "Engenharia de Producao", "Ciencia da Computacao", "Fisica", "Matematica", "Administracao"]


prefixo_disciplina = 'D0'

ids_disciplina = [(prefixo_disciplina + str(id)) for id in range(200)]



edificios = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

orcamento = round(uniform(10000, 100000), 2)

salario = round(uniform(5000, 20000), 2)
eh_chefe = choice([True, False])


