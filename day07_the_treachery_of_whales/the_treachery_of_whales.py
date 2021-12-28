def try_position(start_positions, target_pos, fuel_use_is_nonlinear=False):
    used_fuel = 0
    if fuel_use_is_nonlinear:
        for c in start_positions:
            used_fuel += sum(range(abs(c - target_pos)+1))
    else:
        for c in start_positions:
            used_fuel += abs(c - target_pos)
    return used_fuel

with open('day7.in') as input:
    crabs = [int(f) for f in input.readline().strip().split(',')]

# oart one
fuel_values = []
for p in range(min(crabs), max(crabs)+1):
    fuel_values.append(try_position(crabs, p))
print(f"part 1, linear fuel use:")
print(f"most_efficient_pos @ {fuel_values.index(min(fuel_values))}")
print(f"fuel_for_mep = {min(fuel_values)}")
print()

# part two
fuel_values = []
for p in range(min(crabs), max(crabs)+1):
    fuel_values.append(try_position(crabs, p, fuel_use_is_nonlinear=True))
print(f"part 2, factorial fuel use:")
print(f"most_efficient_pos @ {fuel_values.index(min(fuel_values))}")
print(f"fuel_for_mep = {min(fuel_values)}")