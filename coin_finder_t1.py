import random


def find_fake_coin(coins, num_weighings):
    # Инициализация массива для хранения результатов взвешиваний
    weighing_results = []

    for _ in range(num_weighings):
        # Выбор монет для взвешивания
        left_side = coins[:len(coins) // 2]
        right_side = coins[len(coins) // 2:]

        # Взвешивание
        if sum(left_side) > sum(right_side):
            # Фальшивая монета находится в левой части
            coins = left_side
        elif sum(left_side) < sum(right_side):
            # Фальшивая монета находится в правой части
            coins = right_side
        else:
            # Фальшивая монета находится среди отложенных
            coins = [coin for coin in coins if coin not in left_side and coin not in right_side]

        # Добавление результата взвешивания в список
        weighing_results.append(coins)

    # Проверяем, что фальшивая монета была найдена
    if 0 not in weighing_results[-1]:
        print("Фальшивая монета не была найдена.")
        return None

    # Возвращаем индекс фальшивой монеты
    return weighing_results[-1].index(0)


def main():
    # Создаем массив монет, где одна из них фальшивая
    N = 12  # Общее количество монет
    coins = [1] * (N - 1) + [0]  # Фальшивая монета
    random.shuffle(coins)  # Перемешиваем монеты

    # Выполняем взвешивания
    num_weighings = 3  # Количество взвешиваний
    fake_coin_index = find_fake_coin(coins, num_weighings)

    if fake_coin_index is not None:
        print(f"Индекс фальшивой монеты: {fake_coin_index}")
    else:
        print("Фальшивая монета не была найдена.")


if __name__ == "__main__":
    main()
