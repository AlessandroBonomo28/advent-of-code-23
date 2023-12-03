MAX_RED_CUBES= 12
MAX_BLUE_CUBES= 14
MAX_GREEN_CUBES= 13

"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

def parse_game(game : str):
    id = int(game[game.find(" ")+1:game.find(":")])
    header = game[game.find(":")+2:].strip()
    matches = header.split(";")
    impossible = False
    max_red = 0
    max_blue = 0
    max_green = 0
    for match in matches:
        match = match.strip()
        cubes = match.split(",")
        for cube in cubes:
            cube = cube.strip()
            color = cube.split(" ")[1]
            count = int(cube.split(" ")[0])
            if color == "red":
                if count > MAX_RED_CUBES:
                    impossible = True
                if count > max_red:
                    max_red = count
            elif color == "blue":
                if count > MAX_BLUE_CUBES:
                    impossible = True
                if count > max_blue:
                    max_blue = count
            elif color == "green":
                if count > MAX_GREEN_CUBES:
                    impossible = True
                if count > max_green:
                    max_green = count
            else:
                print("Unknown color: " + color)
    power = max_red * max_blue * max_green
    return impossible,id,power

id_sum = 0
power_sum = 0
with open('input.txt', 'r') as file:
    for line in file:
        impossible, id, power = parse_game(line)
        if impossible:
            print("Game " + str(id) + " is impossible")
        else:
            print("Game " + str(id) + " is possible")
            id_sum += id
        print("Game " + str(id) + " has power " + str(power))
        power_sum += power

print("sum of IDs is",id_sum)
print("sum of powers is",power_sum)