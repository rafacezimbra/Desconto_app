import abc


class IDesconto(abc.ABC):
    @abc.abstractmethod
    def calcular(self, valor: float) -> float:
        raise NotImplementedError  # pragma: no cover


class ICupom(abc.ABC):
    @abc.abstractmethod
    def aplicar_cupom(self, codigo: str) -> bool:
        raise NotImplementedError  # pragma: no cover


class IVIP(abc.ABC):
    @abc.abstractmethod
    def validar_usuario_vip(self, usuario: str) -> bool:
        raise NotImplementedError  # pragma: no cover


class DescontoNormal(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.1


class DescontoVIP(IDesconto, ICupom, IVIP):
    def calcular(self, valor: float) -> float:
        return valor * 0.2

    def aplicar_cupom(self, codigo: str) -> bool:
        return True

    def validar_usuario_vip(self, usuario: str) -> bool:
        return usuario == "vip"


class DescontoPremium(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.3


class Pedido:
    def __init__(self, desconto: IDesconto) -> None:
        self.desconto = desconto

    def total(self, valor: float) -> float:
        return valor - self.desconto.calcular(valor)


def aplicar_desconto(desconto: IDesconto, valor: float) -> float:
    return desconto.calcular(valor)


def aplicar_cupom(cupom: ICupom, codigo: str) -> bool:
    return cupom.aplicar_cupom(codigo)


if __name__ == "__main__":  # pragma: no cover
    valor = 100

    pedido_normal = Pedido(DescontoNormal())
    print("Normal:", pedido_normal.total(valor))

    pedido_vip = Pedido(DescontoVIP())
    print("VIP:", pedido_vip.total(valor))

    pedido_premium = Pedido(DescontoPremium())
    print("Premium:", pedido_premium.total(valor))
