from dados import carregar_dados, ARQUIVO_PRODUTOS, ARQUIVO_VENDAS, ARQUIVO_MOVIMENTOS


def relatorio_vendas() -> None:
    vendas = carregar_dados(ARQUIVO_VENDAS)
    if not vendas:
        print("Nenhuma venda registrada.")
        return

    print("\n" + "=" * 60)
    print("            RELATÓRIO DE VENDAS")
    print("=" * 60)

    total_geral = 0.0
    for v in vendas:
        print(f"\nVenda #{v['numero']}  |  {v['data']}  |  Cliente: {v['cliente']}")
        print(f"  {'PRODUTO':<25} {'QTD':>4} {'SUBTOTAL':>10}")
        for item in v["itens"]:
            print(f"  {item['produto']:<25} {item['quantidade']:>4}  R${item['subtotal']:>8.2f}")
        print(f"  {'Total da venda:':>32} R${v['total']:>8.2f}")
        total_geral += v["total"]

    print("\n" + "-" * 60)
    print(f"  TOTAL GERAL DE VENDAS: R${total_geral:.2f}")
    print("=" * 60)


def relatorio_estoque() -> None:
    produtos = carregar_dados(ARQUIVO_PRODUTOS)
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\n" + "=" * 72)
    print("               RELATÓRIO DE ESTOQUE ATUAL")
    print("=" * 72)
    print(f"{'CÓDIGO':<12} {'PRODUTO':<28} {'CATEGORIA':<14} {'QTD':>5} {'MÍN':>5}  STATUS")
    print("-" * 72)
    for p in produtos:
        status = "⚠ BAIXO" if p["quantidade"] <= p["estoque_min"] else "OK"
        print(f"{p['codigo']:<12} {p['nome']:<28} {p['categoria']:<14} "
              f"{p['quantidade']:>5} {p['estoque_min']:>5}  {status}")
    print("=" * 72)


def historico_movimentacoes() -> None:
    movimentos = carregar_dados(ARQUIVO_MOVIMENTOS)
    if not movimentos:
        print("Nenhuma movimentação registrada.")
        return

    print("\n" + "=" * 68)
    print("             HISTÓRICO DE MOVIMENTAÇÕES")
    print("=" * 68)
    print(f"{'DATA/HORA':<21} {'CÓDIGO':<12} {'PRODUTO':<22} {'TIPO':<16} {'QTD':>4}")
    print("-" * 68)
    for m in movimentos:
        print(f"{m['data']:<21} {m['codigo']:<12} {m['produto']:<22} "
              f"{m['tipo']:<16} {m['quantidade']:>4}")
    print("=" * 68)
