def ler_inteiro(mensagem: str, minimo: int = 0) -> int:
    """Lê um número inteiro do teclado, rejeitando letras e valores abaixo do mínimo."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor < minimo:
                print(f"  Valor inválido. Digite um número maior ou igual a {minimo}.")
            else:
                return valor
        except ValueError:
            print("  Entrada inválida. Digite apenas números inteiros.")


def ler_decimal(mensagem: str, minimo: float = 0.0, maximo: float = None) -> float:
    """Lê um número decimal do teclado, rejeitando letras e valores fora do intervalo."""
    while True:
        try:
            valor = float(input(mensagem))
            if valor < minimo:
                print(f"  Valor inválido. Digite um número maior ou igual a {minimo}.")
            elif maximo is not None and valor > maximo:
                print(f"  Valor inválido. Digite um número menor ou igual a {maximo}.")
            else:
                return valor
        except ValueError:
            print("  Entrada inválida. Digite apenas números.")
