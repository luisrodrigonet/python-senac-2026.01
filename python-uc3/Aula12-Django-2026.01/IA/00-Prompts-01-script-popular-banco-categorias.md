Você é um desenvolvedor senior especialista em desenvolvimento python, django e sqliite.
Com base no model listado abaixo, crie um script para inserir 20 categorias de produtos no banco de dados sqlite.
O script não deve inserir uma categoria caso ela já tenha sido adicionada. Os dados das categorias devem ser lidos de um arquivo externo
O script será armazenado na pasta _script e o arquivo com os dados dentro da pasta _dados_iniciais, ambos dentro da pasta do projeto

Model:

# produtos/models.py

from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    """
    Agrupa produtos por tipo de uso.

    Exemplos:
    - Esportivo
    - Casual
    - Social
    """

    # Nome obrigatório da categoria.
    # max_length=100 limita o campo a 100 caracteres no banco de dados.
    nome = models.CharField(
        max_length=100,
        unique=True,  # Impede duas categorias com o mesmo nome
        verbose_name="Nome",
    )

    # TextField é indicado para textos longos.
    # blank=True permite que o campo fique vazio em formulários.
    # null=True permite valor nulo no banco de dados.
    descricao = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descrição",
    )

    class Meta:
        # Nome legível exibido no Django Admin.
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

        # Ordena as categorias em ordem alfabética pelo nome.
        ordering = ["nome"]

    def __str__(self):
        # Representação textual do objeto.
        return self.nome


class Produto(models.Model):
    """
    Representa um calçado disponível para venda.
    """

    categoria = models.ForeignKey(
        to=Categoria,
        # CASCADE: ao excluir a categoria, os produtos vinculados também são excluídos.
        on_delete=models.CASCADE,
        # Nome usado para acessar os produtos de uma categoria.
        # Exemplo: categoria.produtos.all()
        related_name="produtos",
        verbose_name="Categoria",
    )

    nome = models.CharField(
        max_length=150,
        verbose_name="Nome do produto",
    )

    descricao = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descrição",
    )

    # DecimalField é o campo correto para valores monetários.
    # Nunca use FloatField para dinheiro, pois pode gerar imprecisões.
    # max_digits=10 permite até 10 dígitos no total.
    # decimal_places=2 reserva duas casas para centavos.
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Preço",
    )

    quantidade_estoque = models.PositiveIntegerField(
        default=0,
        verbose_name="Quantidade em estoque",
    )

    # Define automaticamente a data e hora de criação.
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em",
    )

    # Atualiza a data e hora sempre que o produto for salvo.
    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em",
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    """
    Perfil estendido do usuário padrão do Django.

    Cada Cliente está ligado a apenas um User.
    """

    class Sexo(models.TextChoices):
        """
        Opções inclusivas para o campo sexo.
        """

        FEMININO = "F", "Feminino"
        MASCULINO = "M", "Masculino"
        NAO_INFORMADO = "N", "Prefiro não informar"
        OUTRO = "O", "Outro"

    # OneToOneField cria uma relação um-para-um.
    # Um User pode ter apenas um Cliente.
    # CASCADE: se o User for excluído, o Cliente também será.
    usuario = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name="cliente",
        verbose_name="Usuário",
    )

    telefone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Telefone",
    )

    # ImageField exige a biblioteca Pillow.
    # pip install pillow
    foto = models.ImageField(
        upload_to="clientes/fotos/",
        blank=True,
        null=True,
        verbose_name="Foto de perfil",
    )  

    sexo = models.CharField(
        max_length=1,
        choices=Sexo.choices,
        default=Sexo.NAO_INFORMADO,
        verbose_name="Sexo",
    )

    nome_social = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name="Nome social",
    )

    data_nascimento = models.DateField(
        blank=True,
        null=True,
        verbose_name="Data de nascimento",
    )

    cpf = models.CharField(
        max_length=14,
        unique=True,
        verbose_name="CPF",
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.usuario.get_full_name() or self.usuario.username


class EnderecoEntrega(models.Model):
    """
    Endereço utilizado para entrega de pedidos.

    Um cliente pode ter vários endereços.
    """

    cliente = models.ForeignKey(
        to=Cliente,
        on_delete=models.CASCADE,
        related_name="enderecos_entrega",
        verbose_name="Cliente",
    )

    logradouro = models.CharField(
        max_length=200,
        verbose_name="Logradouro",
    )

    numero = models.CharField(
        max_length=20,
        verbose_name="Número",
    )

    complemento = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Complemento",
    )

    bairro = models.CharField(
        max_length=100,
        verbose_name="Bairro",
    )

    cidade = models.CharField(
        max_length=100,
        verbose_name="Cidade",
    )

    estado = models.CharField(
        max_length=2,
        verbose_name="Estado",
    )

    cep = models.CharField(
        max_length=9,
        verbose_name="CEP",
    )

    class Meta:
        verbose_name = "Endereço de entrega"
        verbose_name_plural = "Endereços de entrega"
        ordering = ["cliente", "cidade"]

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.cidade}/{self.estado}"


