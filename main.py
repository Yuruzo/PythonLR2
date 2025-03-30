def guess_number_game():
    import sys

    # Читаем максимальное число
    max_number = int(sys.stdin.readline().strip())
    possible_numbers = set(range(1, max_number + 1))

    while True:
        line = sys.stdin.readline().strip()

        if line == "HELP":
            break

        question = set(map(int, line.split()))

        # Выбираем ответ так, чтобы оставить больше чисел
        if len(question & possible_numbers) * 2 == len(possible_numbers):
            response = "NO"
        else:
            response = "YES" if len(question & possible_numbers) > len(possible_numbers) / 2 else "NO"

        print(response)

        if response == "YES":
            possible_numbers &= question
        else:
            possible_numbers -= question

    print(" ".join(map(str, sorted(possible_numbers))))


# Запуск программы для чтения из стандартного ввода
if __name__ == "__main__":
    guess_number_game()
