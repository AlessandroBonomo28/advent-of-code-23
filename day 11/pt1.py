import sys
from colorama import Fore, Style
filename = sys.argv[1]
if filename is None:
    print("Please provide a filename")
    exit(1)


def print_galaxy(map, galaxies_pos, expansion_h=[], expansion_v=[]):
    h = len(map)
    for y in range(len(map)-1, -1, -1):
        print(f"{(h-y-1):03d} ", end='')
        for x in range(len(map[y])):
            dot_color = Fore.BLUE if x in expansion_v or y in expansion_h else Fore.WHITE
            if dot_color == Fore.WHITE:
                symbol = "."
            elif x in expansion_v and y in expansion_h:
                symbol = "+"
            elif x in expansion_v:
                symbol = "|"
            elif y in expansion_h:
                symbol = "-"
            else:
                symbol = "?"
            
            if (x,h-y-1) in galaxies_pos:
                indexof = galaxies_pos.index((x,h-y-1))+1
                print(Fore.YELLOW + "#" + Style.RESET_ALL, end='')
            else:
                print(dot_color+symbol+ Style.RESET_ALL, end='')
        print()


galaxy_map = []

horizontal_expansion_index_lines = []

h = 0
with open(filename) as f:
    for line in f:
        line = line.strip()
        galaxy_map.append(line)
        if line.count('#') == 0:
            horizontal_expansion_index_lines.append(h)

        h += 1

horizontal_expansion_index_lines = list(map(lambda y: h-y-1, horizontal_expansion_index_lines))
print(f"Horizontal lines index to expand: {horizontal_expansion_index_lines}")

vertical_expansion_index_lines = []
for x in range(len(galaxy_map[0])):
    count = 0
    for y in range(h):
        if galaxy_map[y][x] == '#':
            count += 1
    if count == 0:
        vertical_expansion_index_lines.append(x)

print(f"Vertical lines index to expand: {vertical_expansion_index_lines}")

galaxies_pos = []
y = 0

for line in galaxy_map:
    x = 0
    for c in line:
        if c == '#':
            galaxies_pos.append((x,y))
        x += 1
    y +=1


print_galaxy(galaxy_map,galaxies_pos, horizontal_expansion_index_lines, vertical_expansion_index_lines)
import math

def count_empty_galaxy_between(pos_a,pos_b,h_exp,v_exp):
    x1 = min(pos_a[0],pos_b[0])
    x2 = max(pos_a[0],pos_b[0])
    y1 = min(pos_a[1],pos_b[1])
    y2 = max(pos_a[1],pos_b[1])
    count_h = 0
    for horiz_line_index in h_exp:
        if horiz_line_index > x1 and horiz_line_index < x2:
            count_h += 1
    count_v = 0
    for vert_line_index in v_exp:
        if vert_line_index > y1 and vert_line_index < y2:
            count_v += 1
    return count_h ,count_v

sum =0
dist =0
count = 0


def distance_stepped(x1, y1, x2, y2):
    # Calcola la distanza a gradini tra due punti
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    # Restituisci la somma delle distanze orizzontali e verticali
    return dx + dy

for i in range(0,len(galaxies_pos)-1):
    for j in range(i+1,len(galaxies_pos)):
        x1,y1 = galaxies_pos[i]
        x2,y2 = galaxies_pos[j]
        empty_h,empty_v = count_empty_galaxy_between(galaxies_pos[i],galaxies_pos[j],
                        horizontal_expansion_index_lines,vertical_expansion_index_lines)
        #math.sqrt((x1-x2)**2 + (y1-y2)**2)
       
        """if x1 > x2:
            x1 -= empty_h
        else:
            x2 -= empty_h

        if y1 > y2:
            y1 -= empty_v
        else:
            y2 -= empty_v"""
        dist = distance_stepped(x1,y1,x2,y2) - empty_h - empty_v
        
        contribute = distance_stepped(0,0,2*empty_h,2*empty_v)
        #print(f" dist {dist} and contribute {contribute}")
        dist += contribute
        
        sum+=dist
        #print(f"Dist between {galaxies_pos[i]} and {galaxies_pos[j]} is {dist}, empty galaxies between: h {empty_h}, v {empty_v}")

        count += 1

print(f"Pairs: {count}")
print(f"Total: {sum}")