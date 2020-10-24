import random
import time


def display_intro():
    print(''' Вы находитесь в землях, заселенных драконами.
                Перед собой вы видите две пещеры. В одной из них — дружелюбный дракон, 
                который готов поделиться с вами своими сокровищами. 
                Во второй — жадный и голодный дракон, который мигом вас съест.''')
    print()


def choose_cave():
    print("Выберите номер пещеры 1 или 2:")
    cave = input()
    while cave != "1" and cave != "2":
        print("Выберите номер пещеры 1 или 2")
        cave = input()
    return cave


def check_cave(chosen_cave):
    print("Вы приближатесь к пещере...")
    time.sleep(2)
    print("---------")
    time.sleep(2)
    print("Большой драконю....")
    print()
    time.sleep(2)

    friendly_cave = random.randint(1, 2)
    if chosen_cave == str(friendly_cave):
        print("Делится с вами своими сокровищами")
    else:
        print("Моментально вас съедает")


play_again = "да"
while play_again == "да" or play_again == "д":
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)

    play_again = input("Попытаете удачу еще раз? (да или нет):")