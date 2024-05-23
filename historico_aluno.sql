select D.id_disciplina, D.nome, H.semestre, H.ano, H.media from historico_aluno H
inner join disciplina D on H.id_disciplina = D.id_disciplina 
where H.RA = '22087' ;

