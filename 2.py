import collections
import copy

MAX_COLOR = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

with open(0) as file:
    data = file.readlines()

def parse_line(line):
    split = line.split()
    split[-1] = split[-1] + ';'
    game_id = int(split[1][:-1])
    games = []
    game = collections.defaultdict(int)
    for i in range(2, len(split), 2):
        num = int(split[i])
        color = split[i+1]
        color, delimiter = color[:-1], color[-1]
        if delimiter == ',':
            game[color] = num
        else:
            game[color] = num
            games.append(copy.deepcopy(game))
            game.clear()
    return game_id, games

def process(data):
    result = 0
    for line in data:
        game_id, games = parse_line(line)
        if all(game[color] <= MAX_COLOR[color] for game in games for color in game):
            result += game_id
    return result

def process2(data):
    result = 0
    for line in data:
        game_id, games = parse_line(line)
        curr = 1
        for color in MAX_COLOR:
            curr *= max(game[color] for game in games)
        result += curr
    return result

print(process(data)) # 2176
print(process2(data)) # 63700
