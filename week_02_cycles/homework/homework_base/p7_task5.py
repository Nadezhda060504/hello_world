"""
Задача 5 (base). Таблица оценок.

Таблица — список списков: строки — студенты, столбцы — оценки.

5.1. Верните плоский список всех оценок (вложенный for).
5.2. Верните сумму всех оценок.
5.3. Верните максимальную оценку.
5.4. Верните количество оценок, равных 5.
5.5. Верните список средних оценок по каждому студенту.
"""


def flat(grades):
    result = []
    for row in grades:
        for grade in row:
            result.append(grade)
    return result


def total(grades):
    result = 0
    for row in grades:
        for grade in row:
            result += grade
    return result


def maximum(grades):
    result = grades[0][0]
    for row in grades:
        for grade in row:
            if grade > result:
                result = grade
    return result


def count_fives(grades):
    count = 0
    for row in grades:
        for grade in row:
            if grade == 5:
                count += 1
    return count


def averages(grades):
    result = []
    for row in grades:
        average = sum(row) / len(row)
        result.append(average)
    return result


if __name__ == "__main__":
    grades = [[5, 4, 5], [3, 3, 4], [5, 5, 5]]

    assert flat(grades) == [5, 4, 5, 3, 3, 4, 5, 5, 5]
    assert total(grades) == 39
    assert maximum(grades) == 5
    assert count_fives(grades) == 5
    assert averages(grades) == [14 / 3, 10 / 3, 5.0]
    print("task5 (base): все тесты пройдены.")
