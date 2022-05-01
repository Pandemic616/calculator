import pytest

from calculator import Calculator


@pytest.mark.parametrize(
    'num1, num2, result',
    [
        (1, 2, 3),
        (4, 5, 9),
        (-5, 10, 5),
        (256, 512, 768)
    ]
)
def test_calculator_plus(num1, num2, result):
    calculator = Calculator(num1, num2)
    assert calculator.plus() == result


@pytest.mark.parametrize(
    'num1, num2, result',
    [
        (1, 2, -1),
        (10, 4, 6),
        (-5, 10, -15),
        (256, 256, 0),
        (0, 0, 0)
    ]
)
def test_calculator_minus(num1, num2, result):
    calculator = Calculator(num1, num2)
    assert calculator.minus() == result


@pytest.mark.parametrize(
    'num1, num2, result',
    [
        (1, 2, 2),
        (11, 4, 44),
        (5, 10, 50),
        (256, 2, 512),
        (0, 0, 0)
    ]
)
def test_calculator_multiplication(num1, num2, result):
    calculator = Calculator(num1, num2)
    assert calculator.multiplication() == result


@pytest.mark.parametrize(
    'num1, num2, result',
    [
        (8, 2, 4),
        (20, 4, 5),
        (5, 5, 1),
        (256, 2, 128)
    ]
)
def test_calculator_divide(num1, num2, result):
    calculator = Calculator(num1, num2)
    assert calculator.divide() == result


@pytest.mark.parametrize(
    'num1, num2, result',
    [
        (8, 2, 64),
        (20, 4, 160000),
        (5, 8, 390625),
        (256, 2, 65536)
    ]
)
def test_calculator_degree(num1, num2, result):
    calculator = Calculator(num1, num2)
    assert calculator.degree() == result