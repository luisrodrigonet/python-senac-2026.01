import json
import os
import sys
from pathlib import Path

# 1. Definição dinâmica de caminhos a partir da pasta _script
DIRETORIO_SCRIPT = Path(__file__).resolve().parent          # pasta _script
DIRETORIO_RAIZ = DIRETORIO_SCRIPT.parent                   # raiz do projeto (onde está manage.py)
CAMINHO_JSON = DIRETORIO_RAIZ / "_dados_iniciais" / "categorias.json"

# 2. Adiciona a raiz do projeto ao sys.path para permitir imports de apps e configurações
if str(DIRETORIO_RAIZ) not in sys.path:
    sys.path.insert(0, str(DIRETORIO_RAIZ))

# 3. Configuração do ambiente Django
# Altere 'meu_projeto.settings' caso seu módulo de settings tenha outro nome
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from django.db import transaction
from apps.produtos.models import Categoria


def carregar_categorias(caminho_arquivo: Path) -> None:
    if not caminho_arquivo.exists():
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        sys.exit(1)

    with open(caminho_arquivo, mode="r", encoding="utf-8") as f:
        try:
            dados = json.load(f)
        except json.JSONDecodeError as err:
            print(f"Erro ao decodificar JSON: {err}")
            sys.exit(1)

    criadas = 0
    ignoradas = 0

    print(f"Lendo dados de: {caminho_arquivo}")
    print("Iniciando importação no banco de dados SQLite...")

    # Bloco atômico: garante integridade e melhora muito a performance no SQLite
    with transaction.atomic():
        for item in dados:
            nome = item.get("nome", "").strip()
            descricao = item.get("descricao", "").strip()

            if not nome:
                continue

            # get_or_create verifica se já existe pelo campo 'nome' (unique=True no model)
            _, created = Categoria.objects.get_or_create(
                nome=nome,
                defaults={"descricao": descricao},
            )

            if created:
                criadas += 1
                print(f" [+] Categoria inserida: {nome}")
            else:
                ignoradas += 1
                print(f" [~] Já existente (ignorada): {nome}")

    print("\n--- Relatório Final ---")
    print(f"Novas categorias adicionadas: {criadas}")
    print(f"Categorias pré-existentes:    {ignoradas}")
    print(f"Total avaliado:               {criadas + ignoradas}")


if __name__ == "__main__":
    carregar_categorias(CAMINHO_JSON)