
"""
Задача 4 (base). Корзина покупок.
Корзина — список цен (числа).

4.1. Добавьте к корзине новую цену price (метод append).
4.2. Удалите первую цену из корзины (метод pop(0)).
4.3. Отсортируйте корзину по возрастанию (метод sort).
4.4. Верните копию корзины (метод copy).
4.5. Верните список цен со скидкой 10% (x * 0.9).
"""


def add_price(cart, price):
    cart.append(price)
    return cart


def remove_first(cart):
    cart.pop(0)
    return cart


def sorted_cart(cart):
    cart.sort()
    return cart


def copy_cart(cart):
    return cart.copy()


def discounted(cart):
    result = []
    for x in cart:
        result.append(x * 0.9)
    return result


if __name__ == "__main__":
    assert add_price([100, 200], 300) == [100, 200, 300]
    assert remove_first([100, 200, 300]) == [200, 300]
    assert sorted_cart([300, 100, 200]) == [100, 200, 300]
    assert copy_cart([100, 200]) == [100, 200]
    assert discounted([100, 200]) == [90.0, 180.0]

    print("task4 (base): все тесты пройдены.")
