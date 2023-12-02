with open(0) as file:
    data = [line.strip() for line in file.readlines()]

# returns None if no digit found
def first_digit(line):
    for i, c in enumerate(line):
        if c.isdigit():
            return i, int(c)

total = 0
for line in data:
    first = first_digit(line)
    second = first_digit(reversed(line))
    if first and second:
        num = first[1]*10 + second[1]
        total += num

print(total) # 55090

def net_calibration_value(line):
    def find_first(line, num):
        return line.find(num)

    def find_last(line, num):
        reverse_line = ''.join(reversed(line))
        reverse_num = ''.join(reversed(num))
        return reverse_line.find(reverse_num)

    def calibration_value(line, search_method):
        idx = float('inf')
        result = None
        for digit in digits:
            occurrence = search_method(line, digit)
            if -1 < occurrence < idx:
                idx = min(idx, occurrence)
                result = digits[digit]
        for i in range(1, 10):
            occurrence = search_method(line, str(i))
            if -1 < occurrence < idx:
                idx = occurrence
                result = i
        return result

    digits = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    first = calibration_value(line, find_first)
    second = calibration_value(line, find_last)

    # Assumption: the input is such that `first` and `second` never end up being
    # `None`.
    return first*10 + second

total = 0
for line in data:
    total += net_calibration_value(line)

print(total) # 54845
