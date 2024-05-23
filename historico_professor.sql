select D.id_disciplina, D.nome, H.semestre, H.ano 
from historico_professor H
inner join disciplina D on H.id_disciplina = D.id_disciplina 
where H.id = '23033'