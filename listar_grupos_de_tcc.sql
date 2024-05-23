select RA, nome, id as id_professor from aluno A
inner join grupo_tcc G
on A.tcc_id = G.tcc_id 