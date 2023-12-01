import re

file = open('input.txt', 'r')
sum = 0

while True:
    line = file.readline()
    if not line:
        break

    # Finding first number
    first = re.search(r'\d', line)
    # Finding last number
    last = re.search(r'\d', line[::-1])

    if first and last:
        sum += int(first.group() + last.group())

print("sum=" + str(sum))
file.close()
