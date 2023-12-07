"""
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

def occourences_and_pairs(array):
    occ = {}
    pairs = 0
    for i in set(array):
        o = array.count(i)
        occ[i] = o
        if o == 2:
            pairs += 1
    return occ,pairs


def calculate_power_with_jollys(power,jollys):
    if jollys ==0:
        return power
    if power == 1:
        return calculate_power_with_jollys(2,jollys-1)
    elif power == 2:
        return calculate_power_with_jollys(4,jollys-1)
    elif power == 3:
        return calculate_power_with_jollys(5,jollys-1)
    elif power == 4:
        return calculate_power_with_jollys(6,jollys-1)
    elif power == 5:
        return calculate_power_with_jollys(6,jollys-1)
    elif power == 6:
        return calculate_power_with_jollys(7,jollys-1)
    else:
        return 7

def parse_match(match):
    hand, bid = match.split(" ")
    jollys = hand.count("J")
    hand_without_jolly = hand.replace("J","")
    occourrences_hand,pairs = occourences_and_pairs(hand_without_jolly)

    length = len(occourrences_hand) 
    if length == len(hand_without_jolly):
        power = 1 # high card
    elif length == 1 and jollys == 0:
        power = 7 # five of a kind
    elif jollys == 5:
        power = 7 # five of a kind
    else:
        if 4 in occourrences_hand.values():
            power = 6 # four of a kind
        elif 3 in occourrences_hand.values() and pairs == 1:
            power = 5 # full house
        elif 3 in occourrences_hand.values():
            power = 4 # three of a kind
        elif pairs == 1:
            power = 2 #one pair
        elif pairs == 2:
            power = 3 #two pairs
    power = calculate_power_with_jollys(power,jollys)
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
    "J":0,
    "Q":12,
    "K":13,
    "A":14
}


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