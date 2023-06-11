use sucos_vendas;

select * from tabela_de_produtos;
select * from itens_notas_fiscais;

select a.numero, a.codigo_do_produto, a.quantidade, b.nome_do_produto, b.preco_de_lista from itens_notas_fiscais a
inner join tabela_de_produtos b
on a.CODIGO_DO_PRODUTO = b.codigo_do_produto;

select a.codigo_do_produto, b.nome_do_produto, b.preco_de_lista, sum(a.quantidade) as qtd_total from itens_notas_fiscais a
inner join tabela_de_produtos b
on a.CODIGO_DO_PRODUTO = b.codigo_do_produto
group by a.CODIGO_DO_PRODUTO, b.NOME_DO_PRODUTO, b.PRECO_DE_LISTA;
