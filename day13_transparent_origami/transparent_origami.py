with open('day13.in') as input:
    lines = [l.strip() for l in input.readlines()]

    dot_instructions = [l.split(',') for l in lines[:lines.index('')]]
    dot_instructions = [[int(n) for n in instr] for instr in dot_instructions]

    fold_instructions = [l.split('=') for l in lines[lines.index('')+1:]]
    for index, instruction in enumerate(fold_instructions):
        # first part: only last char ('x'/'y')
        fold_instructions[index][0] = instruction[0][-1]
        # second part: as int
        fold_instructions[index][1] = int(instruction[1])

rows, columns = 0, 0
for (axis, value) in fold_instructions[:2]:
    if axis == 'x':
        rows = value * 2 + 1
    elif axis == 'y':
        columns = value * 2 + 1

paper_grid = [[0 for x in range(rows)] for y in range(columns)]

for (x, y) in dot_instructions:
    paper_grid[y][x] = 1

for instruction_index, (axis, value) in enumerate(fold_instructions):
    moving_half = []
    if axis == 'x':
        for y in range(len(paper_grid)):
            paper_grid[y][value] = '-'
            moving_half_row = paper_grid[y][(value+1):]
            moving_half_row.reverse()
            moving_half.append(moving_half_row)
        for y in range(len(moving_half)):
            for x in range(len(moving_half[y])):
                paper_grid[y][x] += moving_half[y][x]
        paper_grid = [row[:value] for row in paper_grid]
    elif axis == 'y':
        for x in range(len(paper_grid[value])):
            paper_grid[value][x] = '-'
        moving_half = paper_grid[(value+1):]
        moving_half.reverse()
        for y in range(len(moving_half)):
            for x in range(len(moving_half[y])):
                paper_grid[y][x] += moving_half[y][x]
        paper_grid = paper_grid[:value]
    if instruction_index == 0:
        dots = 0
        for row in paper_grid:
            for p in row:
                if p != 0:
                    dots += 1
        print(f"part1: {dots} dots after 1st fold")

print(f"part2:")
for row in paper_grid:
    row_string = ''
    for p in row:
        if p == 0:
            row_string += '.'
        else:
            row_string += '#'
    print(row_string)
