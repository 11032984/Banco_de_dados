"""Exercícios SELECT
    1. Consulte com select todos dos dados nas tabelas herói, monstro, poder e batalha. Obs.: Cada um com o seu select
    2. Faça uma união entre monstro e herói Obs.: Cuidado com as colunas (tem que ter o mesmo total de colunas)
    3. Selecione todos os poderes de cada herói Obs.: Ordenação pelo nome do herói
    4. Selecione todos os poderes de cada monstro Obs.: Ordenação pelo nome do monstro
    5. Selecione todas as batalhas de cada herói Obs.: Ordenação pela data e horário da batalha, seguida pelo nome
    6. Selecione todas as participações em batalha de cada herói contra cada monstro, filtrando onde teve vitória e o monstro tinha nível maior que o herói Obs.: Ordenação pela data e hora da batalha, e depois pelo nome do herói


"""
#####################################################################################################################################################################################################################################
1- SELECT
select * from heroi
select * from monstro
select * from poder
select * from batalhas



2 -SELECT id, nome, nivel, forca, defesa, vida, mana,moeda, xp FROM heroi
union
select id, nome, nivel, forca, defesa, vida, mana, moeda_reconpenca, xp_reconpenca from monstro



3-
SELECT  h.id   AS h_id, h.nome AS h_nome, p.id AS p_id, p.tipo AS p_tipo
FROM heroi AS h
LEFT JOIN heroi_poder AS hp ON hp.heroi_id = h.id
LEFT JOIN poder AS p ON p.id  = hp.poder_id
ORDER BY h.nome
4 -
SELECT  m.id   AS m_id, m.nome AS m_nome, p.id AS p_id, p.tipo AS p_tipo
FROM monstro AS m
LEFT JOIN monstro_poder AS mp ON mp.heroi_id = m.id
LEFT JOIN poder AS p ON p.id  = mp.poder_id
ORDER BY m.nome




5/6
SELECT  h.id   AS h_id, h.nome AS h_nome,
b. “data” AS b_data, b.hora AS b_hora,
m.id AS m id, m.nome AS m_nome,
FROM heroi AS h
LEFT JOIN monstro_heroi_batalha AS mhb.heroi_id = h.id
LEFT JOIN batalhas AS b ON b.id = mhb.batalha_id
RIGHT JOIN monstro  AS m ON m.id = mhb.monstro_id
ORDER BY b. “data”, b.hora, h.nome ASC


