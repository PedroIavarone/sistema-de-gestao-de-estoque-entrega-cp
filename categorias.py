from dados import carregar_dados, ARQUIVO_PRODUTOS

# Formato do código gerado: PREFIXO-NNN  (ex: VEST-003)
CATEGORIAS = {
    "1":  ("vestuário",   "VEST"),
    "2":  ("calçados",    "CALC"),
    "3":  ("eletrônicos", "ELET"),
    "4":  ("informática", "INFO"),
    "5":  ("alimentos",   "ALIM"),
    "6":  ("bebidas",     "BEBV"),
    "7":  ("móveis",      "MOVE"),
    "8":  ("esportes",    "ESPT"),
    "9":  ("beleza",      "BELE"),
    "10": ("automotivo",  "AUTO"),
    "11": ("livros",      "LIVR"),
    "12": ("ferramentas", "FERR"),
    "13": ("brinquedos",  "BRNQ"),
    "14": ("outro",       "OUTR"),
}


def _proximo_numero(prefixo: str) -> int:
    """Retorna o próximo número sequencial para um dado prefixo."""
    maior = 0
    for p in carregar_dados(ARQUIVO_PRODUTOS):
        if p["codigo"].startswith(prefixo + "-"):
            parte = p["codigo"].split("-")[-1]
            if parte.isdigit():
                maior = max(maior, int(parte))
    return maior + 1


def gerar_codigo(prefixo: str) -> str:
    """Gera o próximo código no padrão PREFIXO-NNN."""
    return f"{prefixo}-{_proximo_numero(prefixo):03d}"


def escolher_categoria() -> tuple[str, str]:
    """Exibe o menu de categorias e retorna (nome_categoria, prefixo)."""
    print("\n  Categorias disponíveis:")
    print("  " + "-" * 36)
    for k, (nome, pref) in CATEGORIAS.items():
        print(f"  [{k:>2}] {nome:<15}  →  código: {pref}-NNN")
    print("  " + "-" * 36)

    while True:
        opcao = input("  Escolha o número da categoria: ").strip()
        if opcao in CATEGORIAS:
            nome, prefixo = CATEGORIAS[opcao]
            return nome, prefixo
        print("  Opção inválida, tente novamente.")
