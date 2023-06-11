use sucos_vendas;

select distinct a.cpf, a.nome, b.cpf from tabela_de_clientes a
left join notas_fiscais b
on a.cpf = b.cpf;
