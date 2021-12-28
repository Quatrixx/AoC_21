def get_neighbor_coords(grid: list, c: tuple):
    neighbor_list = []
    x, y = c[0], c[1]
    if y > 0:
        neighbor_list.append((x, y-1))
    if x > 0:
        neighbor_list.append((x-1, y))
    if x < len(grid)-1:
        neighbor_list.append((x+1, y))
    if y < len(grid[x])-1:
        neighbor_list.append((x, y+1))
    return neighbor_list
    
def get_neighbor_heights(grid: list, c: tuple):
    neighbor_coords = get_neighbor_coords(grid, c)
    return [grid[x][y] for (x, y) in neighbor_coords]

def check_if_lowpoint(grid: list, c: tuple):
    x, y = c[0], c[1]
    neighbors = sorted(get_neighbor_heights(grid, (x, y)))
    return (grid[x][y] < neighbors[0])

def check_basin_size_recursively(input_map, output_map, c: tuple):
    neighbor_coords = get_neighbor_coords(input_map, c)
    x, y = c[0], c[1]
    output_map[x][y] = 1
    size = 1
    for (n_x, n_y) in neighbor_coords:
        if output_map[n_x][n_y] == 0:
            if input_map[n_x][n_y] == 9:
                output_map[n_x][n_y] = 9
            else:
                size += check_basin_size_recursively(input_map, output_map, (n_x, n_y))
    return size

with open('day9.in') as input:
    heightmap = [[int(c) for c in l.strip()] for l in input.readlines()]
low_point_list = []

# part one
risk_level_sum = 0
for x, row in enumerate(heightmap):
    for y, cell in enumerate(row):
        is_lowpoint = check_if_lowpoint(heightmap, (x, y))
        if is_lowpoint:
            low_point_list.append((x,y))
            risk_level_sum += 1 + cell
        # print(f"lp@({x:2},{y:2}): risk {1 + cell}")
print(f"part 1: global_risk_level= {risk_level_sum}")

# part two
basin_map = [[0 for c in row] for row in heightmap]
basin_list = []
for lp in low_point_list:
    basin_list.append(check_basin_size_recursively(heightmap, basin_map, lp))
biggest_basin_size_list = sorted(basin_list, reverse=True)[:3]
size_product = biggest_basin_size_list[0]
for b in biggest_basin_size_list[1:]:
    size_product *= b
print(f"part 2: biggest_basins= {biggest_basin_size_list}, product_of_sizes= {size_product}")