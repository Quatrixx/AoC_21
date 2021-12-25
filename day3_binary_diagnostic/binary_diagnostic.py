def get_most_common_bits(bit_lists):
    mcb = ""
    for bit_list in bit_lists:
        if bit_list.count(1) > bit_list.count(0):
            mcb += '1'
        elif bit_list.count(1) < bit_list.count(0):
            mcb += '0'
        else:
            mcb += '2'
    return mcb

def get_least_common_bits(bit_lists):
    lcb = get_most_common_bits(bit_lists)
    trans = []
    trans.append(lcb.maketrans('0', '3'))
    trans.append(lcb.maketrans('1', '0'))
    trans.append(lcb.maketrans('3', '1'))
    for t in trans:
        lcb = lcb.translate(t)
    return lcb

def make_bit_position_lists(bit_strings):
    position_lists = [[]]
    for bit_string in bit_strings:
        for pos, bit in enumerate(bit_string):
            if len(position_lists) == pos:
                position_lists.append(list())
            position_lists[pos].append(int(bit))
    return position_lists


with open('day3.in') as input:
    lines = input.readlines()
    measurements = []
    for line in lines:
        measurements.append(line.strip())

# part one
measurements_bit_position_lists = make_bit_position_lists(measurements)
gamma_rate = int(get_most_common_bits(measurements_bit_position_lists), base=2)
epsilon_rate = gamma_rate ^ 0xFFF
power_consumption = gamma_rate * epsilon_rate
print(f"mcb= {bin(gamma_rate):14} gamma_rate= {gamma_rate}\n"
    f"lcb= {bin(epsilon_rate):14} epsil_rate= {epsilon_rate}\n"
    f"power_consumption= {power_consumption}\n")

# part two
shrinking_measurements = measurements
for i in range(12):
    if len(shrinking_measurements) == 1:
            break
    mcb = get_most_common_bits(make_bit_position_lists(shrinking_measurements))
    debug = [m for m in shrinking_measurements if (m[i] == mcb[i]) | ((mcb[i] == '2') & (m[i] == '1'))]
    shrinking_measurements = debug
oxygen_generator_rating = int(shrinking_measurements[0], base=2)

shrinking_measurements = measurements
for i in range(12):
    if len(shrinking_measurements) == 1:
            break
    lcb = get_least_common_bits(make_bit_position_lists(shrinking_measurements))
    shrinking_measurements = [m for m in shrinking_measurements if (m[i] == lcb[i]) | ((lcb[i] == '2') & (m[i] == '0'))]
co2_scrubber_rating = int(shrinking_measurements[0], base=2)
life_support_rating = oxygen_generator_rating * co2_scrubber_rating
print(f"oxygen_gen_r= {oxygen_generator_rating} co2_scrubber_r= {co2_scrubber_rating}\n"
    f"life_support_r= {life_support_rating}")