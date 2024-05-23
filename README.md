# Projeto-Banco-De-Dados
Um modelo de banco de dados projetado para atender as demandas de uma faculdade

# Participantes 
Angelo Gabriel Vasconcelos Baptista  RA: 22.122.081-7

Luan Petroucic Moreno RA: 22.122.076-7
# Diagrama Relacional

![image](https://github.com/AngeloGabriel-dev/Projeto-Banco-De-Dados/blob/main/Modelo%20Relacional.png)

# Como instalar o banco
Inicialmente, faz-se imprescindível que o usuário crie um cluster no CockroachDB e faça os procedimentos
padrões para conectá-lo no DBeaver. <br>
Após isso, é necessário utilizar o script de criação de tabelas 'Script_criacao_tabelas.sql' para inicializar
as tabelas do banco. <br>
Tendo as tabelas em mãos, está na hora de executar o script python 'codigo_gerador_sql.py' para a geração de
instruções de insert aleatórias, o programa irá printar no terminal todos os inserts que deverão ser copiados
e colados em um script sql e subsequentemente rodados no DBeaver. <br>
Finalmente, resta apenas testar cada um dos scripts sql responsáveis por realizar as 5 atividades exigidas no
projeto. <br>


