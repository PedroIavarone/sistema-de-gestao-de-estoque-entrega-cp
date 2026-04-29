from datetime import datetime
from dados import carregar_dados, salvar_dados, ARQUIVO_PRODUTOS, ARQUIVO_VENDAS
from produtos import listar_produtos, buscar_produto
from estoque import registrar_movimento, verificar_alerta
from utils import ler_inteiro, ler_decimal


def registrar_venda() -> None:
    print("\n--- REGISTRAR VENDA ---")
    cliente = input("Nome do cliente: ").strip()
    itens   = []
    total   = 0.0

    while True:
        listar_produtos()
        codigo = input("\nCódigo do produto (ou 'fim' para encerrar): ").strip().upper()
        if codigo == "FIM":
            break

        produto = buscar_produto(codigo)
        if not produto:
            print("Produto não encontrado.")
            continue

        if produto["quantidade"] == 0:
            print("Produto sem estoque disponível.")
            continue

        qtd = ler_inteiro(f"Quantidade (estoque disponível: {produto['quantidade']}): ", minimo=1)
        if qtd > produto["quantidade"]:
            print("Quantidade solicitada maior do que o estoque disponível.")
            continue

        desconto_pct       = ler_decimal("Desconto em % (0 se não houver): ", minimo=0, maximo=100)
        preco_unit         = produto["preco"]
        preco_com_desconto = preco_unit * (1 - desconto_pct / 100)
        subtotal           = preco_com_desconto * qtd

        itens.append({
            "codigo":       codigo,
            "produto":      produto["nome"],
            "quantidade":   qtd,
            "preco_unit":   preco_unit,
            "desconto_pct": desconto_pct,
            "subtotal":     subtotal
        })
        total += subtotal
        print(f"  → Adicionado: {produto['nome']} x{qtd}  R${subtotal:.2f}")

    if not itens:
        print("Nenhum item adicionado. Venda cancelada.")
        return

    # Desconta cada item do estoque e registra a movimentação
    produtos = carregar_dados(ARQUIVO_PRODUTOS)
    for item in itens:
        for p in produtos:
            if p["codigo"] == item["codigo"]:
                p["quantidade"] -= item["quantidade"]
                registrar_movimento(item["codigo"], item["produto"], "venda", item["quantidade"])
                verificar_alerta(p)
    salvar_dados(ARQUIVO_PRODUTOS, produtos)

    vendas       = carregar_dados(ARQUIVO_VENDAS)
    numero_venda = len(vendas) + 1
    venda = {
        "numero":  numero_venda,
        "data":    datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "cliente": cliente,
        "itens":   itens,
        "total":   total
    }
    vendas.append(venda)
    salvar_dados(ARQUIVO_VENDAS, vendas)

    emitir_recibo(venda)


def emitir_recibo(venda: dict) -> None:
    print("\n" + "=" * 52)
    print("             RECIBO DE VENDA")
    print("=" * 52)
    print(f"Nº da Venda : {venda['numero']}")
    print(f"Data/Hora   : {venda['data']}")
    print(f"Cliente     : {venda['cliente']}")
    print("-" * 52)
    print(f"{'PRODUTO':<22} {'QTD':>4} {'UNIT':>8} {'DESC':>6} {'SUBTOTAL':>9}")
    print("-" * 52)
    for item in venda["itens"]:
        print(f"{item['produto']:<22} {item['quantidade']:>4} "
              f"R${item['preco_unit']:>6.2f} {item['desconto_pct']:>5.1f}% "
              f"R${item['subtotal']:>7.2f}")
    print("-" * 52)
    print(f"{'TOTAL':>43} R${venda['total']:>7.2f}")
    print("=" * 52)
    print("          Obrigado pela compra!")
    print("=" * 52)
