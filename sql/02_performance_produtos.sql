-- Os 5 produtos mais vendidos em quantidade total
SELECT produtos.nome, SUM(itenspedidos.quantidade) as total_prdutos_vendidos, SUM(itenspedidos.precounitario * itenspedidos.quantidade) as faturamento
FROM produtos
JOIN itenspedidos on produtos.id = itenspedidos.idprodutos
GROUP BY produtos.nome
ORDER BY total_prdutos_vendidos DESC
LIMIT 5;

-- Qual o faturamento total por categoria?
SELECT SUM(itenspedidos.precounitario * itenspedidos.quantidade) as valor_faturamento, produtos.categoria
FROM itenspedidos
JOIN produtos on itenspedidos.idprodutos = produtos.id
GROUP BY produtos.categoria;

-- Quais produtos nunca foram vendidos?
SELECT produtos.nome as produtos_nunca_vendidos
FROM produtos
LEFT JOIN itenspedidos on produtos.id = itenspedidos.idprodutos
WHERE(itenspedidos.idprodutos is NULL);

-- Qual a média de itens por pedido?
SELECT AVG(itenspedidos.quantidade) as media_pedidos
FROM itenspedidos;

-- Qual produto tem o maior faturamento total?
SELECT produtos.nome, SUM(itenspedidos.precounitario * itenspedidos.quantidade) AS faturamento_total
FROM itenspedidos
JOIN produtos on itenspedidos.idprodutos = produtos.id
GROUP by produtos.nome
ORder by faturamento_total desc LIMIT 1;

