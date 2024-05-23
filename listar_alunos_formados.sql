select * from aluno A
inner join curso C
on A.creditos_totais = C.creditos and A.id_curso = C.id_curso
inner join historico_aluno H
on H.semestre = '1' and H.ra = A.ra