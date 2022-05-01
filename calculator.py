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
        """Врзводит в степень первый аргумент на второй аргумент"""
        return self.arg1 ** self.arg2
