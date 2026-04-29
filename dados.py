import json
import os

ARQUIVO_PRODUTOS   = "produtos.json"
ARQUIVO_VENDAS     = "vendas.json"
ARQUIVO_MOVIMENTOS = "movimentos.json"


def carregar_dados(arquivo: str) -> list:
    """Lê um arquivo JSON e retorna a lista de dados. Retorna [] se não existir."""
    if not os.path.exists(arquivo):
        return []
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Erro: o arquivo '{arquivo}' está corrompido. Iniciando com lista vazia.")
        return []
    except OSError as e:
        print(f"Erro ao ler o arquivo '{arquivo}': {e}")
        return []


def salvar_dados(arquivo: str, dados: list) -> None:
    """Grava a lista de dados em um arquivo JSON formatado."""
    try:
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
    except OSError as e:
        print(f"Erro ao salvar o arquivo '{arquivo}': {e}")
