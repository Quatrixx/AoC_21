with open('day8.in') as input:
    split_lines = [line.strip().split(" | ") for line in input.readlines()]
    unique_patterns_list = [h[0].split(' ') for h in split_lines]
    output_values_list = [h[1].split(' ') for h in split_lines]

# part one
unique_digit_count = 0
for display in output_values_list:
    for digit_segments in display:
        match len(digit_segments):
            case 2 | 3 | 4 | 7:
                unique_digit_count += 1
            case _:
                pass

print(f"part 1: total_unique_digits= {unique_digit_count}")

# part two
print("part 2:")
def first_of_len(patterns, target_len):
    for p in patterns:
        if len(p) == target_len:
            return p

def first_of_len_without(patterns, target_len, exclusion):
    for p in patterns:
        if (len(p) == target_len) & (exclusion not in p):
            return p

def last_of_len_without(patterns, target_len, exclusion):
    for p in reversed(patterns):
        if (len(p) == target_len) & (exclusion not in p):
            return p

def get_common(patterns: list):
    ret_pat = ''
    for s in patterns[0]:
        is_common = True
        for p in patterns[1:]:
            if s not in p:
                is_common = False
        if is_common:
            ret_pat += s
    return ret_pat

def p_sub(pat_a: str, pat_b: str):
    ret_pat = ''
    for s in pat_a:
        if s not in pat_b:
            ret_pat += s
    return ret_pat
    
def p_add(pat_a: str, pat_b: str):
    ret_pat = pat_a
    for s in pat_b:
        if s not in ret_pat:
            ret_pat += s
    return ret_pat

sum = 0
for display_nr, (patterns, output) in enumerate(zip(unique_patterns_list, output_values_list)):
    patterns.sort(key=len)
    wire_dict = {}
    wire_dict['A'] = p_sub(first_of_len(patterns, 3), first_of_len(patterns, 2))
    wire_dict['5c'] = get_common([p for p in patterns if len(p) == 5])
    wire_dict['B'] = p_sub(p_sub(first_of_len(patterns, 4), first_of_len(patterns, 2)), wire_dict['5c'])
    wire_dict['D'] = p_sub(p_sub(first_of_len(patterns, 4), first_of_len(patterns, 2)), wire_dict['B'])
    wire_dict['6c'] = get_common([p for p in patterns if len(p) == 6])
    wire_dict['F'] = p_sub(p_sub(wire_dict['6c'], wire_dict['5c']), wire_dict['B'])
    wire_dict['5/f'] = first_of_len_without(patterns, 5, wire_dict['F'])
    wire_dict['5&f'] = p_add(first_of_len_without(patterns, 5, wire_dict['5/f']), last_of_len_without(patterns, 5, wire_dict['5/f']))
    wire_dict['E'] = p_sub(first_of_len(patterns, 7), wire_dict['5&f'])
    wire_dict['G'] = p_sub(p_sub(p_sub(first_of_len(patterns, 7), first_of_len(patterns, 4)), wire_dict['A']), wire_dict['E'])
    for p in patterns:
        for s in p:
            if s not in [v for v in wire_dict.values()]:
                wire_dict['C'] = s

    decoding_dict = {k: v.lower() for v, k in wire_dict.items() if len(v) == 1}
    decoded_output_digits = []
    for index, digit_segments in enumerate(output):
        decoded_digit = ''
        for s in digit_segments: 
            decoded_digit += decoding_dict[s]
        decoded_output_digits.append(decoded_digit)

    decoded_output_int_list = []
    for d in decoded_output_digits:
        sorted_d = ''.join(sorted(d))
        match sorted_d:
            case 'abcefg':
                decoded_output_int_list.append(0)
            case 'cf':
                decoded_output_int_list.append(1)
            case 'acdeg':
                decoded_output_int_list.append(2)
            case 'acdfg':
                decoded_output_int_list.append(3)
            case 'bcdf':
                decoded_output_int_list.append(4)
            case 'abdfg':
                decoded_output_int_list.append(5)
            case 'abdefg':
                decoded_output_int_list.append(6)
            case 'acf':
                decoded_output_int_list.append(7)
            case 'abcdefg':
                decoded_output_int_list.append(8)
            case 'abcdfg':
                decoded_output_int_list.append(9)
    decoded_output_int = ''
    for i in decoded_output_int_list:
        decoded_output_int += str(i)
    decoded_output_int = int(decoded_output_int)
    sum += decoded_output_int
    print(f"display {display_nr+1:3} - wires: {sorted([(k, v) for k, v in wire_dict.items() if len(k) == 1])} decoded output: {decoded_output_int}")
print(f"sum_of_decoded_outputs: {sum}")