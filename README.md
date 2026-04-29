# Sistema de Controle de Estoque

Sistema de gerenciamento de estoque desenvolvido em Python, com cadastro de produtos, controle de entradas e saídas, registro de vendas e geração de relatórios.

---

## Como executar

**Pré-requisito:** Python 3.10 ou superior instalado.

```bash
python main.py
```

Na primeira execução, 11 produtos de exemplo são carregados automaticamente para facilitar os testes.

---

## Funcionalidades

### Cadastro de produtos
- Código gerado automaticamente com base na categoria (ex: `VEST-001`, `ELET-003`)
- Campos: nome, categoria, quantidade, preço, descrição, fornecedor e estoque mínimo

### Gestão de estoque
- Adicionar, remover ou ajustar manualmente a quantidade de um produto
- Alerta automático quando o estoque atinge o nível mínimo

### Vendas
- Registro de venda com múltiplos produtos
- Aplicação de desconto por item
- Redução automática do estoque ao confirmar a venda
- Emissão de recibo no terminal

### Relatórios
- **Relatório de vendas:** histórico completo com total por venda e total geral
- **Relatório de estoque:** situação atual de todos os produtos com indicação de estoque baixo
- **Histórico de movimentações:** todas as entradas e saídas registradas com data e tipo

---

## Tratamento de erros

O sistema possui tratamento de erros em três camadas:

**Validação de entrada (`utils.py`)**
- Qualquer input numérico que receber letras exibe uma mensagem e pede novamente, sem travar o programa
- Valores fora do intervalo permitido (ex: desconto acima de 100%, quantidade negativa) são rejeitados com aviso

**Leitura e gravação de arquivos (`dados.py`)**
- Arquivo JSON corrompido: o sistema avisa e continua com lista vazia em vez de travar
- Erro de permissão ou disco cheio: exibe a mensagem do sistema operacional

**Menu principal (`main.py`)**
- `Ctrl+C`: encerra o sistema de forma limpa
- Erros inesperados em qualquer opção: exibe a mensagem de erro e volta ao menu sem fechar o programa

---

## Estrutura de arquivos

```
├── main.py          # Menu principal e ponto de entrada do sistema
├── dados.py         # Leitura e gravação dos arquivos JSON
├── utils.py         # Funções de validação de entrada (ler_inteiro, ler_decimal)
├── categorias.py    # Tabela de categorias e geração automática de códigos
├── produtos.py      # Cadastro, listagem e busca de produtos
├── estoque.py       # Movimentações, alertas e operações de estoque
├── vendas.py        # Registro de vendas e emissão de recibo
├── relatorios.py    # Relatórios de vendas, estoque e histórico
└── exemplos.py      # Produtos pré-carregados para teste
```

Os dados são salvos em arquivos `.json` na mesma pasta:

```
├── produtos.json
├── vendas.json
└── movimentos.json
```

> Esses arquivos são gerados automaticamente na primeira execução e estão listados no `.gitignore`.

---

## Categorias e prefixos de código

| # | Categoria    | Prefixo | Exemplo    |
|---|--------------|---------|------------|
| 1 | Vestuário    | VEST    | VEST-001   |
| 2 | Calçados     | CALC    | CALC-001   |
| 3 | Eletrônicos  | ELET    | ELET-001   |
| 4 | Informática  | INFO    | INFO-001   |
| 5 | Alimentos    | ALIM    | ALIM-001   |
| 6 | Bebidas      | BEBV    | BEBV-001   |
| 7 | Móveis       | MOVE    | MOVE-001   |
| 8 | Esportes     | ESPT    | ESPT-001   |
| 9 | Beleza       | BELE    | BELE-001   |
|10 | Automotivo   | AUTO    | AUTO-001   |
|11 | Livros       | LIVR    | LIVR-001   |
|12 | Ferramentas  | FERR    | FERR-001   |
|13 | Brinquedos   | BRNQ    | BRNQ-001   |
|14 | Outro        | OUTR    | OUTR-001   |

O número é sequencial por categoria. Ao cadastrar o segundo produto de vestuário, o código gerado será `VEST-002` automaticamente.

---

## Exemplo de uso

```
  [1] Cadastrar produto
  [2] Listar produtos
  [3] Adicionar ao estoque
  [4] Remover do estoque
  [5] Atualizar estoque
  [6] Registrar venda
  [7] Relatório de vendas
  [8] Relatório de estoque
  [9] Histórico de movimentações
  [0] Sair
```

---

## Tecnologias utilizadas

- **Python 3.10+**
- Biblioteca padrão: `json`, `os`, `datetime` — sem dependências externas

---

## Integrantes do grupo

| Nome                              | RM       |
|-----------------------------------|----------|
| Alexandre Silva Alves             | RM567415 |
| Julia Marcela de Faria Bonifacio  | RM566673 |
| Mariana Pergentino Fonseca        | RM568252 |
| Pedro Iavarone Custódio           | RM567638 |
