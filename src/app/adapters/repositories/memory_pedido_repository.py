from src.app.entities.pedido import Pedido
from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.gateways.pedido_gateway import IPedidoGateway


class MemoryPedidoRepository(IPedidoGateway):
    def __init__(self, database: MemoryDatabase) -> None:
        self.database = database

    def salvar(self, pedido: Pedido) -> None:
        self.database.pedidos.append(pedido)

    def listar(self) -> list[Pedido]:
        return self.database.pedidos
