class Player:

    def __init__(self, name, user_subwords=None):
        """
        :param name: имя игрока
        :param user_subwords: слова, названные игроком
        """
        self.name = name
        if user_subwords:
            self.user_subwords = user_subwords
        else:
            self.user_subwords = []

    def __repr__(self):
        return f"{self.name}({self.user_subwords})"

    def append_subword(self, user_input):
        """
        Добавляет введеное слово в список угаданных
        :param user_input: введенное слово
        """
        self.user_subwords.append(user_input)

    def count_subwords(self):
        """
        Считает и возвращает количество угаданных слов
        """
        return len(self.user_subwords)

    def is_used(self, user_input):
        """
        Проверяет было ли слово уже угадано
        :param user_input: слово, введенное пользователем
        :return: True - если слово уже угадано, False - слово еще не угадано
        """
        return user_input in self.user_subwords
