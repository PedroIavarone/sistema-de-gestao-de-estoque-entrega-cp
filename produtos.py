from dados import carregar_dados, salvar_dados, ARQUIVO_PRODUTOS
from categorias import escolher_categoria, gerar_codigo
from estoque import registrar_movimento
from utils import ler_inteiro, ler_decimal


def cadastrar_produto() -> None:
    print("\n--- CADASTRAR PRODUTO ---")
    nome = input("Nome do produto: ").strip()

    categoria, prefixo = escolher_categoria()
    codigo = gerar_codigo(prefixo)
    print(f"  Código gerado automaticamente: {codigo}")

    quantidade  = ler_inteiro("Quantidade em estoque: ", minimo=0)
    preco       = ler_decimal("Preço de venda (R$): ", minimo=0.01)
    descricao   = input("Descrição: ").strip()
    fornecedor  = input("Fornecedor: ").strip()
    estoque_min = ler_inteiro("Quantidade mínima para alerta de estoque baixo: ", minimo=0)

    produto = {
        "nome":        nome,
        "codigo":      codigo,
        "categoria":   categoria,
        "quantidade":  quantidade,
        "preco":       preco,
        "descricao":   descricao,
        "fornecedor":  fornecedor,
        "estoque_min": estoque_min
    }

    produtos = carregar_dados(ARQUIVO_PRODUTOS)
    produtos.append(produto)
    salvar_dados(ARQUIVO_PRODUTOS, produtos)

    registrar_movimento(codigo, nome, "entrada_inicial", quantidade)
    print(f"\nProduto '{nome}' cadastrado com sucesso!  [{codigo}]")


def listar_produtos() -> None:
    produtos = carregar_dados(ARQUIVO_PRODUTOS)
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\n--- LISTA DE PRODUTOS ---")
    print(f"{'CÓDIGO':<12} {'NOME':<28} {'CATEGORIA':<14} {'QTD':>5} {'PREÇO':>10}  STATUS")
    print("-" * 78)
    for p in produtos:
        alerta = "⚠ BAIXO" if p["quantidade"] <= p["estoque_min"] else "OK"
        print(f"{p['codigo']:<12} {p['nome']:<28} {p['categoria']:<14} "
              f"{p['quantidade']:>5} R${p['preco']:>9.2f}  {alerta}")


def buscar_produto(codigo: str) -> dict | None:
    """Retorna o dicionário do produto pelo código, ou None se não encontrado."""
    for p in carregar_dados(ARQUIVO_PRODUTOS):
        if p["codigo"] == codigo:
            return p
    return None