class Pedido(models.Model):
    """
    Representa uma compra realizada por um cliente.
    """

    class Status(models.TextChoices):
        """
        Situações possíveis de um pedido.
        """

        PENDENTE = "pendente", "Pendente"
        PAGO = "pago", "Pago"
        ENVIADO = "enviado", "Enviado"
        ENTREGUE = "entregue", "Entregue"
        CANCELADO = "cancelado", "Cancelado"

    cliente = models.ForeignKey(
        to=Cliente,
        on_delete=models.CASCADE,
        related_name="pedidos",
        verbose_name="Cliente",
    )

    endereco_entrega = models.ForeignKey(
        to=EnderecoEntrega,
        on_delete=models.PROTECT,
        related_name="pedidos",
        verbose_name="Endereço de entrega",
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDENTE,
        verbose_name="Status",
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em",
    )

    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em",
    )

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ["-criado_em"]

    def __str__(self):
        return f"Pedido #{self.pk} - {self.cliente}"

    def total_pedido(self):
        """
        Calcula o valor total do pedido.

        O total considera a quantidade de cada item multiplicada
        pelo preço registrado no momento da compra.
        """
        total = Decimal("0.00")

        for item in self.itens.all():
            total += item.quantidade * item.preco_unitario

        return total


class ItemPedido(models.Model):
    """
    Representa um produto dentro de um pedido.

    O preço unitário é salvo no momento da compra para preservar
    o valor histórico, mesmo se o preço do produto mudar depois.
    """

    pedido = models.ForeignKey(
        to=Pedido,
        on_delete=models.CASCADE,
        related_name="itens",
        verbose_name="Pedido",
    )

    produto = models.ForeignKey(
        to=Produto,
        on_delete=models.PROTECT,
        related_name="itens_pedido",
        verbose_name="Produto",
    )

    quantidade = models.PositiveIntegerField(
        default=1,
        verbose_name="Quantidade",
    )

    preco_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Preço unitário",
    )

    class Meta:
        verbose_name = "Item do pedido"
        verbose_name_plural = "Itens do pedido"
        ordering = ["pedido", "produto"]

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"

    def subtotal(self):
        """
        Retorna o valor total do item.
        """
        return self.quantidade * self.preco_unitario


class ComentarioAvaliacao(models.Model):
    """
    Avaliação e comentário de um cliente sobre um produto.
    """

    cliente = models.ForeignKey(
        to=Cliente,
        on_delete=models.CASCADE,
        related_name="avaliacoes",
        verbose_name="Cliente",
    )

    produto = models.ForeignKey(
        to=Produto,
        on_delete=models.CASCADE,
        related_name="avaliacoes",
        verbose_name="Produto",
    )

    texto = models.TextField(
        verbose_name="Comentário",
    )

    nota = models.PositiveSmallIntegerField(
        # Valores permitidos: 1, 2, 3, 4 e 5.
        choices=[(nota, str(nota)) for nota in range(1, 6)],
        verbose_name="Nota",
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em",
    )

    class Meta:
        verbose_name = "Comentário e avaliação"
        verbose_name_plural = "Comentários e avaliações"
        ordering = ["-criado_em"]

    def __str__(self):
        return f"{self.produto.nome} - nota {self.nota}"
