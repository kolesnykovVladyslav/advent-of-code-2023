import functools
from collections import defaultdict

ranks = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}


def get_card_rank(card: str):
    return int(card) if card.isnumeric() else ranks[card]


def hand_compare(hand1, hand2):
    for i in range(len(hand1)):
        rank1 = get_card_rank(hand1[i])
        rank2 = get_card_rank(hand2[i])

        if rank1 != rank2:
            return rank1 - rank2

    return 0


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        hands_types = defaultdict(lambda: list(), {})
        hand_to_bid = dict()
        for line in lines:
            parsed_line = line.split()
            bid = int(parsed_line[1])

            hand = parsed_line[0]
            hand_dict = {i: hand.count(i) for i in hand}
            _type = (6 - len(hand_dict.keys())) * 3 + max(value for value in hand_dict.values())

            hands_types[_type].append(hand)
            hand_to_bid[hand] = bid

        rank = len(hand_to_bid)
        total_winnings = 0
        for _type in sorted(hands_types.keys(), reverse=True):
            hands = hands_types[_type]
            hands.sort(key=functools.cmp_to_key(hand_compare), reverse=True)
            for hand in hands:
                total_winnings += rank * hand_to_bid[hand]
                rank -= 1

        print("What are the total winnings? " + str(total_winnings))


if __name__ == "__main__":
    main()
