import random

def find_fake_coin(data, start, end, total_items):
    if total_items == 1:
        return (0, start)
    elif total_items == 2:
        if data[start] > data[end]:
            return (1, end)
        elif data[start] < data[end]:
            return (1, start)
    else:
        partition = total_items // 3
        a_weight = sum(data[start:start+partition])
        b_weight = sum(data[start+partition:start+2*partition])
        c_weight = sum(data[start+2*partition:end])
        if a_weight == b_weight:
            result = find_fake_coin(data, start+2*partition, end, end-start-2*partition)
            return (1+result[0], result[1])
        else:   
            if a_weight > b_weight:
                result = find_fake_coin(data, start, start+partition, partition)
                return (1+result[0], result[1])
            else:
                result = find_fake_coin(data, start+partition, start+2*partition, partition)
                return (1+result[0], result[1])

n = 39
for bad_coin in range(n):
    data = [1]*n
    data[bad_coin] = 0
    total_weighing, position = find_fake_coin(data, 0, n, n)
    print(f"Пробный сброс {bad_coin}")
    if total_weighing != 4:
        print("Неверное количество взвешиваний:", total_weighing)
    if position != bad_coin:
        print("Неверный ID:", position)