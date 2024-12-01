import functools
from collections import defaultdict

ranks = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
ranks_joker = {"A": 14, "K": 13, "Q": 12, "J": 0, "T": 10}


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        solve_task1(lines)
        solve_task2(lines)


def solve_task2(lines):
    hands_types = defaultdict(lambda: list(), {})
    hand_to_bid = dict()
    for line in lines:
        parsed_line = line.split()
        bid = int(parsed_line[1])

        hand = parsed_line[0]
        hand_dict = {i: hand.count(i) for i in hand}

        if 'J' in hand_dict.keys() and len(hand_dict.keys()) > 1:
            joker_count = hand_dict.pop('J')
            max_value = max(hand_dict.values())
            max_card = max([key if hand_dict[key] == max_value else "0" for key in hand_dict.keys()],
                           key=get_card_rank_joker)
            hand_dict[max_card] += joker_count

        _type = (6 - len(hand_dict.keys())) * 3 + max(value for value in hand_dict.values())
        hands_types[_type].append(hand)
        hand_to_bid[hand] = bid

    rank = get_total_winnings(hands_types, hand_to_bid, hand_compare_joker)
    print("Task2: What are the total winnings? " + str(rank))


def solve_task1(lines):
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

    rank = get_total_winnings(hands_types, hand_to_bid, hand_compare)
    print("Task1: What are the total winnings? " + str(rank))


def get_total_winnings(hands_types, hand_to_bid, compare):
    rank = len(hand_to_bid)
    total_winnings = 0
    for _type in sorted(hands_types.keys(), reverse=True):
        hands = hands_types[_type]
        hands.sort(key=functools.cmp_to_key(compare), reverse=True)
        for hand in hands:
            total_winnings += rank * hand_to_bid[hand]
            rank -= 1
    return total_winnings


def get_card_rank(card: str):
    return int(card) if card.isnumeric() else ranks[card]


def get_card_rank_joker(card: str):
    return int(card) if card.isnumeric() else ranks_joker[card]


def hand_compare_joker(hand1, hand2):
    for i in range(len(hand1)):
        rank1 = get_card_rank_joker(hand1[i])
        rank2 = get_card_rank_joker(hand2[i])

        if rank1 != rank2:
            return rank1 - rank2

    return 0


def hand_compare(hand1, hand2):
    for i in range(len(hand1)):
        rank1 = get_card_rank(hand1[i])
        rank2 = get_card_rank(hand2[i])

        if rank1 != rank2:
            return rank1 - rank2

    return 0


if __name__ == "__main__":
    main()
