import sys
from colorama import Fore, Style
import random
"""

| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
Based on the acoustics of the animal's scurrying, you're confiden
"""

vertical_pipe_symbol = '|'
horizontal_pipe_symbol = '-'
pipe_north_east_symbol = 'L'
pipe_north_west_symbol = 'J'
pipe_south_west_symbol = '7'
pipe_south_east_symbol = 'F'
ground_symbol = '.'
start_symbol = 'S'

compatibility = {
    vertical_pipe_symbol: [(0, -1), (0, 1)],
    horizontal_pipe_symbol: [(-1, 0), (1, 0)],
    pipe_north_east_symbol: [(0, 1), (1, 0)],
    pipe_north_west_symbol: [(0, 1), (-1, 0)],
    pipe_south_west_symbol: [(0, -1), (-1, 0)],
    pipe_south_east_symbol: [(0, -1), (1, 0)],
    ground_symbol: [],
    start_symbol: [(0, -1), (0, 1), (-1, 0), (1, 0)],
    "X":[]
}

lookup = {}


directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def dfs(pos, path = []):
    #print(f"dfs({get_sybmol_at(pos)})")
    global lookup
    for dir in directions:
        allowed = is_allowed_to_move(pos, dir)
        #print(f" allow to move {dir} from {pos}: {allowed}")
        if allowed:
            next_pos = vec_sum(pos, dir)
            status = lookup.get(next_pos, 'new')
            if status == 'visited' or status == 'seen':
                continue
            else:
                lookup[next_pos] = 'visited'
                #print(f"visited {get_sybmol_at(next_pos)}")
                path.append(next_pos)
                dfs(next_pos, path)
    return path

def dfs_iterative(pos):
    global lookup
    stack = [pos]
    path = [pos]
    while len(stack) > 0:
        pos = stack.pop()
        for dir in directions:
            allowed = is_allowed_to_move(pos, dir)
            if allowed:
                next_pos = vec_sum(pos, dir)
                status = lookup.get(next_pos, 'new')
                if status == 'visited' or status == 'seen':
                    continue
                else:
                    lookup[next_pos] = 'visited'
                    stack.append(next_pos)
                    path.append(next_pos)
    return path

def start_dfs(pos, iterative=True):
    global lookup
    lookup = {}
    lookup[pos] = 'visited'
    if not iterative:
        sys.setrecursionlimit(10000)
        return dfs(pos)
    else:
        return dfs_iterative(pos)

filename = sys.argv[1]
if filename is None:
    print("Please provide a filename")
    exit(1)

pipe_map = []


def get_sybmol_at(pos):
    global pipe_map
    h = len(pipe_map)
    x,y = pos
    y = h-y-1
    if y >= h or y < 0:
        return 'X'
    if x >= len(pipe_map[0]) or x < 0:
        return 'X'
    return pipe_map[y][x]

def vec_sum(pos, direction):
    x,y = pos
    dx,dy = direction
    return (x+dx, y+dy)

def is_compatible(current_symbol, next_symbol,direction):
    global compatibility
    opposite_direction = (-direction[0], -direction[1])
    if direction in compatibility[current_symbol] and opposite_direction in compatibility[next_symbol]:
        return True
    return False

def is_allowed_to_move(your_pos, direction):
    global pipe_map
    next_pos = vec_sum(your_pos, direction)
    your_symbol = get_sybmol_at(your_pos)
    next_pos_symbol = get_sybmol_at(next_pos)
    return is_compatible(your_symbol, next_pos_symbol,direction)
    



def print_compatibility(a,b,direction):
    """
    . b .
    . a .
    . . .
    print based on direction
    """
    compatibility = is_compatible(a,b,direction)
    word = {
        (0,1):"under",
        (0,-1):"above",
        (-1,0):"and on the left",
        (1,0):"and on the right"
    }
    print(f"Compatibility between '{a}' {word[direction]} '{b}': {compatibility}")
    if direction == (0,1):
        print(".  " + str(b) + "  .")
        print(".  " + str(a) + "  .")
        print(".  .  .")
    elif direction == (0,-1):
        print(".  .  .")
        print(".  " + str(a) + "  .")
        print(".  " + str(b) + "  .")
    elif direction == (-1,0):
        print(".  .  .")
        print(str(b)+"  " + str(a) + "  .")
        print(".  .  .")
    elif direction == (1,0):
        print(".  .  .")
        print(".  " + str(a) + "  " + str(b))
        print(".  .  .")
    print("")



def draw_path(path,pipe_map):
    h = len(pipe_map)
    x = 0
    y = 0
    for line in pipe_map:
        x=0
        for c in line:
            if c == start_symbol and (x,h-y-1) in path:
                print(Fore.YELLOW + c + Style.RESET_ALL,end="")
            elif (x,h-y-1) in path:
                print(Fore.GREEN + c + Style.RESET_ALL,end="")
            elif c == ground_symbol:
                print(Fore.BLUE + c + Style.RESET_ALL,end="")
            else:
                print(Fore.RED + c + Style.RESET_ALL,end="")
            x += 1
        print("")
        y+=1

def count_dots_in_path(path,map):
    total_dots = 0
    h = len(map)
    x = 0
    y = 0
    for line in map:
        x=0
        for c in line:
            if c == ground_symbol and (x,h-y-1) in path:
                total_dots += 1
            x += 1
        y+=1
    return total_dots

symbols = [vertical_pipe_symbol, horizontal_pipe_symbol, pipe_north_east_symbol, pipe_north_west_symbol, pipe_south_west_symbol, pipe_south_east_symbol, ground_symbol, start_symbol]

n = 0
for i in range(n):
    a = random.choice(symbols)
    b = random.choice(symbols)
    random_direction = random.choice(directions)
    print_compatibility(a,b,random_direction)

total_dots = 0

start_pos = None
y = 0
with open(filename, 'r') as file:
    for line in file:
        line = line.strip()
        total_dots += line.count(ground_symbol)
        if start_symbol in line:
            x = line.index(start_symbol)
            start_pos = (x,y)
        pipe_map.append(line)
        y += 1
start_pos = (x,y-start_pos[1]-1)
print("Start pos: " + str(start_pos))

path = start_dfs(start_pos)

silent = True if len(sys.argv) > 2 and sys.argv[2] == 'silent' else False


h = len(pipe_map)
w = len(pipe_map[0])


if not silent:
    draw_path(path,pipe_map)

out_path = []



compatibility[ground_symbol]= directions


for i in range(2):
    if i == 0:
        y = 0
    else:
        y = h-1
    for x in range(w):
        if (x,y) not in out_path and (x,y) not in path:
            out_path += start_dfs((x,y))
    if i == 0:
        x = 0
    else:
        x = w-1
    for y in range(h):
        if (x,y) not in out_path and (x,y) not in path:
            out_path += start_dfs((x,y))
            
out_path = list(set(out_path) - set(path))


if not silent:
    print("")
    print("Outside path:")
    draw_path(out_path,pipe_map)
outside_dots = count_dots_in_path(out_path,pipe_map)
trapped_dots = total_dots - outside_dots
print(Fore.RED + 'Day 10 AoC - DFS Flood Fill' + Style.RESET_ALL)
print(Fore.YELLOW +f"Farthest position: {len(path)//2}"+ Style.RESET_ALL)
print(Fore.BLUE +f"Trapped dots: {trapped_dots}" + Style.RESET_ALL)
print(Fore.GREEN +f"Outside dots: {outside_dots}" + Style.RESET_ALL)