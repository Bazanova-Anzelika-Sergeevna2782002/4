if __name__ == "__main__":
    class Mammals:
        def __init__(self, feeding: str, heart_chambers: int):
            self._feeding = feeding
            self._heart_chambers = heart_chambers

        @property
        def feeding(self) -> str:
            return self._feeding

        @property
        def heart_chambers(self) -> int:
            return self._heart_chambers

        """
            Создание и подготовка к работе класса "Млекопитающие"

            :param feeding: Тип вскармливания. 
            Защищенный атрибут, так как тип вскармливания млекопитающих может быть 
            только один, поэтому пользователь не может задать иной тип вскармливания. 
            Свойство досупно только для чтения. 
            Наследуется для отрядов млекопитающих, так как является общим признаком.
            
            :param heart_chambers: Количество камер сердца. 
            Защищенный атрибут, так как количество камер сердца 
            млекопитающих может быть равным только 4, поэтому пользователь не может задать иное количество. 
            Свойство досупно только для чтения.
            Наследуется для отрядов млекопитающих, так как является общим признаком.
        """

        def __str__(self) -> str:
            return f'Вскармливание {self.feeding}. Камер сердца {self.heart_chambers}'

        """
            Функция выводит строку

            :return: Строка "Вскармливание ... Камер сердца ..."
            
            Наследуется, так как для всех отрядов класса млекопитающих тип вскармливания и число камер сердца - общие 
            характеристики.
        """

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}(feeding={self.feeding!r}, heart_chambers={self.heart_chambers!r})'

        """
             Функция возвращает валидную python строку
             
             :return: Строка "Название класса feeding=..., heart_chambers=..."
         """

        def is_it_mammal(self) -> bool:
            ...

        """
            Функция определяет является ли животное млекопитающим

            :return: Является ли животное млекопитающим
            
            Метод наследуется, так как для всех отрядов будет общим принадлежность к классу млекопитающих.
        """

        def number_of_animals(self, number_of_mammals: int) -> None:
            ...

        """
            Функция определяет количество животных, принадлежащих к классу млекопитающих

            :param number_of_mammals: количество млекопитающих
            
            :return: Количество млекопитающих
        """

    class Artiodactyls(Mammals):
        def __init__(self, feeding: str, heart_chambers: int, structure_legs: str):
            super().__init__(feeding=feeding, heart_chambers=heart_chambers)
            self.structure_legs = structure_legs

        """
            Подкласс Парнокопытные класса Млекопитающие
            
            :param structure_legs: Тип ног.
            Характеристика, присущая исклучительно подклассу Парнокопытные.
            
            :param feeding и heart_chambers наследуются из класса Млекопитающие и присущи всем представителям класса.
        """

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}(feeding={self.feeding!r}, heart_chambers={self.heart_chambers!r}, ' \
                   f'structure_legs={self.structure_legs!r})'

        """
             Функция возвращает валидную python строку
             
             :return: Строка "Название класса feeding=..., heart_chambers=..., structure_legs=..."
             
             Метод перезагружается, так как меняется название класса и добавляется 1 характеристика, не упомянутая в 
             базовом классе.
        """

        def number_of_animals(self, number_of_artiodactyls: int) -> None:
            super().number_of_animals(number_of_mammals=number_of_artiodactyls)
            ...

        """
            Функция определяет количество животных, принадлежащих к классу парнокопытных

            :param number_of_artiodactyls: Количество парнокопытных
            
            :return: Количество парнокопытных

            Метод перезагружается, так как количество млекопитающих не равно количеству парнокопытных.
        """

    class Predatory(Mammals):
        def __init__(self, feeding: str, heart_chambers: int, nutrition: str):
            super().__init__(feeding=feeding, heart_chambers=heart_chambers)
            self.nutrition = nutrition

        """
            Подкласс Хищники класса Млекопитающие

            :param nutrition: Питание.
            Характеристика, присущая исклучительно подклассу Хищники.

            :param feeding и heart_chambers наследуются из класса Млекопитающие и присущи всем представителям класса.
        """

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}(feeding={self.feeding!r}, heart_chambers={self.heart_chambers!r}, ' \
                   f'nutrition={self.nutrition!r})'

        """
            Функция возвращает валидную python строку

            :return: Строка "Название класса feeding=..., heart_chambers=..., heart_chambers=..."

            Метод перезагружается, так как меняется название класса и добавляется 1 характеристика, не упомянутая в 
            базовом классе.
        """

        def number_of_animals(self, number_of_predatory: int) -> None:
            super().number_of_animals(number_of_mammals=number_of_predatory)
            ...

        """
            Функция определяет количество животных, принадлежащих к классу хищников

            :param number_of_predatory: Количество хищников

            :return: Количество хищников

            Метод перезагружается, так как количество млекопитающих не равно количеству хищников.
        """

pass
