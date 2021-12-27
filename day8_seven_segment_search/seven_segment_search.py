class Pattern:
    def __init__(self, par_string: str):
        self.string = par_string

    def __iter__(self):
        return iter(self.string)
    def __next__(self):
        return next(self.string)
    def __len__(self):
        return len(self.string)
    def __str__(self):
        return self.string
    def __reversed__(self):
        return reversed(self.string)

    def sub(self, pat_b: str):
        'Return a copy of the pattern with segments from pat_b removed'
        ret_pat = ''
        for s in self.string:
            if s not in pat_b:
                ret_pat += s
        return Pattern(ret_pat)
        
    def add(self, pat_b: str):
        'Return a copy of the pattern with segments from pat_b added'
        ret_pat = self.string
        for s in pat_b:
            if s not in ret_pat:
                ret_pat += s
        return Pattern(ret_pat)

class Display:
    def __init__(self, unique: list, output: list):
        self.unique_patterns = unique
        self.output_patterns = output
        self.idx = 0

    def first_of_len(self, target_len):
        for p in self.unique_patterns:
            if len(p) == target_len:
                return Pattern(p)

    def first_of_len_without(self, target_len, exclusion):
        for p in self.unique_patterns:
            if (len(p) == target_len) & (str(exclusion) not in p):
                return Pattern(p)

    def last_of_len_without(self, target_len, exclusion):
        for p in reversed(self.unique_patterns):
            if (len(p) == target_len) & (str(exclusion) not in p):
                return Pattern(p)

    def get_common_of_len(self, target_len):
        ret_pat = ''
        patterns_of_target_len = [s for s in self.unique_patterns if len(s) == target_len]
        for s in patterns_of_target_len[0]:
            is_common = True
            for p in patterns_of_target_len[1:]:
                if s not in p:
                    is_common = False
            if is_common:
                ret_pat += s
        return Pattern(ret_pat)

with open('day8.in') as input:
    split_lines = [line.strip().split(" | ") for line in input.readlines()]
    unique_patterns_list = sorted([Pattern(h[0].split(' ')) for h in split_lines], key=len)
    output_values_list = sorted([Pattern(h[1].split(' ')) for h in split_lines], key=len)
    displays = [Display(u, o) for u, o in zip(unique_patterns_list, output_values_list)]

# part one
unique_digit_count = 0
for display in displays:
    for digit_segments in display.output_patterns:
        match len(digit_segments):
            case 2 | 3 | 4 | 7:
                unique_digit_count += 1
            case _:
                pass
print(f"part 1: total_unique_digits= {unique_digit_count}")

# part two
print("part 2:")
sum = 0
for index, display in enumerate(displays):
    wire_dict = {}
    wire_dict['A'] = str(display.first_of_len(3).sub(display.first_of_len(2)))
    wire_dict['5c'] = str(display.get_common_of_len(5))
    wire_dict['B'] = str(display.first_of_len(4).sub(display.first_of_len(2)).sub(wire_dict['5c']))
    wire_dict['D'] = str(display.first_of_len(4).sub(display.first_of_len(2)).sub(wire_dict['B']))
    wire_dict['6c'] = str(display.get_common_of_len(6))
    wire_dict['F'] = str(Pattern(wire_dict['6c']).sub(wire_dict['5c']).sub(wire_dict['B']))
    wire_dict['5/f'] = str(display.first_of_len_without(5, wire_dict['F']))
    wire_dict['5&f'] = str(display.first_of_len_without(5, wire_dict['5/f']) \
        .add(display.last_of_len_without(5, wire_dict['5/f'])))
    wire_dict['E'] = str(display.first_of_len(7).sub(wire_dict['5&f']))
    wire_dict['G'] = str(display.first_of_len(7).sub(display.first_of_len(4)) \
        .sub(wire_dict['A']).sub(wire_dict['E']))
    for p in display.unique_patterns:
        for s in p:
            if s not in [v for v in wire_dict.values()]:
                wire_dict['C'] = s

    decoding_dict = {k: v.lower() for v, k in wire_dict.items() if len(v) == 1}
    decoded_output_digits = []
    for digit_segments in display.output_patterns:
        decoded_digit = ''
        for s in digit_segments: 
            decoded_digit += decoding_dict[s]
        decoded_output_digits.append(decoded_digit)

    decoded_output_int_list = []
    for display in decoded_output_digits:
        sorted_d = ''.join(sorted(display))
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
    print(f"display: {index+1:3}, "
        f"wires: {sorted([(k, v) for k, v in wire_dict.items() if len(k) == 1])}, "
        f"decoded output: {decoded_output_int}")
print(f"sum_of_decoded_outputs: {sum}")