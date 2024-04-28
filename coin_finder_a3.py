def find_fake_coin(coins, start, end):
    # Base case: only one coin left
    if start == end:
        return coins[start]
    
    # Divide the search space into three parts
    size = end - start + 1
    part_size = size // 3
    
    # Calculate the indices of the midpoints
    mid1 = start + part_size
    mid2 = start + 2 * part_size
    
    # Weigh the coins in the first and second thirds
    left_sum = sum(coins[start:mid1])
    mid_sum = sum(coins[mid1:mid2])
    
    # If the weights are different, recurse on the lighter portion
    if left_sum < mid_sum:
        return find_fake_coin(coins, start, mid1 - 1)
    elif left_sum > mid_sum:
        return find_fake_coin(coins, mid1, mid2 - 1)
    else:
        # If weights are the same, check the last third
        last_sum = sum(coins[mid2:end+1])
        if last_sum < mid_sum:  # Last third is lighter
            return find_fake_coin(coins, mid2, end)
        elif last_sum > mid_sum:  # Last third is heavier
            return find_fake_coin(coins, mid1, mid2 - 1)
        else:  # All thirds are equal, we haven't found the fake coin yet
            return "No fake coin"  # Indicate that there's no fake coin

# Wrapper function for simplicity
def find_fake_coin_wrapper(coins):
    if not coins:
        return "No coins provided"
    result = find_fake_coin(coins, 0, len(coins) - 1)
    if isinstance(result, int):
        return result
    else:
        return result

