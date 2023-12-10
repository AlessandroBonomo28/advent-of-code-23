import sys
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
    start_symbol: [(0, -1), (0, 1), (-1, 0), (1, 0)]
}

lookup = {}


directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def dfs(map, pos, path = []):
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
                dfs(map, next_pos, path)
    return path

def start_dfs(map, pos):
    global lookup
    lookup[pos] = 'visited'
    return dfs(map, pos, [pos])

filename = sys.argv[1]
if filename is None:
    print("Please provide a filename")
    exit(1)

pipe_map = []

search_directions = {
    "S":(0, -1), # south
    "E":(1, 0),  # east
    "N":(0, 1),   # north
    "W":(-1, 0)  # west
}

def get_sybmol_at(pos):
    global pipe_map
    h = len(pipe_map)
    x,y = pos
    return pipe_map[h-y-1][x]

def vec_sum(pos, direction):
    x,y = pos
    dx,dy = direction
    return (x+dx, y+dy)

def is_compatible(current_symbol, next_symbol,direction):
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
    


start_pos = None
y = 0
with open(filename, 'r') as file:
    for line in file:
        line = line.strip()
        if start_symbol in line:
            x = line.index(start_symbol)
            start_pos = (x,y)
        pipe_map.append(line)
        y += 1
start_pos = (x,y-start_pos[1]-1)
print("Start pos: " + str(start_pos))

# genera n simboli a caso e vedi se sono compatibili, poi stampa

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


symbols = [vertical_pipe_symbol, horizontal_pipe_symbol, pipe_north_east_symbol, pipe_north_west_symbol, pipe_south_west_symbol, pipe_south_east_symbol, ground_symbol, start_symbol]
import random
n = 0
for i in range(n):
    a = random.choice(symbols)
    b = random.choice(symbols)
    random_direction = random.choice(list(search_directions.values()))
    print_compatibility(a,b,random_direction)


sys.setrecursionlimit(10000)

#start_pos = (1,3)
#s = get_sybmol_at((3,1))
path = start_dfs(pipe_map, start_pos)
print(path)
print(len(path))
