def display_hand(msg, hand):
    c = 0
    print(msg)
    for card in hand:
        if c % 3 == 0:
            print()
        print(f"position: {c + 1}. card: {card[0]}{card[1]}", end="\t")
        c += 1
    print("\n")

def display_table(msg, table):
    for sets in table:
        for card in sets:
            print()