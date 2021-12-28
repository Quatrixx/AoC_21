class LineCorruptionError(Exception):
    def __init__(self, expected_delim, actual_delim):
        self.expected_delim = expected_delim
        self.actual_delim = actual_delim

corresponding_delim_dict = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

syntax_score_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

completion_score_dict = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

with open('day10.in') as input:
    lines = [l.strip() for l in input.readlines()]

# part one
corrupted_line_indices, incomplete_line_stacks = [], []
syntax_error_score = 0
for line_index, line in enumerate(lines):
    try:
        chunk_stack = []
        for c in line:
            match c:
                case '(' | '[' | '{' | '<':
                    chunk_stack.append(c)
                case ')' | ']' | '}' | '>':
                    expected_delim = corresponding_delim_dict[chunk_stack.pop()]
                    if c != expected_delim:
                        raise LineCorruptionError(expected_delim, c)
        incomplete_line_stacks.append(chunk_stack)
    except LineCorruptionError as err:
        corrupted_line_indices.append(line_index)
        syntax_error_score += syntax_score_dict[err.actual_delim]
print(f"part1: syntax_error_score= {syntax_error_score}")

# part two
for already_deleted, line_index in enumerate(corrupted_line_indices):
    del(lines[line_index-already_deleted])
completion_scores = []
for chunk_stack in incomplete_line_stacks:
    completion_score = 0
    for delim in reversed(chunk_stack):
        completion_score = completion_score * 5 + completion_score_dict[corresponding_delim_dict[delim]]
    completion_scores.append(completion_score)
completion_scores.sort()
print(f"part2: middle_completion_score= {completion_scores[len(completion_scores) // 2]}")