from logger import Logger

class Calculator:
    """Класс производит вычесление из двух аргументов"""

    def __init__(self, arg1: float, arg2: float):
        self.arg1 = arg1
        self.arg2 = arg2

    def plus(self) -> float:
        """Суммирует два аргумента"""
        return self.arg1 + self.arg2

    def minus(self) -> float:
        """Вычитает второй аргумент из первого аргумента"""
        return self.arg1 - self.arg2

    def multiplication(self) -> float:
        """Умножает первый аргумент на второй аргумент"""
        return self.arg1 * self.arg2

    def divide(self) -> float:
        """Делит первый аргумент на второй"""
        return self.arg1 / self.arg2

    def degree(self) -> float:
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


def operator(operand: str, calculator: Calculator) -> float | str:
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


def main_calculator(expression):
    string = expression.partition(operand(expression))
    calculator = Calculator(arg1=float(string[0]), arg2=float(string[2]))
    result = operator(operand=string[1], calculator=calculator)
    Logger.write(f'Выходящие данные: {result}')
    print(result)


def main():
    start = input('run or exit: ')
    stop = 'exit'
    while start.strip() != stop:
        print('Program in run')
        expression = input()
        Logger.write(f'Входящие данные: {expression}')
        try:
            if expression.strip() == stop:
                print('Program is stop')
                break
            else:
                main_calculator(expression)
        except TypeError:
            print('Invalid request')
    else:
        print('Program is not run')


if __name__ == '__main__':
    main()
