# p8_task5.py — Домашняя работа 8, базовый уровень.
# Задача 5. Отчёт по сессиям: кортежи + множества + while.
#
# Сессии — список кортежей (user, start, end), где start/end — int (минуты).
# Например: ("alice", 0, 30), ("bob", 10, 20), ("alice", 40, 50).
#
# Подзадачи:
#   5.1. Вернуть кортеж (общая длительность, число сессий).
#   5.2. Вернуть словарь {user: суммарная длительность}.
#   5.3. Вернуть множество пользователей, у которых была
#        хотя бы одна сессия короче 15 минут.
#   5.4. Вернуть кортеж (user, длительность) самой длинной сессии;
#        при равенстве — лексикографически меньший user.
#   5.5. Вернуть True, если интервалы всех сессий корректны (start <= end),
#        иначе False. Проверить через while по индексам.


def total_and_count(sessions: list[tuple[str, int, int]]) -> tuple[int, int]:
    """Общая длительность и число сессий."""
    total = 0
    count = 0

    for user, start, end in sessions:
        total += end - start
        count += 1

    return (total, count)


def duration_by_user(sessions: list[tuple[str, int, int]]) -> dict[str, int]:
    """Суммарная длительность по пользователям."""
    result = {}

    for user, start, end in sessions:
        duration = end - start
        result[user] = result.get(user, 0) + duration

    return result


def short_session_users(sessions: list[tuple[str, int, int]], limit: int = 15) -> set[str]:
    """Пользователи с хотя бы одной сессией короче limit."""
    result = set()

    for user, start, end in sessions:
        duration = end - start

        if duration < limit:
            result.add(user)

    return result


def longest_session(sessions: list[tuple[str, int, int]]) -> tuple[str | None, int]:
    """Самая длинная сессия: (user, длительность)."""
    if not sessions:
        return (None, 0)

    best_user = None
    best_duration = -1

    for user, start, end in sessions:
        duration = end - start

        if duration > best_duration:
            best_user = user
            best_duration = duration

        elif duration == best_duration and user < best_user:
            best_user = user

    return (best_user, best_duration)


def sessions_valid(sessions: list[tuple[str, int, int]]) -> bool:
    """True, если у всех сессий start <= end."""
    i = 0

    while i < len(sessions):
        user, start, end = sessions[i]

        if start > end:
            return False

        i += 1

    return True


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    SESSIONS = [
        ("alice", 0, 30),
        ("bob", 10, 20),
        ("alice", 40, 50),
        ("carol", 5, 8),
    ]

    assert total_and_count(SESSIONS) == (30 + 10 + 10 + 3, 4)
    assert total_and_count([]) == (0, 0)

    assert duration_by_user(SESSIONS) == {"alice": 40, "bob": 10, "carol": 3}
    assert duration_by_user([]) == {}

    assert short_session_users(SESSIONS) == {"bob", "carol"}
    assert short_session_users(SESSIONS, limit=5) == {"carol"}
    assert short_session_users([]) == set()

    assert longest_session(SESSIONS) == ("alice", 30)
    assert longest_session([("b", 0, 10), ("a", 0, 10)]) == ("a", 10)
    assert longest_session([]) == (None, 0)

    assert sessions_valid(SESSIONS) is True
    assert sessions_valid([("a", 5, 5)]) is True
    assert sessions_valid([("a", 10, 5)]) is False
    assert sessions_valid([]) is True

    print("p8_task5 (base): все assert-тесты пройдены.")
