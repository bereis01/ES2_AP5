from src.calculator import CumulativeCalculator


def test_initialization():
    calculator = CumulativeCalculator()

    assert calculator.result() == None
    assert calculator.history() == []


def test_clear_empty_calculator():
    calculator = CumulativeCalculator()

    calculator.clear()

    assert calculator.result() == None
    assert calculator.history() == []


def test_clear_full_calculator():
    calculator = CumulativeCalculator()
    calculator.sum(8)
    calculator.sum(-2)

    calculator.clear()

    assert calculator.result() == 8
    assert calculator.history() == []


def test_reset_empty_calculator():
    calculator = CumulativeCalculator()

    calculator.reset()

    assert calculator.result() == None
    assert calculator.history() == []


def test_reset_full_calculator():
    calculator = CumulativeCalculator()
    calculator.sum(8)
    calculator.sum(-2)

    calculator.reset()

    assert calculator.result() == None
    assert calculator.history() == []


def test_sum_to_empty_calculator():
    calculator = CumulativeCalculator()

    calculator.sum(8)

    assert calculator.result() == 8


def test_sum_multiple_numbers():
    calculator = CumulativeCalculator()

    calculator.sum(8)
    calculator.sum(17)
    calculator.sum(-2)

    assert calculator.result() == 23


def test_sub_to_empty_calculator():
    calculator = CumulativeCalculator()

    calculator.sub(8)

    assert calculator.result() == -8


def test_sub_multiple_numbers():
    calculator = CumulativeCalculator()

    calculator.sub(4)
    calculator.sub(-7)
    calculator.sub(-2)

    assert calculator.result() == 5


def test_mul_to_empty_calculator():
    calculator = CumulativeCalculator()

    calculator.mul(8)

    assert calculator.result() == 8


def test_mul_multiple_numbers():
    calculator = CumulativeCalculator()

    calculator.mul(4)
    calculator.mul(-5)
    calculator.mul(1 / 8)

    assert calculator.result() == -2.5


def test_div_to_empty_calculator():
    calculator = CumulativeCalculator()

    calculator.div(12)

    assert calculator.result() == 1 / 12


def test_div_multiple_numbers():
    calculator = CumulativeCalculator()

    calculator.div(1 / 8)
    calculator.div(4)
    calculator.div(-2)

    assert calculator.result() == -1


def test_multiple_operations():
    calculator = CumulativeCalculator()

    calculator.div(1 / 8)
    calculator.sum(17)
    calculator.mul(-2)
    calculator.sub(-50)

    assert calculator.result() == 0


def test_history_being_tracked():
    calculator = CumulativeCalculator()

    calculator.div(-2)
    calculator.sum(4)
    calculator.mul(-8)
    calculator.sub(16)

    assert calculator.history() == [-1 / 2, 7 / 2, -28]
