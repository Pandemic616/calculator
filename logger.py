import os.path
from datetime import datetime


class Logger:
    number: int = 1
    file: str = f'log_file_{number}.txt'

    @classmethod
    def write(cls, message: str) -> None:
        cls.creature()
        cls.record(message)

    @classmethod
    def creature(cls) -> None:
        """Если нет файла, метод его создаст"""
        if not os.path.exists(cls.file):
            open(cls.file, 'w')

    @classmethod
    def record(cls, message: str) -> None:
        cls.size()
        with open(cls.file, 'a', encoding='UTF-8') as file:
            file.write(f'{datetime.now()}: {__name__}: {message}\n')

    @classmethod
    def size(cls) -> None:
        if os.path.getsize(cls.file) > 5000:
            cls.number += 1
            cls.file = f'log_file_{cls.number}.txt'

