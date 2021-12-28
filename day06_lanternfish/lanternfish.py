with open('day6.in') as input:
    initial_state = [int(f) for f in input.readline().strip().split(',')]

fish_timers = [0 for n in range(0, 8+1)]
for timer_value in initial_state:
    fish_timers[timer_value] += 1

sim_end = 256
print(f'simulating fish... (initial_pop:{len(initial_state)})')
for day in range(1, sim_end+1):
    next_day_timers = [0 for t in fish_timers]
    for timer_value, amount in enumerate(fish_timers):
        if timer_value == 0:
            breeders = amount
            next_day_timers[8] += amount
        else:
            next_day_timers[timer_value-1] = amount
    next_day_timers[6] += breeders
    fish_timers = next_day_timers
    if (day == 80) | (day == sim_end):
        print(f'day {day:3}/{sim_end}: {sum(fish_timers)}')