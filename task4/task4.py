import re


def main():
    file = open('input.txt', 'r')
    _sum = 0

    while True:
        line = file.readline()
        if not line:
            break

        scratchcard = line.split(':')[1].split('|')
        my_numbers = set(map(int, re.findall('\d+', scratchcard[1])))
        winning_numbers = set(map(int, re.findall('\d+', scratchcard[0])))

        count = 0
        for num in my_numbers:
            if num in winning_numbers:
                count += 1

        _sum += 2 ** (count - 1) if count > 0 else 0

    print("Points = " + str(_sum))
    file.close()


if __name__ == "__main__":
    main()
