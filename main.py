from player import Player
from utils import load_random_word


if __name__ == '__main__':
    user_name = input("Введите имя игрока:\n")
    # Создаем экземпляр класса Player с именем игрока
    player = Player(user_name)

    # Присваиваем переменной basic_word результат функции load_random_word(экземпляр класса BasicWord)
    basic_word = load_random_word('https://www.jsonkeeper.com/b/BWTJ')

    # Программа здоровается, объясняет правила игры
    print(f"Привет {user_name}!\n"
          f"Составьте {basic_word.count_subwords()} слов из слова {basic_word.word}\n"
          "Слова должны быть не короче 3 букв\n"
          "Чтобы закончить игру, угадайте все слова или напишите слово 'stop'\n"
          "Поехали, ваше первое слово?"
          )

    # Запускаем цикл из ответов игрока, пока количество отгаданных слов не сравняется с количеством допустимых
    while player.count_subwords() != basic_word.count_subwords():
        user_answer = input().lower().rstrip()
        if len(user_answer) < 3:
            print("Слово должно быть не короче 3 букв!")
        elif user_answer in ['stop', 'стоп']:
            print(f"Игра завершена, вы угадали {len(player.user_subwords)} слов")
            quit()
        elif not basic_word.is_subword(user_answer):
            print("Неверно")
        elif player.is_used(user_answer):
            print("Слово уже угадано")
        # Если слово прошло все проверки, добавляем его в список слов игрока, выводим промежуточный результат
        else:
            player.append_subword(user_answer)
            print(f"Верно, угадано {player.count_subwords()} слов из {basic_word.count_subwords()}")
    print(f"Игра завершена, вы угадали {len(player.user_subwords)} слов! Поздравляем!")
