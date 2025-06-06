import doctest


class Car:
    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        engine_volume: float,
        fuel_type: str = "бензин",
        mileage: float = 0.0,
        color: str = "white",
    ):
        """
        Создание объекта "Автомобиль".

        :param brand: Марка автомобиля (например, "Toyota")
        :param model: Модель автомобиля (например, "Camry")
        :param year: Год выпуска (например, 2020)
        :param engine_volume: Объем двигателя (в литрах, например, 2.5)
        :param fuel_type: Тип топлива ("бензин", "дизель", "электричество")
        :param mileage: Пробег (в км, по умолчанию 0.0)
        :param color: Цвет (по умолчанию "white")

        Пример:
        >>> my_car = Car("Toyota", "Camry", 2020, 2.5, "бензин", 15000, "black")
        >>> my_car = Car("Toyota", "Camry", cool_car, 2.5, "бензин", 15000, "black")
        Traceback (most recent call last):
        ...
        NameError: name 'cool_car' is not defined
        """
        if not isinstance(brand, str):
          raise TypeError("Бренд должен быть записан строкой")
        self.brand = brand

        if not isinstance(model, str):
          raise TypeError("Модель должна быть записан строкой")
        self.model = model

        if not isinstance(year, (float, int)):
          raise TypeError("Год должен быть передан цифрой")
        if year < 0:
          raise ValueError("Год не может быть отрицательным")
        self.year = year

        if not isinstance(engine_volume, (float, int)):
          raise TypeError("Объем двигателя должен быть передан цифрой")
        if engine_volume < 0:
          raise ValueError("Объем двигателя не может быть отрицательным")
        self.engine_volume = engine_volume

        if not isinstance(fuel_type, str):
          raise TypeError("Тип топлива должен быть записан строкой")
        self.fuel_type = fuel_type

        if not isinstance(mileage, (float, int)):
          raise TypeError("Пробег должен быть передан цифрой")
        if mileage < 0:
          raise ValueError("Пробег не может быть отрицательным")
        self.mileage = mileage

        if not isinstance(color, str):
          raise TypeError("Цвет должен быть записан строкой")
        self.color = color

    def drive(self, distance: float) -> None:  # self - ссылка на экземпляр класса
        """Увеличивает пробег автомобиля.
        
        Пример:
        >>> my_car = Car("Toyota", "Camry", 2020, 2.5, "бензин", 15000, "black")
        >>> my_car.drive(100)
        >>> print(my_car.mileage)
        15100
        """
        if not isinstance(distance, (float, int)):
          raise TypeError("Расстояние должно быть передано цифрой")
        if distance < 0:
          raise ValueError("Расстояние не может быть отрицательным")
        self.mileage += distance

    def repaint(self, new_color: str) -> None:
        """Перекрашивает автомобиль.
        
        Пример:
        >>> my_car = Car("Toyota", "Camry", 2020, 2.5, "бензин", 15000, "black")
        >>> my_car.repaint("white")
        >>> print(my_car.color)
        white
        """
        if not isinstance(new_color, str):
          raise TypeError("Цвет должен быть записан строкой")
        self.color = new_color

    def __str__(self) -> str:
      """Возвращает информацию об автомобиле для чтения людьми.

      Пример:
        >>> my_car = Car("Toyota", "Camry", 2020, 2.5, "бензин", 15000, "black")
        >>> print(my_car)
        Toyota Camry (2020), black, пробег: 15000 км. Информация для чтения людьми.
        >>> my_car.__str__()
        'Toyota Camry (2020), black, пробег: 15000 км. Информация для чтения людьми.'
      """
      return f"{self.brand} {self.model} ({self.year}), {self.color}, пробег: {self.mileage} км. Информация для чтения людьми."

doctest.testmod()
