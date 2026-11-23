# p8_task4.py — Домашняя работа 8, базовый уровень.
# Задача 4. Лог-файл на диске: запись, чтение, сводка.
#
# Работаем с файлом во временной директории (tempfile),
# чтобы не зависеть от текущего каталога.
#
# Подзадачи:
#   4.1. Записать строки в файл (каждая — с переводом строки).
#   4.2. Прочитать все строки файла в список (без переводов строк).
#   4.3. Вернуть число непустых строк в файле.
#   4.4. Дописать строку в конец файла (режим "a").
#   4.5. Вернуть словарь {первое слово строки: количество строк}
#        по непустым строкам файла.


def write_lines(path: str, lines: list[str]) -> None:
    """Записать строки в файл, каждая с переводом строки."""
    with open(path, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


def read_lines(path: str) -> list[str]:
    """Прочитать строки файла без символов перевода строки."""
    with open(path, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    return lines


def count_nonempty(path: str) -> int:
    """Число непустых строк в файле."""
    count = 0

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                count += 1

    return count


def append_line(path: str, line: str) -> None:
    """Дописать строку в конец файла."""
    with open(path, "a", encoding="utf-8") as file:
        file.write(line + "\n")


def first_word_counts(path: str) -> dict[str, int]:
    """{первое слово: количество строк} по непустым строкам."""
    result = {}

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            words = line.split()

            if words:
                first_word = words[0]
                result[first_word] = result.get(first_word, 0) + 1

    return result


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    import os
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "log.txt")

        write_lines(path, ["alice login", "bob upload", "", "alice logout"])
        assert os.path.exists(path)

        assert read_lines(path) == ["alice login", "bob upload", "", "alice logout"]
        assert count_nonempty(path) == 3

        append_line(path, "carol login")
        assert read_lines(path)[-1] == "carol login"

        assert first_word_counts(path) == {"alice": 2, "bob": 1, "carol": 1}

        # перезапись
        write_lines(path, ["only one"])
        assert read_lines(path) == ["only one"]
        assert count_nonempty(path) == 1

        # пустой файл
        write_lines(path, [])
        assert read_lines(path) == []
        assert count_nonempty(path) == 0
        assert first_word_counts(path) == {}

    print("p8_task4 (base): все assert-тесты пройдены.")
