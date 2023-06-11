use sucos_vendas;

select * from tabela_de_vendedores;
select * from notas_fiscais;

select a.matricula, a.nome, b.* from tabela_de_vendedores a
inner join notas_fiscais b
on a.matricula = b.matricula;

select a.matricula, a.nome, count(*) as total_vendas
from tabela_de_vendedores a
inner join notas_fiscais b
on a.matricula = b.matricula
group by a.matricula, a.nome;
