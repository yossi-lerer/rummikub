import random

def create_pool():
    pool = []
    for symbol in ["R", "B", "K", "O"]:
        for num in range(1,14):
            pool.append((num, symbol))
    pool = pool * 2
    random.shuffle(pool)
    return pool

def is_valid_set(tiles):
    pass

def play_set(hand, table, indexes):
    pass

print(create_pool())