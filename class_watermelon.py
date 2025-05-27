import doctest


class Watermelon:
    def __init__(
        self,
        weight: float,            # вес в кг
        color: str = "зеленый",   # основной цвет корки
        variety: str = "обычный", # сорт
        is_ripe: bool = True,     # спелый ли?
        has_seeds: bool = True    # есть ли косточки
    ):
        """
        Создание объекта "Арбуз".

        :param weight: Вес арбуза в килограммах (должен быть > 0).
        :param color: Цвет корки (по умолчанию "зеленый").
        :param variety: Сорт арбуза (по умолчанию "обычный").
        :param is_ripe: Спелость (True/False).
        :param has_seeds: Наличие косточек (True/False).

        Примеры:
        >>> melon = Watermelon(7.5, "зеленый с полосками", "Астраханский", True, True)
        >>> melon = Watermelon(7.5, 5, "Астраханский", True, True)
        Traceback (most recent call last):
        ...
        TypeError: Цвет должен быть записан строкой
        """
        if not isinstance(weight, (int, float)):
          raise TypeError("Вес арбуза должен быть числом")
        if weight <= 0:
            raise ValueError("Вес арбуза должен быть положительным числом!")
        self.weight = weight
        if not isinstance(color, str):
          raise TypeError("Цвет должен быть записан строкой")
        self.color = color
        if not isinstance(variety, str):
          raise TypeError("Сорт должен быть записан строкой")
        self.variety = variety
        if not isinstance(is_ripe, bool):
          raise TypeError("Спелость арбуза должна быть передана в булевом типе данных")
        self.is_ripe = is_ripe
        if not isinstance(has_seeds, bool):
          raise TypeError("Наличие косточек должно быть передано в булевом типе данных")
        self.has_seeds = has_seeds

    def __str__(self) -> str:
        """
        Возвращает информацию об арбузе в виде строки.

        Примеры:
        >>> melon = Watermelon(7.5, "зеленый с полосками", "Астраханский", True, True)
        >>> print(melon)
        Арбуз сорта 'Астраханский': 7.5 кг, цвет: зеленый с полосками, спелый, с косточками.
        >>> melon.__str__()
        "Арбуз сорта 'Астраханский': 7.5 кг, цвет: зеленый с полосками, спелый, с косточками."
        """
        ripeness = "спелый" if self.is_ripe else "неспелый"
        seeds = "с косточками" if self.has_seeds else "без косточек"
        return f"Арбуз сорта '{self.variety}': {self.weight} кг, "\
               f"цвет: {self.color}, {ripeness}, {seeds}."

    def cut(self, piece_weight: float) -> float:
        """
        Разрезает арбуз на части и возвращает вес оставшегося куска.

        :param piece_weight: Желаемый вес куска в кг.
        :return: Реальный вес отрезанного куска.
        :raises ValueError: Если кусок больше самого арбуза или вес <= 0.

        Пример:
        >>> melon = Watermelon(7.5, "зеленый с полосками", "Астраханский", True, True)
        >>> melon.cut(2)
        5.5
        """
        if not isinstance(piece_weight, (int, float)):
          raise TypeError("Вес должен быть указан числом")
        if piece_weight <= 0:
            raise ValueError("Вес куска должен быть положительным!")
        if piece_weight > self.weight:
            raise ValueError("Нельзя отрезать больше, чем весит арбуз!")
        self.weight -= piece_weight
        return self.weight

    def check_ripeness(self) -> str:
        """
        Проверяет спелость арбуза.

        Пример:
        >>> melon = Watermelon(7.5, "зеленый с полосками", "Астраханский", True, True)
        >>> melon.check_ripeness()
        'Готов к употреблению!'
        """
        return "Готов к употреблению!" if self.is_ripe else "Пусть дозревает..."

    def remove_seeds(self) -> None:
        """
        Удаляет все косточки (если они есть).

        Пример:
        >>> melon = Watermelon(7.5, "зеленый с полосками", "Астраханский", True, True)
        >>> melon.remove_seeds()
        Косточки удалены!
        """
        if not self.has_seeds:
            print("В этом арбузе нет косточек!")
        else:
            self.has_seeds = False
            print("Косточки удалены!")


doctest.testmod()
