class BasicWord:

    def __init__(self, word, subwords):
        """
        :param word: Исходное слово, из которого составляются новые слова.
        :param subwords: Список допустимых слов, которые можно составить из исходного
        """
        self.word = word.upper()
        self.subwords = subwords

    def __repr__(self):
        return f"{self.word}({self.subwords})"

    def is_subword(self, user_input):
        """
        Проверяет, является ли введеное слово допустимым
        :param user_input: слово, введеное игроком
        :return: True - если слово допустимо, False - если недоустимо
        """
        return user_input in self.subwords

    def count_subwords(self):
        """
        Считает и возвращает количество допустимых слов
        """
        return len(self.subwords)
