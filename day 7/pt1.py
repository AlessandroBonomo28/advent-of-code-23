"""
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

def occourrences(array):
    occ = {}
    pairs = 0
    for i in set(array):
        o = array.count(i)
        occ[i] = o
        if o == 2:
            pairs += 1
    return occ,pairs

def get_max(array):
    max = 0
    for i in array:
        if i > max:
            max = i
    return max

def parse_match(match):
    hand, bid = match.split(" ")
    occourrences_hand,pairs = occourrences(hand)
    length = len(occourrences_hand) 
    if length == 5:
        power = 1 # high card
    elif length == 1:
        power = 6 # five of a kind
    else:
        if 4 in occourrences_hand.values():
            power = 5 # full house
        elif 3 in occourrences_hand.values():
            power = 4 # three of a kind
        elif pairs == 1:
            power = 2 #one pair
        elif pairs == 2:
            power = 3 #two pairs
    return hand,power,int(bid)
    
result = 0
hands = []
import sys
argv = sys.argv[1]
filename = argv
with open(filename) as f:
    for line in f:
        hand,power,bid = parse_match(line)
        #print("Hand: ",hand," Power: ",power," Bid: ",bid)
        hands.append((hand,power,bid))

card_value = {
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "T":10,
    "J":11,
    "Q":12,
    "K":13,
    "A":14
}
# cycle over hands and sort by power
"""for i in range(0,len(hands)):
    for j in range(i+1,len(hands)):
        if hands[i][1] < hands[j][1]:
            hands[i],hands[j] = hands[j],hands[i]
        elif hands[i][1] == hands[j][1]:
            # cycle over card
            for k in range(0,5):
                if hands[i][0][k] < hands[j][0][k]:
                    hands[i],hands[j] = hands[j],hands[i]
                    break
                elif hands[i][0][k] > hands[j][0][k]:
                    break
"""

# rewrite the above commented using the card_value dictionary
for i in range(0,len(hands)):
    for j in range(i+1,len(hands)):
        if hands[i][1] < hands[j][1]:
            hands[i],hands[j] = hands[j],hands[i]
        elif hands[i][1] == hands[j][1]:
            # cycle over card
            for k in range(0,5):
                if card_value[hands[i][0][k]] < card_value[hands[j][0][k]]:
                    hands[i],hands[j] = hands[j],hands[i]
                    break
                elif card_value[hands[i][0][k]] > card_value[hands[j][0][k]]:
                    break
                

max = len(hands)
count = 0
for hand in hands:
    result += hand[2]*(max-count)
    count+=1

print("Result: ",result)