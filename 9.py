def parse_data(data):
    result = []
    for line in data:
        result.append(list(map(int, line.split())))
    return result

with open(0) as file:
    data = parse_data(file.readlines())

def diffs(seq):
    diffs = [seq]
    curr = seq
    while True:
        diff = [curr[i+1] - curr[i] for i in range(len(curr)-1)]
        diffs.append(diff)
        if all(x == diff[0] for x in diff):
            break
        curr = diff
    return diffs

def predict_next(seq):
    ds = diffs(seq)
    return sum(x[-1] for x in ds)

def predict_prev(seq):
    ds = diffs(seq)
    curr = ds[-1][0]
    for i in range(len(ds)-2, -1, -1):
        curr = ds[i][0] - curr
    return curr

print(sum(map(predict_next, data))) # 1806615041
print(sum(map(predict_prev, data)))
