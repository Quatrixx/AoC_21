grid = [[0 for x in range(1000)] for y in range(1000)]

def plot_vents_to_file():
    with open('day5.out', 'w') as output:
        for row in grid:
            line_string = ''
            for n in row:
                line_string += str(n)
            line_string += '\n'
            output.write(line_string)

def draw_vent(start: tuple, end: tuple):
    if start == end:
        grid[start[0]][start[1]] += 1
    elif start[1] == end[1]:
        if start[0] > end[0]:
            for x in range(start[0], end[0]-1, -1):
                grid[x][start[1]] += 1
        else:
            for x in range(start[0], end[0]+1):
                grid[x][start[1]] += 1
    elif start[0] == end[0]:
        if start[1] > end[1]:
            for y in range(start[1], end[1]-1, -1):
                grid[start[0]][y] += 1
        else:
            for y in range(start[1], end[1]+1):
                grid[start[0]][y] += 1
    else: # diagonal vent (for part two)
        if start[0] > end[0]:
            if start[1] > end[1]:
                for (x, y) in zip(range(start[0], end[0]-1, -1), range(start[1], end[1]-1, -1)):
                    grid[x][y] += 1
            else:
                for (x, y) in zip(range(start[0], end[0]-1, -1), range(start[1], end[1]+1)):
                    grid[x][y] += 1
        else:
            if start[1] > end[1]:
                for (x, y) in zip(range(start[0], end[0]+1), range(start[1], end[1]-1, -1)):
                    grid[x][y] += 1
            else:
                for (x, y) in zip(range(start[0], end[0]+1), range(start[1], end[1]+1)):
                    grid[x][y] += 1

diagonal_vents = []
with open('day5.in') as input:
    for line in input:
        split_line = line.strip().split(' -> ')
        for i, half in enumerate(split_line):
            if i == 0:
                start_coords = [int(n) for n in half.split(',')]
            else:
                end_coords = [int(n) for n in half.split(',')]
        if (start_coords[0] != end_coords[0]) & (start_coords[1] != end_coords[1]):
            diagonal_vents.append((start_coords, end_coords))
        else:
            draw_vent(start_coords, end_coords)

overlaps = 0
for row in grid:
    for p in row:
        if p >= 2:
            overlaps += 1
print(f"part1: straight_intersects= {overlaps}")
plot_vents_to_file()

for vent in diagonal_vents:
    draw_vent(vent[0], vent[1])

overlaps = 0
for row in grid:
    for p in row:
        if p >= 2:
            overlaps += 1
print(f"part2: all_intersects= {overlaps}")