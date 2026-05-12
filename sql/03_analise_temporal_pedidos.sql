-- Quantos pedidos foram feitos por mês?
SELECT SUBSTR(pedidos.data_hora_pedido, 1, 7) AS ano_mes, COUNT(pedidos.id) AS total_pedidos
FROM pedidos
GROUP by ano_mes;

-- Qual o status mais comum dos pedidos?
SELECT pedidos.status, COUNT(pedidos.id) AS total_status
FROM pedidos
GROUP BY pedidos.status
ORDER BY total_status DESC LIMIT 1;

-- Qual mês teve o maior faturamento?
SELECT SUBSTR(pedidos.data_hora_pedido, 1, 7) AS ano_mes, SUM(itenspedidos.quantidade * itenspedidos.precounitario) AS faturamento_total
FROM pedidos
JOIN itenspedidos on pedidos.id = itenspedidos.id_pedidos
GROUP by ano_mes
ORDER BY faturamento_total DESC LIMIT 1;

-- Qual a distribuição percentual de pedidos por status?
SELECT pedidos.status, (COUNT(pedidos.id) * 100.0) / (SELECT COUNT(*) FROM pedidos) AS percentual
FROM pedidos
GROUP BY pedidos.status;

-- Quais clientes fizeram pedidos nos últimos 3 meses disponíveis no banco?
SELECT DISTINCT clientes.nome
FROM clientes
JOIN pedidos on clientes.id = pedidos.id_cliente
WHERE SUBSTR(pedidos.data_hora_pedido, 1, 7) IN (
    SELECT DISTINCT SUBSTR(data_hora_pedido, 1, 7) 
    FROM pedidos 
    ORDER BY data_hora_pedido DESC 
    LIMIT 3
);
