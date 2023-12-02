def main():
    file = open('games_input.txt', 'r')
    _sum = 0

    while True:
        line = file.readline()
        if not line:
            break

        _sum += get_game_id(line)

    print("Sum games IDs = " + str(_sum))
    file.close()


def get_game_id(line: str):
    return 1


if __name__ == "__main__":
    main()
