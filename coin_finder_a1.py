import enum
import random

# coins 
coin_real = 2
coin_fake = 1

Scale = enum.Enum(
    "Scale", ["LeftHeavy", "RightHeavy", "Balanced"]
)

def random_coins(n):
    """A shuffled list of (n-1) real coins and 1 fake coin."""
    assert n > 0
    coins = [coin_real] * (n - 1) + [coin_fake] * (1)
    random.shuffle(coins)
    return coins

def compare(left, right):
    """Weight two collections of coins and return the
    result (a Scale enum).
    """
    delta = sum(right) - sum(left)
    if delta < 0:
        return Scale.LeftHeavy
    elif delta > 0:
        return Scale.RightHeavy
    else:
        return Scale.Balanced
    
def find_fake_coin_fast(*, coins, compare):
    """Find the fake coin quickly by comparing as
    many coins as possible at once.
    """
    k = 0
    pile = list(coins)
    while len(pile) > 1:
        k += 1
        print(f'массив на {k}-ой итерации: {pile}')
        n = len(pile) // 2
        A = pile[:n]
        B = pile[n : 2 * n]

        result = compare(A, B)
        if result == Scale.LeftHeavy:
            pile = B
        elif result == Scale.RightHeavy:
            pile = A
        elif result == Scale.Balanced:
            C = pile[2 * n :]
            pile = C

    return pile[0]

test_pass = 0
test_fail = 0

for _ in range(1):
    coins = random_coins(20)
    print(f'массив из весов фальшивой монеты и настоящих:', coins)
    found = find_fake_coin_fast(
        coins=coins, compare=compare
    )
    print(found)

    if found == coin_fake:
        test_pass += 1
    else:
        test_fail += 1

print("tests passed:", test_pass)
print("tests failed:", test_fail)