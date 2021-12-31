import time
import pygame

def get_neighbor_coords(grid: list, c: tuple):
    neighbor_list = []
    x, y = c[0], c[1]
    north = y > 0
    west = x > 0
    east = x < len(grid[y])-1
    south = y < len(grid)-1
    if north & west:
        neighbor_list.append((x-1, y-1))
    if north:
        neighbor_list.append((x, y-1))
    if north & east:
        neighbor_list.append((x+1, y-1))
    if west:
        neighbor_list.append((x-1, y))
    if east:
        neighbor_list.append((x+1, y))
    if south & west:
        neighbor_list.append((x-1, y+1))
    if south:
        neighbor_list.append((x, y+1))
    if south & east:
        neighbor_list.append((x+1, y+1))
    return neighbor_list

def flash_recursively(grid, exclusion_map, c: tuple):
    neighbor_coords = get_neighbor_coords(grid, c)
    x, y = c[0], c[1]
    exclusion_map[y][x] = 1
    tracked_flashes = 1
    for (n_x, n_y) in neighbor_coords:
        grid[n_y][n_x] += 1
        if (grid[n_y][n_x] > 9) & (exclusion_map[n_y][n_x] == 0):
            tracked_flashes += flash_recursively(grid, exclusion_map, (n_x, n_y))
    return tracked_flashes

def simulate_step(energy_grid):
    for y in range(len(energy_grid)):
        for x in range(len(energy_grid[y])):
            energy_grid[y][x] += 1
    step_flashmap = [[0 for c in row] for row in energy_grid]
    step_flashes = 0
    for y in range(len(energy_grid)):
        for x in range(len(energy_grid[y])):
            if (energy_grid[y][x] > 9) & (step_flashmap[y][x] == 0):
                step_flashes += flash_recursively(energy_grid, step_flashmap, (x, y))
    for y in range(len(step_flashmap)):
        for x in range(len(step_flashmap[y])):
            if step_flashmap[y][x] == 1:
                energy_grid[y][x] = 0
    return step_flashes

def draw_dumbos_as_squares():
    screen.fill((10, 10, 10))
    for y in range(len(energy_grid)):
        for x in range(len(energy_grid[y])):
            energy = energy_grid[y][x]
            dumbo_body = pygame.Rect(0+(dumbo_size*x), 0+(dumbo_size*y), dumbo_size, dumbo_size)
            dumbo_color = (0+(energy*28), 0, 252-(energy*28))
            pygame.draw.rect(screen, dumbo_color, dumbo_body)
    pygame.display.flip()

def draw_dumbos_as_circles():
    screen.fill((10, 10, 10))
    for y in range(len(energy_grid)):
        for x in range(len(energy_grid[y])):
            energy = energy_grid[y][x]
            #dumbo_body = pygame.Rect(0+(dumbo_size*x), 0+(dumbo_size*y), dumbo_size, dumbo_size)
            dumbo_body = 20
            dumbo_pos = (25+(dumbo_size*x), 25+(dumbo_size*y))
            dumbo_color = (0+(energy*28), 0, 252-(energy*28))
            pygame.draw.circle(screen, dumbo_color, dumbo_pos, dumbo_body)
    pygame.display.flip()

with open('day11.in') as input:
    energy_grid = [[int(c) for c in l.strip()] for l in input.readlines()]

square_dumbos = False

pygame.init()
dumbo_size = 50
screen = pygame.display.set_mode([dumbo_size*len(energy_grid[0]), dumbo_size*len(energy_grid)])
total_flashes = 0
sync = False
for step in range(1, 600):
    if square_dumbos:
        draw_dumbos_as_squares()
    else:
        draw_dumbos_as_circles()
    total_flashes += simulate_step(energy_grid)
    if step == 100:
        print(f"part1: total_flashes_after_100_steps= {total_flashes}")
    if (sync == False) & (energy_grid == [[0 for c in row] for row in energy_grid]):
        print(f"part2: synchronisation_after= {step} steps")
        sync = True
    stop = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
    if stop:
        break
    time.sleep(0.05)