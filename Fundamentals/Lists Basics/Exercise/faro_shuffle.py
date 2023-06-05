cards = input().split()
count_of_shuffles = int(input())

for shuffle in range(count_of_shuffles):
    shuffled_cards = []
    for card_index in range(len(cards) // 2):
        card = cards[card_index]
        shuffled_cards.append(card)
        next_card = cards[card_index + len(cards) // 2]
        shuffled_cards.append(next_card)
    cards = shuffled_cards

print(shuffled_cards)
