# python3 6.py < 6.txt
# python3 6.py < 6t.txt

with open(0) as file:
    data = file.readlines()

def parse_line(line):
    return list(map(int, line.split()[1:]))

times, distances = parse_line(data[0]), parse_line(data[1])

def ints_to_int(arr):
    return int(''.join(map(str, arr)))

def lowest_press_duration(time_, distance):
    def breaks_record(t):
        return t * (time_ - t) > distance
    lo, hi = 0, time_
    while lo <= hi:
        if hi == lo + 1:
            if breaks_record(hi) and not breaks_record(lo):
                return hi
        curr = (lo + hi) // 2
        if breaks_record(curr):
            if curr > 0 and not breaks_record(curr-1):
                return curr
            hi = curr - 1
        else:
            lo = curr + 1
    return hi

result = 1
for t, d in zip(times, distances):
    result *= t - 2*lowest_press_duration(t, d) + 1
print(result) # 220320

t, d = ints_to_int(times), ints_to_int(distances)
print(t - 2*lowest_press_duration(t, d) + 1) # 34454850
