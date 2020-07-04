import random

want_more = 'хочу'

while want_more == 'хочу':
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
            want_more = input('Хотите сыграть ещё? "хочу" или "не хочу": ')

print()
print('До свиданья(не в том смысле!), приходите ещё!')
print()