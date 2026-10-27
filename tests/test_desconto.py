import pytest

from src.desconto import (
    DescontoNormal,
    DescontoPremium,
    DescontoVIP,
    Pedido,
    aplicar_cupom,
    aplicar_desconto,
)


def test_desconto_normal() -> None:
    desconto = DescontoNormal()
    resultado = desconto.calcular(100)
    assert resultado == 10, f"Esperado 10, mas obteve {resultado}"


@pytest.fixture
def desconto_vip() -> DescontoVIP:
    return DescontoVIP()


def test_desconto_vip_100(desconto_vip: DescontoVIP) -> None:
    assert desconto_vip.calcular(100) == 20


def test_desconto_vip_200(desconto_vip: DescontoVIP) -> None:
    assert desconto_vip.calcular(200) == 40


@pytest.mark.parametrize(
    "valor, esperado",
    [
        (100, 30),
        (200, 60),
        (300, 90),
    ],
)
def test_desconto_premium(valor: float, esperado: float) -> None:
    desconto = DescontoPremium()
    resultado = desconto.calcular(valor)

    assert resultado == esperado


def test_pedido_total_desconto_normal() -> None:
    pedido = Pedido(DescontoNormal())
    assert pedido.total(100) == 90


def test_pedido_total_desconto_vip(desconto_vip: DescontoVIP) -> None:
    pedido = Pedido(desconto_vip)
    assert pedido.total(100) == 80


def test_pedido_total_desconto_premium() -> None:
    pedido = Pedido(DescontoPremium())
    assert pedido.total(100) == 70


def test_aplicar_desconto_polimorfico() -> None:
    assert aplicar_desconto(DescontoNormal(), 100) == 10
    assert aplicar_desconto(DescontoVIP(), 100) == 20
    assert aplicar_desconto(DescontoPremium(), 100) == 30


def test_cupom_e_validacao_vip(desconto_vip: DescontoVIP) -> None:
    assert aplicar_cupom(desconto_vip, "DESC10") is True
    assert desconto_vip.validar_usuario_vip("vip") is True
    assert desconto_vip.validar_usuario_vip("normal") is False

