import re


def main():
    file = open('input.txt', 'r')
    _sum = 0
    scratchcards_count = 0
    scratchcards_to_count = {}

    card = 1
    while True:
        line = file.readline()
        if not line:
            break

        scratchcard = line.split(':')[1].split('|')
        my_numbers = set(map(int, re.findall('\d+', scratchcard[1])))
        winning_numbers = set(map(int, re.findall('\d+', scratchcard[0])))

        count = get_occurrences_number(winning_numbers, my_numbers)
        _sum += 2 ** (count - 1) if count > 0 else 0

        # add original card
        scratchcards_to_count[card] = scratchcards_to_count.get(card, 0) + 1
        # add for count number of following cards the number of current card copies
        for i in range(1, count + 1):
            scratchcards_to_count[card + i] = scratchcards_to_count.get(card + i, 0) + scratchcards_to_count[card]
        # increment card
        scratchcards_count += scratchcards_to_count[card]
        card += 1

    print("Points = " + str(_sum))
    print("Total scratchcards do you end up with = " + str(scratchcards_count))
    file.close()


def get_occurrences_number(original_set, my_numbers):
    count = 0
    for num in my_numbers:
        if num in original_set:
            count += 1
    return count


if __name__ == "__main__":
    main()
