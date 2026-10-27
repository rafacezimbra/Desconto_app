from src.models.pedido import Pedido
from src.repositories.pedido_repository import PedidoRepository


class PedidoService:
    """Classe de serviço para processar pedidos e aplicar descontos."""

    def __init__(self, repository: PedidoRepository) -> None:
        self.repository = repository

    def adicionar_pedido(self, pedido: Pedido) -> None:
        self.repository.adicionar_pedido(pedido)

    def processar_pedidos(self) -> None:
        pedidos = self.repository.listar_pedidos()
        for pedido in pedidos:
            print(f"Cliente: {pedido.cliente}")
            print(f"Valor final: {pedido.valor_final(pedido.valor_original)}")
