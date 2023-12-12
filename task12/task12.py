from functools import cache


@cache
def count(line, groups_count, spring_count=0):
    if not line:
        return not groups_count and not spring_count
    n = 0
    if line[0] in ("#", "?"):
        n += count(line[1:], groups_count, spring_count + 1)
    if line[0] in (".", "?") and (groups_count and groups_count[0] == spring_count or not spring_count):
        n += count(line[1:], groups_count[1:] if spring_count else groups_count)
    return n


def main():
    with open("input.txt") as f:
        line_groups = [l.split() for l in f.read().splitlines()]
        line_groups = [(line, tuple(int(n) for n in groups_count.split(","))) for line, groups_count in line_groups]

        print(sum(count(line + ".", groups_count, 0) for line, groups_count in line_groups))
        print(sum(count("?".join([line] * 5) + ".", groups_count * 5) for line, groups_count in line_groups))


if __name__ == "__main__":
    main()
