import collections
import copy

with open(0) as file:
	lines = file.readlines()
	data = [line.strip() for line in lines]

def is_symbol(c):
	return not (c == '.' or c.isdigit())

def borders_a_symbol(grid, r, c):
	rows, cols = len(grid), len(grid[0])
	for dr in range(-1, 2):
		for dc in range(-1, 2):
			r_, c_ = r + dr, c + dc
			if not(0 <= r_ < rows and 0 <= c_ < cols):
				continue
			if is_symbol(grid[r_][c_]):
				return True
	return False

def get_all_nbr_gears(grid, r, c):
	rows, cols = len(grid), len(grid[0])
	result = []
	for dr in range(-1, 2):
		for dc in range(-1, 2):
			r_, c_ = r + dr, c + dc
			if not(0 <= r_ < rows and 0 <= c_ < cols):
				continue
			if grid[r_][c_] == '*':
				result.append((r_, c_))
	return result

def process(grid):
	result = 0
	rows, cols = len(grid), len(grid[0])
	buffer = []
	include_num = False
	for r in range(rows):
		for c in range(cols):
			if not grid[r][c].isdigit() and buffer:
				if include_num:
					result += int(''.join(buffer))
				include_num = False
				buffer.clear()
				continue
			if grid[r][c].isdigit():
				buffer.append(grid[r][c])
				if borders_a_symbol(grid, r, c):
					include_num = True
	return result

def get_gear_to_nums(num_to_gears):
	result = collections.defaultdict(list)
	for num, gears in num_to_gears.items():
		for gear in gears:
			result[gear].append(num)
	return result

def process2(grid):
	result = 0
	rows, cols = len(grid), len(grid[0])
	buffer = []
	gears_for_buffer = []
	include_num = False
	num_to_gears = collections.defaultdict(list) # map numbers to gear locations
	for r in range(rows):
		for c in range(cols):
			if not grid[r][c].isdigit() and buffer:
				if include_num:
					num = int(''.join(buffer))
					for gear in set(gears_for_buffer):
						num_to_gears[num].append(gear)
					include_num = False
				buffer.clear()
				gears_for_buffer.clear()
				continue
			if grid[r][c].isdigit():
				buffer.append(grid[r][c])
				gears_for_buffer.extend(get_all_nbr_gears(grid, r, c))
				include_num = True
	gear_to_nums = get_gear_to_nums(num_to_gears)
	return sum(nums[0] * nums[1] for nums in gear_to_nums.values() if len(nums) == 2)

print(process(data)) # 559667
print(process2(data)) # 86841457
