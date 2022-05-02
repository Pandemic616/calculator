class Calculator:
    """Класс производит вычесление из двух аргументов"""

    def __init__(self, arg1: int, arg2: int):
        self.arg1 = arg1
        self.arg2 = arg2

    def plus(self) -> int:
        """Суммирует два аргумента"""
        return self.arg1 + self.arg2

    def minus(self) -> int:
        """Вычитает второй аргумент из первого аргумента"""
        return self.arg1 - self.arg2

    def multiplication(self) -> int:
        """Умножает первый аргумент на второй аргумент"""
        return self.arg1 * self.arg2

    def divide(self) -> int:
        """Делит первый аргумент на второй"""
        return self.arg1 // self.arg2

    def degree(self) -> int:
        """Возводит в степень первый аргумент на второй аргумент"""
        return self.arg1 ** self.arg2


def operand(expression: str) -> str:
    """Определяет какой операнд вырожения ввел пользователь и выводит его из строки"""
    if '+' in expression:
        return '+'
    elif '-' in expression:
        return '-'
    elif '*' in expression:
        return '*'
    elif '/' in expression:
        return '/'
    elif '^' in expression:
        return '^'


def operator(operand: str, calculator: Calculator) -> int | str:
    """Определяет какой метод класса нужно использовать по операнду"""
    if operand in '+':
        return calculator.plus()
    elif operand in '-':
        return calculator.minus()
    elif operand in '*':
        return calculator.multiplication()
    elif operand in '/':
        return calculator.divide()
    elif operand in '^':
        return calculator.degree()
    else:
        return 'Такого оператора нет'


def main():
    expression = input()
    string = expression.partition(operand(expression))
    calculator = Calculator(arg1=int(string[0]), arg2=int(string[2]))
    print(operator(operand=string[1], calculator=calculator))


if __name__ == '__main__':
    main()
