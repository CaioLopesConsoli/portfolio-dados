-- Os 5 clientes que mais gastaram no total?
SELECT clientes.nome, SUM((itenspedidos.precounitario * itenspedidos.quantidade)) AS valor_total
FROM clientes
JOIN pedidos on clientes.id = pedidos.id_cliente
JOIN itenspedidos on pedidos.id = itenspedidos.id_pedidos
GROUP BY clientes.nome
ORDER BY valor_total DESC LIMIT 5;

-- ticket médio por pedido de cada cliente?
SELECT 
    sub_pedido.nome,
    AVG(sub_pedido.total_do_pedido) AS ticket_medio_por_cliente
FROM (
 
    SELECT clientes.nome, SUM(itenspedidos.precounitario * itenspedidos.quantidade) AS total_do_pedido
    FROM clientes
    JOIN pedidos ON clientes.id = pedidos.id_cliente
    JOIN itenspedidos ON pedidos.id = itenspedidos.id_pedidos
    GROUP BY clientes.nome, pedidos.id
) AS sub_pedido
GROUP BY sub_pedido.nome
ORDER BY ticket_medio_por_cliente DESC;


-- Clientes que nunca fizeram um pedido?
SELECT clientes.nome
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.id_cliente
WHERE pedidos.id_cliente IS NULL;

-- Qual cliente fez o maior número de pedidos?
SELECT COUNT(pedidos.id), clientes.nome as cliente_maior_pedidos
FROM clientes
JOIN pedidos on clientes.id = pedidos.id_cliente
GROUP by clientes.nome
ORDER by COUNT(pedidos.id) DESC LIMIT 1;

-- Qual o gasto médio por pedido de toda a base?
SELECT AVG(itenspedidos.precounitario * itenspedidos.quantidade) as media_gasto_por_pedido
FROM itenspedidos;
