# produtos/admin.py

from django.contrib import admin

from .models import (
    Categoria,
    Cliente,
    ComentarioAvaliacao,
    EnderecoEntrega,
    ItemPedido,
    Pedido,
    Produto,
)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """
    Configuração do painel administrativo para Categoria.
    """

    # Colunas exibidas na listagem.
    list_display = ["id", "nome", "descricao"]

    # Campos pesquisáveis na caixa de busca.
    search_fields = ["nome", "descricao"]

    # Ordenação padrão da listagem.
    ordering = ["nome"]


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    """
    Configuração do painel administrativo para Produto.
    """

    list_display = [
        "id",
        "nome",
        "categoria",
        "preco",
        "quantidade_estoque",
        "criado_em",
    ]

    # Filtros laterais no Admin.
    list_filter = ["categoria", "criado_em"]

    # Permite pesquisar por nome do produto e nome da categoria.
    # O duplo underscore atravessa relacionamentos.
    search_fields = ["nome", "categoria__nome"]

    # Campos que não podem ser alterados manualmente.
    readonly_fields = ["criado_em", "atualizado_em"]


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """
    Configuração do painel administrativo para Cliente.
    """

    list_display = [
        "id",
        "usuario",
        "telefone",
        "sexo",
        "cpf",
    ]

    search_fields = [
        "usuario__username",
        "usuario__first_name",
        "usuario__last_name",
        "cpf",
    ]

    list_filter = ["sexo"]


@admin.register(EnderecoEntrega)
class EnderecoEntregaAdmin(admin.ModelAdmin):
    """
    Configuração do painel administrativo para Endereço de entrega.
    """

    list_display = [
        "id",
        "cliente",
        "logradouro",
        "numero",
        "cidade",
        "estado",
        "cep",
    ]

    search_fields = [
        "cliente__usuario__username",
        "cidade",
        "cep",
    ]

    list_filter = ["estado", "cidade"]


class ItemPedidoInline(admin.TabularInline):
    """
    Exibe e permite cadastrar itens dentro da página do Pedido.

    TabularInline mostra os itens em formato de tabela.
    """

    model = ItemPedido
    extra = 1  # Quantidade de linhas extras exibidas para novos itens


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    """
    Configuração do painel administrativo para Pedido.
    """

    list_display = [
        "id",
        "cliente",
        "status",
        "endereco_entrega",
        "criado_em",
        "total_pedido",
    ]

    list_filter = ["status", "criado_em"]

    search_fields = [
        "cliente__usuario__username",
        "cliente__usuario__first_name",
        "cliente__usuario__last_name",
    ]

    # Exibe os itens diretamente na tela de edição do pedido.
    inlines = [ItemPedidoInline]

    readonly_fields = ["criado_em", "atualizado_em"]


@admin.register(ComentarioAvaliacao)
class ComentarioAvaliacaoAdmin(admin.ModelAdmin):
    """
    Configuração do painel administrativo para avaliações.
    """

    list_display = [
        "id",
        "produto",
        "cliente",
        "nota",
        "criado_em",
    ]

    list_filter = ["nota", "criado_em"]

    search_fields = [
        "produto__nome",
        "cliente__usuario__username",
        "texto",
    ]


# Registro simples, útil quando não há personalização necessária.
# admin.site.register(ItemPedido)
