import doctest


class Phone:
    def __init__(self, number: str, owner_name: str) -> None:
        """
        Конструктор класса Телефон

        :param number: номер телефона
        :param owner_name: имя владельца

        Примеры:
        >>> phone = Phone('88005553535', 'Андрей')
        """

        if not isinstance(number, str):
            raise TypeError("Номер телефона должен быть строкой")
        if not isinstance(owner_name, str):
            raise TypeError("Имя владельца должно быть строкой")

        if len(owner_name) < 1 or len(owner_name) > 50:
            raise ValueError("Имя владельца не может быть пустой строкой и превышать 50 символов")
        if len(number) != 11:
            raise ValueError("Номер телефона должен быть из 11 символов (включая код страны)")

        self.number = number
        self.owner_name = owner_name

    def call_to_person(self, person_to_call: str) -> None:
        """
        Совершить вызов другому человеку

        :param person_to_call: имя человека, которому звоним
        :return: Совершние звонка

        Примеры:
        >>> iphone = Phone('88005553535', 'Андрей')
        >>> iphone.call_to_person('Артём')
        Андрей звонит Артём с номера 88005553535
        """

        print(f"{self.owner_name} звонит {person_to_call} с номера {self.number}")

    def update_phone_number(self, new_number: str) -> None:
        """
        Обновнить номера телефона

        :param new_number: новый номер телефона
        :return: новый номер телефона
        >>> iphone = Phone('88005553535', 'Андрей')
        >>> iphone.update_phone_number('88005553536')
        Андрей обновил номер на 88005553536
        """
        self.number = new_number
        print(f"{self.owner_name} обновил номер на {self.number}")


if __name__ == '__main__':
    doctest.testmod()
