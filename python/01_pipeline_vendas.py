vendas = [
    {'data': '2024-01-15', 'produto': 'Notebook', 'categoria': 'Eletronicos', 'vendedor': 'Ana', 'regiao': 'Sul', 'quantidade': 2, 'preco_unitario': 3500.0},
    {'data': '2024-01-18', 'produto': 'Mouse', 'categoria': 'Eletronicos', 'vendedor': 'Carlos', 'regiao': 'Norte', 'quantidade': 5, 'preco_unitario': 150.0},
    {'data': '2024-02-03', 'produto': 'Notebook', 'categoria': 'Eletronicos', 'vendedor': 'Ana', 'regiao': 'Sul', 'quantidade': 1, 'preco_unitario': 3500.0},
    {'data': '2024-02-10', 'produto': 'Cadeira', 'categoria': 'Moveis', 'vendedor': 'Pedro', 'regiao': 'Leste', 'quantidade': 3, 'preco_unitario': 800.0},
    {'data': '2024-02-20', 'produto': 'Mesa', 'categoria': 'Moveis', 'vendedor': 'Maria', 'regiao': 'Sul', 'quantidade': 2, 'preco_unitario': 1200.0},
    {'data': '2024-03-05', 'produto': 'Monitor', 'categoria': 'Eletronicos', 'vendedor': 'Carlos', 'regiao': 'Norte', 'quantidade': 4, 'preco_unitario': 900.0},
    {'data': '2024-03-12', 'produto': 'Teclado', 'categoria': 'Eletronicos', 'vendedor': 'Ana', 'regiao': 'Sul', 'quantidade': 6, 'preco_unitario': 200.0},
    {'data': '2024-03-18', 'produto': 'Cadeira', 'categoria': 'Moveis', 'vendedor': 'Pedro', 'regiao': 'Leste', 'quantidade': 2, 'preco_unitario': 800.0},
]


faturamento_regiao = {}

faturamento_vendedor = {}

faturamento_mes = {}

faturamento_produto = {}

faturamento_categoria = {}

faturamento_total = 0

for venda in vendas:
    categoria_atual = venda['categoria']
    regiao_atual = venda['regiao']
    vendedor_atual = venda['vendedor']
    produto_atual = venda['produto']

    faturamento_venda = venda['quantidade'] * venda['preco_unitario']
    mes_atual = venda['data'][5:7]

    if categoria_atual not in faturamento_categoria:
        faturamento_categoria[categoria_atual] = faturamento_venda
    else:
        faturamento_categoria[categoria_atual] += faturamento_venda

    faturamento_total += faturamento_venda

    if regiao_atual not in faturamento_regiao:
        faturamento_regiao[regiao_atual] = faturamento_venda
    else:
        faturamento_regiao[regiao_atual] += faturamento_venda

    if vendedor_atual not in faturamento_vendedor:
        faturamento_vendedor[vendedor_atual] = faturamento_venda
    else:
        faturamento_vendedor[vendedor_atual] += faturamento_venda
    
    if mes_atual not in faturamento_mes:
        faturamento_mes[mes_atual] = faturamento_venda
    else:
        faturamento_mes[mes_atual] += faturamento_venda

    if produto_atual not in faturamento_produto:
        faturamento_produto[produto_atual] = faturamento_venda
    else:
        faturamento_produto[produto_atual] += faturamento_venda

vendedor_top = max(faturamento_vendedor, key=faturamento_vendedor.get)
mes_top = max(faturamento_mes, key=faturamento_mes.get)
media_produto = faturamento_total / len(faturamento_produto)

produtos_abaixo_media = []

for produto, faturamento in faturamento_produto.items():
    if faturamento < media_produto:
        produtos_abaixo_media.append(produto)
    
print("--- RELATÓRIO DE VENDAS (Q1) ---")
print(f"Faturamento Total: R$ {faturamento_total:.2f}")
print(f"Faturamento por Categoria: {faturamento_categoria}")
print(f"Faturamento por Região: {faturamento_regiao}")
print(f"Vendedor com Maior Faturamento: {vendedor_top}")
print(f"Mês com Maior Faturamento (Código): {mes_top}")
print(f"Produtos Abaixo da Média de Faturamento: {produtos_abaixo_media}")
