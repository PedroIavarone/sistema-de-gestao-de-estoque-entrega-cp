from datetime import datetime
from dados import carregar_dados, salvar_dados, ARQUIVO_PRODUTOS, ARQUIVO_MOVIMENTOS
from utils import ler_inteiro


def registrar_movimento(codigo: str, nome: str, tipo: str, quantidade: int) -> None:
    """Adiciona uma linha no histórico de movimentações."""
    movimentos = carregar_dados(ARQUIVO_MOVIMENTOS)
    movimentos.append({
        "data":       datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "codigo":     codigo,
        "produto":    nome,
        "tipo":       tipo,
        "quantidade": quantidade
    })
    salvar_dados(ARQUIVO_MOVIMENTOS, movimentos)


def verificar_alerta(produto: dict) -> None:
    """Imprime um aviso se o produto atingiu o estoque mínimo."""
    if produto["quantidade"] <= produto["estoque_min"]:
        print(f"\n*** ALERTA: estoque baixo para '{produto['nome']}' "
              f"(restam {produto['quantidade']} unidades) ***")


def adicionar_estoque() -> None:
    from produtos import listar_produtos  # import local para evitar dependência circular
    listar_produtos()
    codigo   = input("\nCódigo do produto: ").strip().upper()
    produtos = carregar_dados(ARQUIVO_PRODUTOS)

    for p in produtos:
        if p["codigo"] == codigo:
            qtd = ler_inteiro(f"Quantas unidades adicionar? (atual: {p['quantidade']}): ", minimo=1)
            p["quantidade"] += qtd
            salvar_dados(ARQUIVO_PRODUTOS, produtos)
            registrar_movimento(codigo, p["nome"], "entrada", qtd)
            print(f"Estoque atualizado: '{p['nome']}' agora tem {p['quantidade']} unidades.")
            return

    print("Produto não encontrado.")


def remover_estoque() -> None:
    from produtos import listar_produtos
    listar_produtos()
    codigo   = input("\nCódigo do produto: ").strip().upper()
    produtos = carregar_dados(ARQUIVO_PRODUTOS)

    for p in produtos:
        if p["codigo"] == codigo:
            qtd = ler_inteiro(f"Quantas unidades remover? (atual: {p['quantidade']}): ", minimo=1)
            if qtd > p["quantidade"]:
                print("Quantidade insuficiente no estoque.")
                return
            p["quantidade"] -= qtd
            salvar_dados(ARQUIVO_PRODUTOS, produtos)
            registrar_movimento(codigo, p["nome"], "saída_manual", qtd)
            print(f"Remoção registrada. '{p['nome']}' agora tem {p['quantidade']} unidades.")
            verificar_alerta(p)
            return

    print("Produto não encontrado.")


def atualizar_estoque() -> None:
    from produtos import listar_produtos
    listar_produtos()
    codigo   = input("\nCódigo do produto: ").strip().upper()
    produtos = carregar_dados(ARQUIVO_PRODUTOS)

    for p in produtos:
        if p["codigo"] == codigo:
            nova_qtd = ler_inteiro(f"Nova quantidade (atual: {p['quantidade']}): ", minimo=0)
            diff     = nova_qtd - p["quantidade"]
            tipo     = "ajuste_positivo" if diff >= 0 else "ajuste_negativo"
            p["quantidade"] = nova_qtd
            salvar_dados(ARQUIVO_PRODUTOS, produtos)
            registrar_movimento(codigo, p["nome"], tipo, abs(diff))
            print(f"Estoque de '{p['nome']}' ajustado para {nova_qtd} unidades.")
            verificar_alerta(p)
            return

    print("Produto não encontrado.")
