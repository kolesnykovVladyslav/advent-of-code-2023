import re


def main():
    file = open('input.txt', 'r')
    sum = 0

    while True:
        line = file.readline()
        if not line:
            break

        first, last = extract_digits(line)

        if first and last:
            sum += int(first + last)

    print("sum=" + str(sum))
    file.close()


def extract_digits(s):
    digit_mapping = {'nine': '9',
                     'eight': '8',
                     'two': '2',
                     'one': '1',
                     'three': '3',
                     'four': '4',
                     'five': '5',
                     'six': '6',
                     'seven': '7'
                     }

    # Replace spelled-out digits with numeric representations
    for word, digit in digit_mapping.items():
        s = s.replace(word, word[0] + digit + word[-1])

    # Extract numeric digits using regular expression
    numeric_digits = re.findall(r'\d', s)

    return str(numeric_digits[0]), str(numeric_digits[-1])


if __name__ == "__main__":
    main()
