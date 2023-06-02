import random
import requests
from basicword import BasicWord


def load_random_word(filename):
    """Получает данные из файла со списком слов,
    выбирает случайное слово,
    создает из него экземпляр класса BasicWord
    возвращает его"""
    response = requests.get(filename)
    data_words = response.json()
    word = random.choice(data_words)
    basic_word = BasicWord(word['word'], word['subwords'])
    return basic_word
