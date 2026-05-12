estoque = [
    {'produto': 'Dipirona', 'categoria': 'Analgesico', 'quantidade': 15, 'minimo': 50, 'preco': 8.90, 'validade': '2024-06-01'},
    {'produto': 'Amoxicilina', 'categoria': 'Antibiotico', 'quantidade': 200, 'minimo': 30, 'preco': 25.00, 'validade': '2023-12-01'},
    {'produto': 'Ibuprofeno', 'categoria': 'Analgesico', 'quantidade': 8, 'minimo': 40, 'preco': 12.50, 'validade': '2025-03-01'},
    {'produto': 'Omeprazol', 'categoria': 'Gastrico', 'quantidade': 0, 'minimo': 20, 'preco': 15.00, 'validade': '2024-08-01'},
    {'produto': 'Loratadina', 'categoria': 'Alergico', 'quantidade': 90, 'minimo': 25, 'preco': 18.00, 'validade': '2024-02-01'},
]

estoque_zerado = []

abaixo_do_minimo = []

produtos_vencidos = []

valor_por_categoria = {}

alerta_geral = []

for item in estoque:
    produto_atual = item['produto']
    categoria_atual = item['categoria']
    quantidade_atual = item['quantidade']
    minimo_atual = item['minimo']
    preco_atual = item['preco']
    validade_atual = item['validade']

    data_hoje = '2024-03-20'

    if validade_atual < data_hoje:
        produtos_vencidos.append(produto_atual)
    if quantidade_atual == 0:
        estoque_zerado.append(produto_atual)
    if quantidade_atual < minimo_atual:
        abaixo_do_minimo.append(produto_atual)

    valor_item = quantidade_atual * preco_atual

    if categoria_atual not in valor_por_categoria:
          valor_por_categoria[categoria_atual] = valor_item
    else:
          valor_por_categoria[categoria_atual] += valor_item

    motivos_produto = []

    if quantidade_atual > 0 and quantidade_atual < minimo_atual:
        motivos_produto.append("Abaixo do Mínimo")
    if validade_atual < data_hoje:
        motivos_produto.append("Produto Vencido")
    if quantidade_atual == 0:
        motivos_produto.append("Estoque Zerado")
    if len(motivos_produto) > 0:
        alerta_geral.append({
            'produto': produto_atual,
            'alertas': motivos_produto
        })

print("--- RELATÓRIO DE MONITORAMENTO DE ESTOQUE ---")
print(f"Produtos com estoque zerado: {estoque_zerado}")
print(f"Produtos abaixo do mínimo: {abaixo_do_minimo}")
print(f"Produtos vencidos: {produtos_vencidos}")
print(f"Valor total em estoque por categoria: {valor_por_categoria}")

print("\n--- ALERTA GERAL DE ATENÇÃO ---")

for alerta in alerta_geral:
    print(f"Produto: {alerta['produto']} | Motivos: {alerta['alertas']}")
