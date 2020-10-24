import random
HANGMAN_PICS=['''
 +---+
     |
     |
     |
    ===''','''
 +---+
 O   |
     |
     |
    ===''','''
 +---+
 O   |
 |   |
     |
    ===''','''
 +---+
 O   |
/|   |
     |
    ===''','''
 +---+
 O   |
/|\  |
     |
    ===''','''
+---+
 O   |
/|\  |
/    |
    ===''','''

+---+
 O   |
/|\  |
/ \  |
    ===''','''

+---+
[O   |
/|\  |
/ \  |
    ===''','''

+---+
[O]  |
/|\  |
/ \  |
    ===''']

words = {
    "цвета":'красный оранжевый желтый зеленый синий голубой фиолетовый белый черный коричневый'.split(),
    "фигуры":'квадрат треугольник прямоугольник круг эллипс ромб трапеция параллелограмм пятиугольник шестиугольник восьмиугольник'.split(),
    "фрукты":'яблоко апельсин лимон лайм груша мандарин виноград грейпфрут персик банан абрикос манго банан нектарин'.split(),
    "животные":'аист бабуин баран барсук бык волк зебра кит коза корова кошка кролик крыса лев лиса лось медведь мул мышь норка носорог обезьяна овца олень осел панда пума скунс собака сова тигр тюлень хорек ящерица'.split(),
}
print(words)


def get_random_word(word_dict):
    #эта функция возвращает случайную строку из переданного списка
    word_key = random.choice(list(word_dict.keys()))
    word_index=random.randint(0,len(word_dict[word_key]-1))
    pass

def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    print("Ошибочные буквы:", end =" ")
    for letter in missed_letters:
        print(letter, end=" ")
    print()

    # _ _ _
    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end = " ")
    print()

def get_guess(already_guessed):#"ddsfdjgaj"
    while True:
        print('Введите букву')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Пожалуйста введите одну букву")
        elif guess in already_guessed:
            print("Вы уже называли эту букву, назоваите другую")
        elif not guess.isalpha():
            print("Введите букву")
        else:
            return guess

def play_again():
    print("Хотите сыграть ещё раз?")
    answer = input().lower()# D->d d->d
    if answer.startswith("д"):#д*******
        return True
    else:
        return False

print("в и с е л и ц а")
missed_letters = ""
correct_letters = ""
secret_word = get_random_word(words)
game_is_done = False

while True:
    display_board(missed_letters, correct_letters, secret_word)
    guess = get_guess(missed_letters + correct_letters) #вызов функции с аргумекнтом -> получаем от пользователя букву

    if guess in secret_word:
        correct_letters = correct_letters + guess
        #проверяем выиграл ли игрок
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters == True:
            print("Да! Секретное слово " + secret_word)
            game_is_done = True
    else:
        print("Вы ошиблись")
        missed_letters = missed_letters + guess

        if len(missed_letters) >= len(HANGMAN_PICS) - 1:
            #display_board(missed_letters, correct_letters, secret_word)
            print("Вы исчерпали все попытки")
            print("Не угадано" + str(len(missed_letters)))
            print("Угадано" + str(len(correct_letters)))
            print("Было загадано" + secret_word)
            game_is_done=True
    if game_is_done:
        if play_again():
            missed_letters = ""
            correct_letters = ""
            game_is_done = False
            secret_word = get_random_word(words)
        else:
            break
