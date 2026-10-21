from random import randint
import time
import json
import os

STATS_FILE = "stats.json"


def show_stats(stats):
    print("\n" + "=" * 30)
    print("📊 YOUR STATISTICS:")
    print(f"🏆 Wins: {stats['wins']}")
    print(f"💀 Defeats: {stats['losses']}")
    print(f"🎮 Total games: {stats['total_games']}")

    if stats['total_games'] > 0:
        winrate = (stats['wins'] / stats['total_games']) * 100
        print(f"📈 Win percentage: {winrate:.1f}%")
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
    print("\n👋 WELCOME TO THE DEMON'S LAIR!!! 👿\n")
    stats = load_stats()
    show_stats(stats)
    print(
        '\n📖 Backstory... (Perhaps a myth...) Once, there lived a Demon in his cave. He had always loved mathematics (he may have even met Pythagoras himself!), so, using his sinister intellect, he devised a cursed game!\nYou must guess the number the Demon has chosen—anywhere from 1 to 100. If you fail to guess it, the game will become increasingly addictive, pulling you in deeper and deeper—until, that is, you manage to defeat the Demon...\n\n')
    print('🥊 Will you be able to defeat the Demon (😈)?\n')
    while True:
        player_input = input('(Yes/No) - ')
        if player_input.lower() == 'yes':
            print('\n\n🍀 Good luck!!!\n')
            game_option()
        elif player_input.lower() == 'no':
            exit('\nGather your strength and come back! 👋\n')
        else:
            print('\n❌ An invalid value has been entered!\n')


def game_option():
    attempt = [5, 10, 15]
    complexity = ''

    print(
        f'\n\nChoose the difficulty:\n\n🔴 Easy (1) - {attempt[2]} attempts.\n🔴 Medium (2) - {attempt[1]} attempts.\n🔴 Hard (3) - {attempt[0]} attempts.\n')

    while True:
        try:
            choice = int(input('Enter a number (from 1️⃣ to 3️⃣): '))
        except ValueError:
            print('\n❌ Enter a number!\n')
            continue

        if choice <= 0 or choice > 3:
            print('\n❌ Incorrect value!\n')
        else:
            match choice:
                case 1:
                    choice = 15
                    complexity = 'Easy'
                case 2:
                    choice = 10
                    complexity = 'Medium'
                case 3:
                    choice = 5
                    complexity = 'Hard'

            print('\n🚧 Loading...\n')
            time.sleep(2)
            print('✅ Well done!\n')
            print(f'\nSelected difficulty:🔴 {complexity} ({choice} attempts)\n')
            break

    game_play(choice)


def game_play(attempts):
    stats = load_stats()
    print('=' * 31)
    print('| S T A R T  O F  T H E  GAME |\n')

    random_number = randint(1, 100)

    print("I’ve thought of a number... Try to guess it! 👿\n")

    while attempts > 0:
        try:
            player_input = int(input())
        except ValueError:
            print('\n❌ Enter a number!\n')
            continue

        if player_input > 100 or player_input < 0:
            print('\n❌ You’ve gone outside the limits - don’t cheat... I told you, it’s from 1️⃣ to 1️⃣0️⃣0️⃣! 👿\n')
        elif player_input == random_number:
            stats['total_games'] += 1
            stats['wins'] += 1
            save_stats(stats)
            print('\n🎉 Congratulations, you’ve defeated me... But not for long. Next time, I’ll be stronger! 👺\n')
            print('| G A M E  O V E R |')
            print('=' * 20)
            game_conclusion()
        elif player_input > random_number:
            print('LESS! 👹')
            attempts -= 1
        else:
            print('MORE! 👹')
            attempts -= 1

    stats['total_games'] += 1
    stats['losses'] += 1
    save_stats(stats)
    print('\nI won, YES! I always knew I was the strongest 😈👊\n')
    print('| G A M E  O V E R |')
    print('=' * 20)
    game_conclusion()


def game_conclusion():
    stats = load_stats()
    while True:
        print('\n\nDo you want to continue the game❓\n')
        player_input = input('(Yes/No) - ')

        if player_input.lower() == 'yes':
            show_stats(stats)
            game_option()
            break
        elif player_input.lower() == 'no':
            exit('\nCome by again!!! 👿\n')
        else:
            print('\n❌ An invalid value has been entered!\n')


game_greetings()
