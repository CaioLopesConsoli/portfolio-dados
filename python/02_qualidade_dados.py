# Pipeline de qualidade e validação de dados de clientes
clientes_raw = [
    {'id': 1, 'nome': '  joão silva ', 'email': 'joao@gmail.com', 'cpf': '123.456.789-01', 'idade': 28},
    {'id': 2, 'nome': 'MARIA SOUZA', 'email': 'maria.hotmail.com', 'cpf': '98765432100', 'idade': -5},
    {'id': 3, 'nome': 'pedro alves', 'email': 'pedro@yahoo.com', 'cpf': '111.222.333-44', 'idade': 35},
    {'id': 4, 'nome': '', 'email': 'ana@outlook.com', 'cpf': '99988877766', 'idade': 200},
    {'id': 5, 'nome': 'Carlos Eduardo', 'email': 'carlos@gmail.com', 'cpf': '12345678901', 'idade': 42},
]

clientes_validos = []
clientes_invalidos = []


for cliente in clientes_raw:
    id_atual = cliente['id']
    nome_atual = cliente['nome']
    email_atual = cliente['email']
    cpf_atual = cliente['cpf']
    idade_atual = cliente['idade']

    nome_limpo = nome_atual.strip().title()
    cpf_limpo = cpf_atual.replace(".", "").replace("-", "")

    erros_do_cliente = []

    if nome_limpo == "":
        erros_do_cliente.append("Nome em branco")
    if "@" not in email_atual or "." not in email_atual:
        erros_do_cliente.append("E-mail inválido")
    if len(cpf_limpo) != 11 or not cpf_limpo.isdigit():
        erros_do_cliente.append("CPF deve conter 11 dígitos numéricos")
    if idade_atual < 0 or idade_atual > 120:
        erros_do_cliente.append("Idade fora do intervalo permitido (0-120)")

    if len(erros_do_cliente) == 0:
        cliente_salvo = {
            'id': id_atual,
            'nome': nome_limpo,
            'email': email_atual,
            'cpf': cpf_limpo,
            'idade': idade_atual
        }
        clientes_validos.append(cliente_salvo)
    else:
        cliente_rejeitado = {
            'id': id_atual,
            'nome': nome_atual,
            'erros': erros_do_cliente
        }
        clientes_invalidos.append(cliente_rejeitado)
    


print("--- RELATÓRIO DE QUALIDADE DE DADOS ---")
print(f"Total de clientes processados: {len(clientes_raw)}")
print(f"Clientes válidos para importação: {len(clientes_validos)}")
print(f"Clientes inválidos (rejeitados): {len(clientes_invalidos)}")
print("\n--- DETALHAMENTO DOS ERROS ---")

for rejeitado in clientes_invalidos:
    print(f"ID {rejeitado['id']} - Nome Original: '{rejeitado['nome']}' | Erros: {rejeitado['erros']}")
