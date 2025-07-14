from abc import ABC, abstractmethod  # Импорт базового класса для абстрактных классов и декоратора для абстрактных методов
from typing import List  # Импорт для аннотации типов — список элементов

# Класс, представляющий один кусочек пиццы
class PizzaItem:
    def __init__(self, number: int):  # Конструктор принимает номер кусочка
        self.number = number

    def __repr__(self):  # Метод строкового представления объекта
        return f"Slice #{self.number}"  # Например: "Slice #3"

# Абстрактный итератор (интерфейс), определяет методы, которые должен реализовать любой итератор
class Iterator(ABC):
    @abstractmethod
    def next(self) -> PizzaItem:  # Метод получения следующего элемента
        ...

    @abstractmethod
    def has_next(self) -> bool:  # Метод проверки, есть ли ещё элементы
        ...

# Конкретная реализация итератора для срезов пиццы
class PizzaSliceIterator(Iterator):
    def __init__(self, pizza: List[PizzaItem]):  # Принимает список кусочков пиццы
        self._pizza = pizza  # Сохраняем список кусочков
        self._index = 0  # Индекс текущего элемента

    def next(self) -> PizzaItem:  # Возвращает следующий кусочек пиццы
        pizza_item = self._pizza[self._index]  # Берём кусочек по текущему индексу
        self._index += 1  # Увеличиваем индекс
        return pizza_item  # Возвращаем кусочек

    def has_next(self) -> bool:  # Проверяет, остались ли ещё элементы
        return False if self._index >= len(self._pizza) else True
        # Вернёт False, если индекс вышел за границы списка

# Агрегатор пиццы — хранит список кусочков и создаёт итератор
class PizzaAggregate:
    def __init__(self, amount_slices: int = 10):  # По умолчанию 10 кусочков
        self.slices = [PizzaItem(i + 1) for i in range(amount_slices)]
        # Генерация списка кусочков с номерами от 1 до amount_slices
        print(
            f"Приготовили пиццу и порезали "
            f"на {amount_slices} кусочков"
        )

    def amount_slices(self) -> int:  # Возвращает количество кусочков
        return len(self.slices)

    def iterator(self) -> Iterator:  # Создаёт итератор для кусочков пиццы
        return PizzaSliceIterator(self.slices)

# Точка входа — проверка, что модуль запущен напрямую
if __name__ == "__main__":
    pizza = PizzaAggregate(5)  # Создаём пиццу из 5 кусочков
    iterator = pizza.iterator()  # Получаем итератор

    while iterator.has_next():  # Пока есть кусочки
        item = iterator.next()  # Получаем следующий кусочек
        print("Это " + str(item))  # Печатаем его

