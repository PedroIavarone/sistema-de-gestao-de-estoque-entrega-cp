from dados import carregar_dados, salvar_dados, ARQUIVO_PRODUTOS
from estoque import registrar_movimento

_EXEMPLOS = [
    {
        "nome": "Bermuda Tactel Masculina",   "codigo": "VEST-001",
        "categoria": "vestuário",             "quantidade": 30,
        "preco": 59.90,                       "estoque_min": 5,
        "descricao": "Bermuda leve, ideal para o verão, tamanhos P ao GG",
        "fornecedor": "TextilBR",
    },
    {
        "nome": "Camiseta Básica Feminina",   "codigo": "VEST-002",
        "categoria": "vestuário",             "quantidade": 50,
        "preco": 39.90,                       "estoque_min": 8,
        "descricao": "100% algodão, várias cores disponíveis",
        "fornecedor": "TextilBR",
    },
    {
        "nome": "Calça Jeans Slim",           "codigo": "VEST-003",
        "categoria": "vestuário",             "quantidade": 4,  # estoque baixo para testar alerta
        "preco": 129.90,                      "estoque_min": 5,
        "descricao": "Jeans stretch, corte slim, do 38 ao 48",
        "fornecedor": "DenimFlex",
    },
    {
        "nome": "Tênis Casual Masculino",     "codigo": "CALC-001",
        "categoria": "calçados",              "quantidade": 20,
        "preco": 189.90,                      "estoque_min": 4,
        "descricao": "Solado emborrachado, numeração 38–44",
        "fornecedor": "SolBom",
    },
    {
        "nome": "Sandália Rasteira Feminina", "codigo": "CALC-002",
        "categoria": "calçados",              "quantidade": 15,
        "preco": 69.90,                       "estoque_min": 3,
        "descricao": "Sintético macio, tiras reguláveis",
        "fornecedor": "SolBom",
    },
    {
        "nome": "Fone de Ouvido Bluetooth",   "codigo": "ELET-001",
        "categoria": "eletrônicos",           "quantidade": 12,
        "preco": 149.90,                      "estoque_min": 3,
        "descricao": "Sem fio, bateria 20h, cancelamento de ruído",
        "fornecedor": "TechStore",
    },
    {
        "nome": "Carregador USB-C 65W",       "codigo": "ELET-002",
        "categoria": "eletrônicos",           "quantidade": 2,  # estoque baixo para testar alerta
        "preco": 89.90,                       "estoque_min": 5,
        "descricao": "Carga rápida, compatível com notebook e celular",
        "fornecedor": "TechStore",
    },
    {
        "nome": "Mouse Sem Fio",              "codigo": "INFO-001",
        "categoria": "informática",           "quantidade": 18,
        "preco": 79.90,                       "estoque_min": 4,
        "descricao": "2.4GHz, 1600 DPI, pilha incluída",
        "fornecedor": "InfoParts",
    },
    {
        "nome": "Teclado Mecânico ABNT2",     "codigo": "INFO-002",
        "categoria": "informática",           "quantidade": 8,
        "preco": 249.90,                      "estoque_min": 2,
        "descricao": "Switch Blue, RGB, USB",
        "fornecedor": "InfoParts",
    },
    {
        "nome": "Bola de Futebol Campo",      "codigo": "ESPT-001",
        "categoria": "esportes",              "quantidade": 10,
        "preco": 119.90,                      "estoque_min": 2,
        "descricao": "Tamanho 5, termotec, modelo oficial",
        "fornecedor": "SportMax",
    },
    {
        "nome": "Whey Protein 1kg",           "codigo": "ALIM-001",
        "categoria": "alimentos",             "quantidade": 25,
        "preco": 139.90,                      "estoque_min": 5,
        "descricao": "Chocolate, 78% proteína por porção",
        "fornecedor": "NutriPlus",
    },
]


def popular_exemplos() -> None:
    """Insere os produtos de exemplo apenas se o banco estiver vazio."""
    if carregar_dados(ARQUIVO_PRODUTOS):
        return

    print("Carregando dados de exemplo para testes...")

    # Carrega uma vez, adiciona todos, salva uma vez
    produtos = carregar_dados(ARQUIVO_PRODUTOS)
    for produto in _EXEMPLOS:
        produtos.append(produto)
    salvar_dados(ARQUIVO_PRODUTOS, produtos)

    for produto in _EXEMPLOS:
        registrar_movimento(
            produto["codigo"], produto["nome"],
            "entrada_inicial", produto["quantidade"]
        )

    print(f"  {len(_EXEMPLOS)} produtos de exemplo carregados!\n")
