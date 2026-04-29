from exemplos   import popular_exemplos
from produtos   import cadastrar_produto, listar_produtos
from estoque    import adicionar_estoque, remover_estoque, atualizar_estoque
from vendas     import registrar_venda
from relatorios import relatorio_vendas, relatorio_estoque, historico_movimentacoes


def menu() -> None:
    popular_exemplos()  # só age na 1ª execução

    opcoes = {
        "1": ("Cadastrar produto",          cadastrar_produto),
        "2": ("Listar produtos",            listar_produtos),
        "3": ("Adicionar ao estoque",       adicionar_estoque),
        "4": ("Remover do estoque",         remover_estoque),
        "5": ("Atualizar estoque",          atualizar_estoque),
        "6": ("Registrar venda",            registrar_venda),
        "7": ("Relatório de vendas",        relatorio_vendas),
        "8": ("Relatório de estoque",       relatorio_estoque),
        "9": ("Histórico de movimentações", historico_movimentacoes),
        "0": ("Sair",                       None),
    }

    while True:
        print("\n" + "=" * 42)
        print("     SISTEMA DE CONTROLE DE ESTOQUE")
        print("=" * 42)
        for k, (desc, _) in opcoes.items():
            print(f"  [{k}] {desc}")
        print("=" * 42)

        try:
            escolha = input("Escolha uma opção: ").strip()
        except KeyboardInterrupt:
            print("\nEncerrando o sistema. Até logo!")
            break

        if escolha == "0":
            print("Encerrando o sistema. Até logo!")
            break
        elif escolha in opcoes:
            try:
                _, funcao = opcoes[escolha]
                funcao()
            except Exception as e:
                print(f"Erro inesperado: {e}")
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
