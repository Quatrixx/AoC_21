with open('day1.in') as input:
    lines = input.readlines()
    measurements = []
    for line in lines:
        measurements.append(int(line.strip()))

# part one
increases = 0
for prev, cur in zip(measurements, measurements[1:]):
    if(cur > prev):
        increases += 1
print(f"part one: {increases} single increases")

# part two
increases = 0
sliding_sums = []
for prevprev, prev, cur in zip(measurements, measurements[1:], measurements[2:]):
    sliding_sums.append(prevprev + prev + cur)
for prev, cur in zip(sliding_sums, sliding_sums[1:]):
    if(cur > prev):
        increases += 1
print(f"part two: {increases} sliding sum increases")