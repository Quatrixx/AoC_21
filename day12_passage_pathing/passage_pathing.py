def check_paths_recursively(connection_dict: dict, prev_path_list: list, cave: str):
    found_paths = []
    connections = connection_dict[cave].copy()
    already_visited = prev_path_list.copy()
    already_visited.append(cave)
    if cave == 'end':
        found_paths.append(already_visited)
        connections = []
    else:
        for v in already_visited:
            if (v.islower()) & (v in connections):
                connections.remove(v)
    for con in connections:
        found_paths += [p for p in check_paths_recursively(connection_dict, already_visited, con)]
    return found_paths

def check_paths_recursively_with_exception(connection_dict: dict, prev_path_list: list, cave: str):
    found_paths = []
    connections = connection_dict[cave].copy()
    already_visited = prev_path_list.copy()
    already_visited.append(cave)
    if cave == 'end':
        found_paths.append(already_visited)
        connections = []
    else:
        no_more_exceptions = False
        for v in already_visited:
            if (v.islower()) & (already_visited.count(v) >= 2):
                no_more_exceptions = True
        for v in already_visited:
            if v in connections:
                if v == 'start':
                    connections.remove(v)
                elif (no_more_exceptions) & (v.islower()):
                    connections.remove(v)
    for con in connections:
        found_paths += [p for p in check_paths_recursively_with_exception(connection_dict, already_visited, con)]
    return found_paths

with open('day12.in') as input:
    split_lines = [line.strip().split('-') for line in sorted(input.readlines())]
cave_dict = {}
for (a, b) in split_lines:
    if a in cave_dict.keys():
        cave_dict[a].append(b)
    else:
        cave_dict[a] = [b]
    if b in cave_dict.keys():
        cave_dict[b].append(a)
    else:
        cave_dict[b] = [a]

valid_paths = check_paths_recursively(cave_dict, [], 'start')
print(f"part1: single_small_cave_paths= {len(valid_paths)}")

valid_paths = check_paths_recursively_with_exception(cave_dict, [], 'start')
print(f"part2: small_cave_exception_paths= {len(valid_paths)}")