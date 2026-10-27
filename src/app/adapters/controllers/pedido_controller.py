from src.app.entities.pedido import Pedido
from src.app.use_cases.criar_pedido import CriarPedido


class PedidoController:
    def __init__(self, criar_pedido_use_case: CriarPedido) -> None:
        self.criar_pedido_use_case = criar_pedido_use_case

    def criar_pedido(
        self, cliente: str, valor_original: float, tipo_desconto: str
    ) -> Pedido:
        return self.criar_pedido_use_case.executar(
            cliente, valor_original, tipo_desconto
        )

    def listar_pedidos(self) -> list[Pedido]:
        return self.criar_pedido_use_case.listar_pedidos()
