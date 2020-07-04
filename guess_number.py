
import random

answer = random.randint(1, 10)
guess = -1
while answer != guess:
    guess = input('Введите число: ')
    try:
        guess = int(guess)
    except ValueError:
        print('Где у вас башка? Я вам сказала введите ЧИСЛО! Вы слышите, ЧИСЛО!!!!!!!')
        continue

    if answer < guess:
        print('Загаданое число меньше')
    elif answer > guess:
        print('Загаданое число больше')
    else:
        print('Бинго!!!!')