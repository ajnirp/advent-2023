# python3 7.py < 7.txt

from collections import Counter

def parse_line(line):
    hand, bid = line.split()
    bid = int(bid)
    return hand, bid

with open(0) as file:
    data = list(map(parse_line, file.readlines()))

def hand_type(h):
    counts = Counter(h)
    if len(counts) == 1: # five of a kind
        return 7
    elif len(counts) == 2:
        if max(counts.values()) == 4: # four of a kind
            return 6
        else: # full house
            return 5
    elif len(counts) == 3:
        if max(counts.values()) == 3: # three of a kind
            return 4
        else: # two pair
            return 3
    else: # len(counts) == 4
        if max(counts.values()) == 2: # one pair
            return 2
        else: # high card
            return 1

def hand_type2(h):
    if 'J' not in h:
        return hand_type(h)
    counts = Counter(h)
    temp = counts['J'] + max(counts.values())
    if temp == 5: # five of a kind:
        return 7
    elif temp == 4: # four of a kind, never full house
        return 6
    elif temp == 3: # three of a kind, never two pair
        return 4
    else: # temp == 2, one pair, never high card
        return 2

def card_value(c):
    if '2' <= c <= '9':
        return int(c)
    return 10 + 'TJQKA'.index(c)

def card_value2(c):
    if c == 'J':
        return 1
    return card_value(c)

# Compare two pairs p1, p2 consisting of a hand and a bid.
# Bids are ignored.
# Hands are compared based on type (one pair, two pair, etc.).
# If two hands have the same type, find the first card from the left
# that has a stronger value (e.g. K vs T). That hand is "greater".
def sort_key(p):
    result = [hand_type(p[0])] + [card_value(c) for c in p[0]]
    return tuple(result)

def sort_key2(p):
    result = [hand_type2(p[0])] + [card_value2(c) for c in p[0]]
    return tuple(result)

data.sort(key=sort_key)

def score(data):
    result = 0
    for i, pair in enumerate(data):
        result += (i + 1) * pair[1]
    return result

print(score(data)) # 248105065

data.sort(key=sort_key2)

print(score(data))
