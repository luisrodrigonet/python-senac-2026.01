import json
import os
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

# 1. Configuração dos caminhos relativos ao projeto
DIRETORIO_SCRIPT = Path(__file__).resolve().parent
DIRETORIO_RAIZ = DIRETORIO_SCRIPT.parent
CAMINHO_JSON = DIRETORIO_RAIZ / "_dados_iniciais" / "produtos.json"

# 2. Inserção do diretório raiz no sys.path
if str(DIRETORIO_RAIZ) not in sys.path:
    sys.path.insert(0, str(DIRETORIO_RAIZ))

# 3. Inicialização do ambiente Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from django.db import transaction
from apps.produtos.models import Categoria, Produto


def carregar_produtos(caminho_arquivo: Path) -> None:
    if not caminho_arquivo.exists():
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        sys.exit(1)

    with open(caminho_arquivo, mode="r", encoding="utf-8") as f:
        try:
            dados = json.load(f)
        except json.JSONDecodeError as err:
            print(f"Erro ao decodificar JSON: {err}")
            sys.exit(1)

    # Cache local de categorias para evitar queries repetitivas no banco
    categorias_cache = {cat.nome.lower(): cat for cat in Categoria.objects.all()}

    criados = 0
    ignorados = 0
    erros = 0

    print(f"Lendo dados de: {caminho_arquivo}")
    print("Iniciando processamento dos produtos no SQLite...")

    with transaction.atomic():
        for item in dados:
            nome = item.get("nome", "").strip()
            nome_categoria = item.get("categoria", "").strip()
            descricao = item.get("descricao", "").strip()
            preco_str = str(item.get("preco", "0.00"))
            estoque = item.get("quantidade_estoque", 0)

            if not nome or not nome_categoria:
                print(f" [!] Registro inválido ignorado: {item}")
                erros += 1
                continue

            # Busca a categoria no cache (case-insensitive)
            categoria = categorias_cache.get(nome_categoria.lower())
            if not categoria:
                print(f" [!] Categoria '{nome_categoria}' não encontrada para o produto '{nome}'.")
                erros += 1
                continue

            try:
                preco = Decimal(preco_str)
                quantidade_estoque = int(estoque)
            except (InvalidOperation, ValueError) as conv_err:
                print(f" [!] Erro de conversão nos valores do produto '{nome}': {conv_err}")
                erros += 1
                continue

            # get_or_create verifica se já existe o produto com o mesmo nome na categoria
            _, created = Produto.objects.get_or_create(
                nome=nome,
                categoria=categoria,
                defaults={
                    "descricao": descricao,
                    "preco": preco,
                    "quantidade_estoque": quantidade_estoque,
                },
            )

            if created:
                criados += 1
                print(f" [+] Produto inserido: {nome} (R$ {preco})")
            else:
                ignorados += 1
                print(f" [~] Já existente (ignorado): {nome}")

    print("\n--- Relatório Final de Produtos ---")
    print(f"Novos produtos adicionados: {criados}")
    print(f"Produtos pré-existentes:    {ignorados}")
    print(f"Falhas/Inconsistências:     {erros}")
    print(f"Total avaliado:             {criados + ignorados + erros}")


if __name__ == "__main__":
    carregar_produtos(CAMINHO_JSON)