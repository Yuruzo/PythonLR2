def create_latin_to_english_dict():
    # Чтение количества английских слов в словаре
    N = int(input())

    # Словарь для латинских слов, где ключ - латинское слово, а значение - множество английских слов
    latin_to_english = {}

    # Чтение записей в англо-латинском словаре
    for _ in range(N):
        # Ввод записи: английское слово и переводы на латинский
        line = input().strip()
        eng_word, latin_words_str = line.split(" - ")
        latin_words = latin_words_str.split(", ")

        # Добавляем для каждого латинского слова соответствующее английское слово
        for latin_word in latin_words:
            if latin_word not in latin_to_english:
                latin_to_english[latin_word] = []
            latin_to_english[latin_word].append(eng_word)

    # Сортировка латинских слов по лексикографическому порядку
    sorted_latin_words = sorted(latin_to_english.keys())

    # Выводим латинско-английский словарь
    for latin_word in sorted_latin_words:
        # Сортируем английские слова для текущего латинского
        english_words = sorted(latin_to_english[latin_word])
        # Выводим латинское слово и переводы
        print(f"{latin_word} - {', '.join(english_words)}")


# Запуск программы
create_latin_to_english_dict()
