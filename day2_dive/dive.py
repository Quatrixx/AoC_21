with open('day2.in') as input:
    lines = input.readlines()
    commands = [];
    for line in lines:
        commands.append(tuple(line.strip().split(" ")));

# part one
h_pos, depth = 0, 0
for op, d in commands:
    d = int(d)
    match op:
        case 'forward':
            h_pos += d
        case 'down':
            depth += d
        case 'up':
            depth -= d
product = h_pos * depth
print(f"part one: {product}")

# part two
h_pos, depth = 0, 0
aim = 0
for op, d in commands:
    d = int(d)
    match op:
        case 'forward':
            h_pos += d
            depth += aim * d
        case 'down':
            aim += d
        case 'up':
            aim -= d
product = h_pos * depth
print(f"part two: {product}")