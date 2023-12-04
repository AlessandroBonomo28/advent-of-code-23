"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

instances = {}

def parse_card(card):
    global instances
    header,body = card.split(":")
    id = int(header[header.find(" ")+1:])
    body = body.strip()
    matching_numbers = body.split("|")[0].strip().replace("  "," ").split(" ")
    guesses = body.split("|")[1].strip().replace("  "," ").split(" ")
    return matching_numbers,guesses,id

def count_matches(k,array):
    count = 0
    for i in set(array): # remove duplicates
        if i == k:
            count += 1
    return count



sum_points = 0
with open("input.txt") as f:
    cards = f.readlines()
    for card in cards:
        matching_numbers, guesses, id = parse_card(card)

        if str(id) not in instances:
            instances[str(id)] = 1

        matches=0
        for i in set(guesses): # without duplicates
            if count_matches(i,matching_numbers) > 0:
                matches += 1
        
        if matches == 0:
            points = 0
        else:
            points = 2**(matches-1)
            for i in range(0,matches):
                #print("id: ",id," i: ",id+1+i)
                if str(id+1+i) not in instances:
                    instances[str(id+1+i)] = 1
                instances[str(id+1+i)] = instances[str(id)] +instances[str(id+1+i)]
            #print(instances)
            #print("")

        #print("points: ",points)
        sum_points += points

sum_instances = 0
print("total: ",sum_points)
for k,v in instances.items():    
    sum_instances += v
    #print(k,v)
print("sum_instances: ",sum_instances)