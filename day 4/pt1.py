"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

def parse_card(card):
    header,body = card.split(":")
    body = body.strip()
    matching_numbers = body.split("|")[0].strip().replace("  "," ").split(" ")
    guesses = body.split("|")[1].strip().replace("  "," ").split(" ")
    return matching_numbers,guesses

def count_matches(k,array):
    count = 0
    for i in set(array): # remove duplicates
        if i == k:
            count += 1
    return count



total = 0
with open("input.txt") as f:
    cards = f.readlines()
    for card in cards:
        matching_numbers,guesses = parse_card(card)
        matches=0
        for i in set(guesses): # without duplicates
            if count_matches(i,matching_numbers) > 0:
                matches += 1
        if matches == 0:
            points = 0
        else:
            points = 2**(matches-1)
        print("points: ",points)
        total += points

print("total: ",total)