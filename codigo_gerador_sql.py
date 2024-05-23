from faker import Faker # type: ignore
from random import randint, uniform, choice

qtd = 100

fake = Faker('pt-BR')
nomes_a = [fake.unique.name() for i in range(qtd)]
nomes_p = [fake.unique.name() for i in range(qtd)]

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



departamentos = ["Civil", "Eletrica", "Mecanica", "Quimica", "Robotica", "Producao", "Computacao", "Fisica", "Matematica", "Administracao",]

departamentos_ap = ["Civil", "Eletrica", "Mecanica", "Quimica", "Robotica", "Producao", "Computacao", "Fisica", "Matematica", "Administracao",]

prefixo_curso = 'C0'

ids_curso = [(prefixo_curso + str(id)) for id in range(10)]
ids_curso2 = [(prefixo_curso + str(id)) for id in range(10)]
ids_curso_matriz = [(prefixo_curso + str(id)) for id in range(10)]

cursos = ["Engenharia Civil", "Engenharia Eletrica", "Engenharia Mecanica", "Engenharia Quimica", "Engenharia de Robos", "Engenharia de Producao", "Ciencia da Computacao", "Fisica", "Matematica", "Administracao"]


prefixo_disciplina = 'D0'

ids_disciplina = [(prefixo_disciplina + str(id)) for id in range(200)]

siglas = ['EC', 'EE', 'EM', 'EQ', 'ER', 'EP', 'CC', 'FS', 'MT', 'AD']
disciplinas = [(choice(siglas) + str(id)) for id in range(200)]


edificios = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

finall = 99
final_cursos = 9
final_disciplinas = 199
final_departamento_curso = 9


def cria_departamentos_cursos_sql():
    global final_departamento_curso

    if(final_departamento_curso > 0):
        aleatorio_departamento_curso = randint(0, final_departamento_curso)

    try:
     dept_nome = departamentos.pop(aleatorio_departamento_curso)
     orcamento = round(uniform(10000, 100000), 2)
     edificio = edificios.pop(aleatorio_departamento_curso)

     print(f"\ninsert into departamento(dept_nome, orcamento, edificio) values ('{dept_nome}', '{orcamento}', '{edificio}');\n")

     id_curso = ids_curso.pop(aleatorio_departamento_curso)
     titulo = cursos.pop(aleatorio_departamento_curso)
     creditos = randint(10, 50)
     
     print(f"\ninsert into curso(id_curso, dept_nome, titulo, creditos) values ('{id_curso}', '{dept_nome}', '{titulo}', '{creditos}');\n")
    except:
       print("Todos os departamentos/cursos já foram inseridos!\n")
    
    final_departamento_curso -= 1

#-----------------------------------------------------------------------------------------------------------------------------------

def cria_tabelas_sql(final_cursos=final_cursos, final_disciplinas = final_disciplinas):
    global finall

    if(finall > 0):
        aleatorio = randint(0, finall)
        
    aleatorio_cursos = randint(0, final_cursos)
    aleatorio_disciplinas = randint(0, final_disciplinas)

    dept_nome = departamentos_ap[aleatorio_cursos]
    id = ids.pop(aleatorio)
    nome = nomes_p.pop(aleatorio)
    salario = round(uniform(5000, 20000), 2)
    eh_chefe = choice([True, False])

    print(f"insert into professor(id, nome, dept_nome, salario, eh_chefe) values ('{id}', '{nome}', '{dept_nome}', '{salario}', {eh_chefe});\n")

    aleatorio = randint(0, finall)
    tcc_id = tcc_ids.pop(aleatorio)
    print(f"insert into grupo_tcc(tcc_id, id) values ('{tcc_id}', '{id}');\n")

    aleatorio = randint(0, finall)
    ra = ras.pop(aleatorio)
    dept_nome = departamentos_ap[aleatorio_cursos]
    nome = nomes_a.pop(aleatorio)
    id_curso = ids_curso_matriz[aleatorio_cursos]
    creditos_totais = randint(10,50)   

    print(f"insert into aluno(ra, id_curso, nome, tcc_id, creditos_totais) values ('{ra}', '{id_curso}', '{nome}', '{tcc_id}', '{creditos_totais}');\n") #!!!!!!!!!!!!!

    print(f"insert into orientado(p_id, a_ra) values ('{id}', '{ra}');\n")
    
    id_disciplina = ids_disciplina[aleatorio_disciplinas]
    nome = disciplinas[aleatorio_disciplinas]
    semestre = choice([1, 2])
    ano = randint(1990, 2024)
    media = randint(0, 10)

    print(f"insert into disciplina(id_disciplina, nome) values ('{id_disciplina}', '{nome}');\n")

    print(f"insert into historico_aluno(ra, id_disciplina, semestre, ano, media) values ('{ra}', '{id_disciplina}', '{semestre}', '{ano}', '{media}');\n")

    id_historico_p = ids_historico_p.pop(aleatorio)

    print(f"insert into historico_professor(id, id_historico, id_disciplina, semestre, ano) values ('{id}', '{id_historico_p}', '{id_disciplina}', '{semestre}', '{ano}');\n")

    id_curso_matriz = ids_curso_matriz[aleatorio_cursos]

    print(f"insert into matriz_curricular(id_curso, id_disciplina) values ('{id_curso_matriz}', '{id_disciplina}');\n")

    
    finall -= 1


print("--" * 60)
print(f"Conjunto de Instruções de Departamentos e Cursos")
print("--" * 60)

for x in range(10):
    cria_departamentos_cursos_sql()
    
for y in range(10):
    print("--" * 60)
    print(f"Conjunto de Instruções {y+1}")
    print("--" * 60)
    cria_tabelas_sql()