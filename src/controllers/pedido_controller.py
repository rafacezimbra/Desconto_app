from src.models.pedido import Pedido
from src.services.pedido_service import PedidoService


class PedidoController:
    """Classe de controlador para gerenciar a lógica de negócios dos pedidos."""

    def __init__(self, service: PedidoService) -> None:
        self.service = service

    def adicionar_pedido(self, pedido: Pedido) -> None:
        self.service.adicionar_pedido(pedido)

    def processar_pedidos(self) -> None:
        self.service.processar_pedidos()
