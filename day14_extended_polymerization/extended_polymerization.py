def get_elem_counts(elem_pairs, polymer_template):
    elements = {}
    for (a, b), amount in elem_pairs.items():
        if amount > 0:
            if a not in elements.keys():
                elements[a] = 0
            if b not in elements.keys():
                elements[b] = 0
            elements[a] += amount
            elements[b] += amount
    elements[polymer_template[0]] += 1
    elements[polymer_template[-1]] += 1
    for e, amount in elements.items():
        elements[e] = amount // 2
    elements = sorted(elements.items(), key=lambda e: e[1], reverse=True)
    return elements

def answer_calc(elem_pairs, polymer_template):
    elements = get_elem_counts(elem_pairs, polymer_template)
    return (elements[0][1]-elements[-1][1])

def do_polymerizsation(elem_pairs, pair_insert_rules):
    new_elem_pairs = {k: 0 for k, v in elem_pairs.items()}
    for (a, b), amount in elem_pairs.items():
        if amount > 0:
            c = pair_insert_rules[a+b]
            new_elem_pairs[a+c] += amount
            new_elem_pairs[c+b] += amount
    return new_elem_pairs

with open('day14.in') as input:
    polymer_template = input.readline().strip()
    input.readline()
    pair_insertion_rules = [ins.strip().split(' -> ') for ins in input.readlines()]
    pair_insertion_rules = {k: v for k, v in pair_insertion_rules}

element_pairs = {}
for pair in pair_insertion_rules.keys():
    element_pairs[pair] = 0
last_element = None
for e in polymer_template:
    if last_element != None:
        element_pairs[last_element+e] += 1
    last_element = e
    
for step in range(40):
    # elements = get_elem_counts(element_pairs, polymer_template)
    # elements = {k: v for k, v in elements}
    # print(elements)
    element_pairs = do_polymerizsation(element_pairs, pair_insertion_rules)
    if step+1 == 10:
        print(f"part1: {answer_calc(element_pairs, polymer_template)}")
    elif step+1 == 40:
        print(f"part2: {answer_calc(element_pairs, polymer_template)}")
