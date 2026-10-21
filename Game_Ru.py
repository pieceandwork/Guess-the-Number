from random import randint
import time
import json
import os

STATS_FILE = "stats.json"


def show_stats(stats):
    print("\n" + "=" * 30)
    print("📊 ВАША СТАТИСТИКА:")
    print(f"🏆 Побед: {stats['wins']}")
    print(f"💀 Поражений: {stats['losses']}")
    print(f"🎮 Всего игр: {stats['total_games']}")

    if stats['total_games'] > 0:
        winrate = (stats['wins'] / stats['total_games']) * 100
        print(f"📈 Процент побед: {winrate:.1f}%")
    print("=" * 30 + "\n")


def load_stats():
    if not os.path.exists(STATS_FILE):
        return {"wins": 0, "losses": 0, "total_games": 0}

    try:
        with open(STATS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError):
        return {"wins": 0, "losses": 0, "total_games": 0}


def save_stats(stats):
    with open(STATS_FILE, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=4)


def game_greetings():
    print('\n👋 ДОБРО ПОЖАЛОВАТЬ В ЛОГОВО ДЕМОНА!!! 👿\n')
    stats = load_stats()
    show_stats(stats)
    print(
        '\n📖 Предыстория... (Возможно миф..)\nЖил как-то в своей пещере Демон. Он любил всегда математику, (да, и возможно, он видел вживую самого Пифагора) поэтому он, используя свой зловещий разум, придумал игру-проклятие!\nНужно отгадать число у Демона от 1 до 100 и если ты не отгадаешь, то эта игра будет у тебя вызывать зависимость все больше и больше, пока не победить Демона...\n\n')
    print('🥊 Сможешь ли ты одолеть Демона (😈) ?\n')
    while True:
        player_input = input('(Да/Нет) - ')
        if player_input.lower() == 'да':
            print('\n\n🍀 Удачи!!!\n')
            game_option()
        elif player_input.lower() == 'нет':
            exit('\nНаберись сил и возвращайся! 👋\n')
        else:
            print('\n❌ Введено некорректное значение!\n')


def game_option():
    attempt = [5, 10, 15]
    complexity = ''

    print(
        f'\n\nВыбери сложность:\n\n🔴 Лёгкая (1) - {attempt[2]} попыток.\n🔴 Средняя (2) - {attempt[1]} попыток.\n🔴 Сложная (3) - {attempt[0]} попыток.\n')

    while True:
        choice = int(input('Введите число (от 1️⃣ до 3️⃣): '))
        if choice <= 0 or choice > 3:
            print('❌ Неверное значение!')
        else:
            match choice:
                case 1:
                    choice = 15
                    complexity = 'Лёгкая'
                case 2:
                    choice = 10
                    complexity = 'Средняя'
                case 3:
                    choice = 5
                    complexity = 'Сложная'

            print('\n🚧 Загрузка...\n')
            time.sleep(2)
            print('✅ Готово!\n')
            print(f'\nВыбранная сложность:🔴 {complexity} ({choice} попыток)\n')
            break

    game_play(choice)


def game_play(attempts):
    stats = load_stats()
    print('=' * 24)
    print('| Н а ч а л о  и г р ы |\n')

    random_number = randint(1, 100)

    print('Я загадал число... Попробуй отгадать! 👿\n')

    while attempts > 0:
        try:
            player_input = int(input())
        except ValueError:
            print('❌ Введи число!')
            continue

        if player_input > 100 or player_input < 0:
            print('\n❌ Ты вышел за пределы, не жульничай... Я же говорил что от 1️⃣ до 1️⃣0️⃣0️⃣! 👿\n')
        elif player_input == random_number:
            stats['total_games'] += 1
            stats['wins'] += 1
            save_stats(stats)
            print('\n🎉 Поздравляю, ты одолел меня... Но не надолго. В следующий раз я буду сильнее! 👺\n')
            print('| К о н е ц  и г р ы |')
            print('-' * 24)
            game_conclusion()
        elif player_input > random_number:
            print('Меньше! 👹')
            attempts -= 1
        else:
            print('Больше! 👹')
            attempts -= 1

    stats['total_games'] += 1
    stats['losses'] += 1
    save_stats(stats)
    print('\nЯ выиграл, ДА! Я всегда знал что я сильнейший 😈👊\n')
    print('| К о н е ц  и г р ы |')
    print('=' * 22)
    game_conclusion()


def game_conclusion():
    stats = load_stats()
    while True:
        print('\n\nХотите продолжить игру❓\n')
        player_input = input('(Да/Нет) - ')

        if player_input.lower() == 'да':
            show_stats(stats)
            game_option()
            break
        elif player_input.lower() == 'нет':
            exit('\nЗаглядывай ещё!!! 👿\n')
        else:
            print('\n❌ Введено некорректное значение!\n')


game_greetings()
