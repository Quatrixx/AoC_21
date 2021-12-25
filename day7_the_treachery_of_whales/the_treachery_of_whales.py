def try_position(start_positions, target_pos):
    used_fuel = 0
    for c in start_positions:
        used_fuel += abs(c - target_pos)
    return used_fuel

with open('day7.in') as input:
    crabs = [int(f) for f in input.readline().strip().split(',')]

fuel_values = []
for p in range(min(crabs), max(crabs)+1):
    fuel_values.append(try_position(crabs, p))
print(f"most_efficient_pos @ {fuel_values.index(min(fuel_values))}")
print(f"fuel @ that pos = {min(fuel_values)}")