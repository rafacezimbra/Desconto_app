from src.database.connection import DatabaseConnection
from src.models.pedido import Pedido


class PedidoRepository:
    """Classe de repositório para armazenar e gerenciar pedidos."""

    def __init__(self, database: DatabaseConnection) -> None:
        self.database = database

    def adicionar_pedido(self, pedido: Pedido) -> None:
        self.database.pedidos.append(pedido)

    def listar_pedidos(self) -> list[Pedido]:
        return self.database.pedidos
