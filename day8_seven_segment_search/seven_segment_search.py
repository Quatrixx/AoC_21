with open('day8.in') as input:
    display_notes = [v for v in [d.strip().split(" | ")[1].split(' ') for d in input.readlines()]]

unique_digit_count = 0
for d in display_notes:
    for v in d:
        active_segments = len(v)
        if (active_segments == 2) | (active_segments == 4) | \
        (active_segments == 3) | (active_segments == 7):
            unique_digit_count += 1

print(f"unique_digits= {unique_digit_count}")