CREATE TABLE departamento(
  dept_nome varchar(50) not null primary key,
  orcamento numeric(12,2),
  edificio varchar(15)
);

CREATE TABLE professor(
  id varchar(5) not null primary key,
  nome varchar(50) not null,
  dept_nome varchar(50),
  salario numeric(8,2) not null,
  eh_chefe boolean,
  foreign key (dept_nome) references departamento(dept_nome)
);

CREATE TABLE grupo_tcc(
  tcc_id varchar(5) not null primary key,
  id varchar(5),
  foreign key (id) references professor(id)
);

CREATE TABLE curso(
  id_curso varchar(8) not null primary key,
  dept_nome varchar(50),
  titulo varchar(50),
  creditos numeric(2),
  foreign key (dept_nome) references departamento(dept_nome)
);

CREATE TABLE disciplina(
  id_disciplina varchar(8) not null primary key,
  nome varchar(20)
);

CREATE TABLE aluno(
  RA varchar(10) not null primary key,
  id_curso varchar(8),
  nome varchar(50) not null,
  tcc_id varchar(5),
  creditos_totais numeric(2),
  foreign key (id_curso) references curso(id_curso),
  foreign key (tcc_id) references grupo_tcc(tcc_id)
);

CREATE TABLE orientado(
  p_id varchar(5),
  a_RA varchar(10),
  foreign key (p_id) references professor(id),
  foreign key (a_RA) references aluno(RA)
);

CREATE TABLE historico_aluno(
  RA varchar(10),
  id_disciplina varchar(8),
  semestre varchar(6),
  ano numeric(4),
  media numeric (4,2),
  foreign key (RA) references aluno(RA),
  foreign key (id_disciplina) references disciplina(id_disciplina)
);

CREATE TABLE historico_professor(
  id varchar(5),
  id_historico varchar(8),
  id_disciplina varchar(8),
  semestre varchar(6),
  ano numeric(4),
  foreign key (id_disciplina) references disciplina(id_disciplina),
  foreign key (id) references professor(id)
);

CREATE TABLE matriz_curricular(
  id_curso varchar(8),
  id_disciplina varchar(8),
  foreign key (id_curso) references curso(id_curso),
  foreign key (id_disciplina) references disciplina(id_disciplina)
);
