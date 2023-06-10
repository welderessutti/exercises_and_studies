use sucos_vendas;

select distinct bairro from tabela_de_clientes where cidade = "rio de janeiro";

select * from notas_fiscais where data_venda = "2017-01-01" limit 2, 10;

select * from tabela_de_produtos where nome_do_produto = "Linha Refrescante - 1 Litro - Morango/Limão";

select * from itens_notas_fiscais where codigo_do_produto = 1101035 order by quantidade desc;

select max(quantidade) as maior_quantidade from itens_notas_fiscais where codigo_do_produto = 1101035;

select count(*) as contador from itens_notas_fiscais where codigo_do_produto = 1101035 and quantidade = 99;

select codigo_do_produto, sum(quantidade) as total from itens_notas_fiscais group by codigo_do_produto;

select cpf, count(*) as contador from notas_fiscais where year(data_venda) = 2016 group by cpf having contador > 2000;

select
case
	when year(data_de_nascimento) < 1990 then "Velhos"
	when year(data_de_nascimento) >= 1990 and year(data_de_nascimento) <= 1995 then "Jovens"
	else "Criancas"
end as "Classificacao", count(cpf) as contador
from tabela_de_clientes group by case
	when year(data_de_nascimento) < 1990 then "Velhos"
	when year(data_de_nascimento) >= 1990 and year(data_de_nascimento) <= 1995 then "Jovens"
	else "Criancas"
end;
