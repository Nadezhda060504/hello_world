# task3.py — Домашняя работа 6, базовый уровень.
# Задача 3. Разбор строки лога.


# ============================================================
# Задача 3. Разбор строки лога
# ============================================================
# На вход приходит строка вида "LEVEL:message".
# Например: "INFO:start", "ERROR:disk full".
#
# Подзадачи:
#   3.1. Вернуть уровень (до ':').
#   3.2. Вернуть сообщение (после ':').
#   3.3. Вернуть True, если уровень — "ERROR" или "WARN".
#   3.4. Вернуть True, если сообщение не пустое и не содержит пробелов
#        в начале/конце.
#   3.5. Нормализовать: уровень в верхнем регистре, сообщение в нижнем,
#        склеить через ':'.

def hw_3_1_level(line: str) -> str:
    """Вернуть уровень до ':'."""
    return line.split(":")[0]


def hw_3_2_message(line: str) -> str:
    """Вернуть сообщение после ':'."""
    return line.split(":")[1]



def hw_3_3_is_alert(line: str) -> bool:
    """Вернуть True, если уровень 'ERROR' или 'WARN'."""
    level = hw_3_1_level(line)
    return level == "ERROR" or level == "WARN"


def hw_3_4_message_clean(line: str) -> bool:
    """Вернуть True, если сообщение не пустое и без пробелов по краям."""
    message = hw_3_2_message(line)
    return message != "" and message == message.strip()



def hw_3_5_normalize(line: str) -> str:
    """Вернуть 'LEVEL:message' в нормализованном виде."""
    level = hw_3_1_level(line).upper()
    message = hw_3_2_message(line).lower()
    return level + ":" + message


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    assert hw_3_1_level("INFO:start") == "INFO"
    assert hw_3_2_message("INFO:start") == "start"
    assert hw_3_3_is_alert("ERROR:disk full") is True
    assert hw_3_3_is_alert("WARN:low memory") is True
    assert hw_3_3_is_alert("INFO:start") is False
    assert hw_3_4_message_clean("INFO:start") is True
    assert hw_3_4_message_clean("INFO:") is False
    assert hw_3_4_message_clean("INFO: start ") is False
    assert hw_3_5_normalize("info:START") == "INFO:start"
    assert hw_3_5_normalize("Error:DISK Full") == "ERROR:disk full"

    print("task3: все assert-тесты пройдены.")
