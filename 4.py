import collections

with open(0) as file:
    data = [line.strip() for line in file.readlines()]

def get_nums(s):
    return [int(n) for n in s.split()]

def parse_line(line):
    card_id = int(line.split()[1][:-1])
    nums = line.split(':')[1]
    winning, guesses = nums.split(' | ')
    winning = get_nums(winning)
    guesses = get_nums(guesses)
    return card_id, winning, guesses

def score(winning, guesses):
    n = len(set(winning).intersection(set(guesses)))
    if n == 0:
        return 0
    return 1 << (n-1)

def process(data):
    lines = list(map(parse_line, data))
    return sum(score(*line[1:]) for line in lines)

def process_card2(card_id, winning, guesses, scratchcards):
    matches = set(winning).intersection(set(guesses))
    copies_won = scratchcards[card_id]
    if matches:
        for i in range(card_id + 1, card_id + 1 + len(matches)):
            scratchcards[i] += copies_won

def process2(data):
    scratchcards = collections.Counter({i: 1 for i in range(1, len(data) + 1)})
    lines = list(map(parse_line, data))
    for card_id, winning, guesses in lines:
        process_card2(card_id, winning, guesses, scratchcards)
    return sum(scratchcards.values())

print(process(data)) # 24542
print(process2(data)) # 8736438
