import sys
filename = sys.argv[1]

"""
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

indications = ""

def parse_node(line):
    origin, destinations = line.split('=')
    origin = origin[:-1]
    destinations = destinations[2:-1]
    left,right = destinations.split(',')
    right = right[1:]
    return (origin, (left, right))

def find_index_of_starting_nodes(network):
    indexes = []
    index=0
    for node in network:
        if node[0][len(node[0])-1] == "A":
            indexes.append(index)
        index+=1
    return indexes

def find_index_of(label,network):
    index=0
    for node in network:
        if node[0] == label:
            return index
        index+=1

def navigate(cur_index,steps,network, indications,end_node_label):
    index = cur_index
    indication = indications[steps%len(indications)]
    
    if indication == "L":
        current_node_label = network[index][1][0]
    else:
        current_node_label = network[index][1][1]
    index = find_index_of(current_node_label,network)
    #if current_node_label == end_node_label:
    if current_node_label[len(current_node_label)-1] == "Z":
        return index, True
    else:
        return index, False
    
network = []
line_count = 0
with open(filename) as f:
    for line in f:
        line = line.strip()
        if line_count == 0:
            indications = line
        elif len(line) > 0:
            node = parse_node(line)   
            network.append(node)
        line_count+=1    

start_indexes = find_index_of_starting_nodes(network)
cur_indexes = start_indexes.copy()
steps = 0
end_node_labels =  []
terminations = []
for i in range(0,len(cur_indexes)):
    end_node_labels.append(network[cur_indexes[i]][0].replace("A","Z"))
    #print(end_node_labels[i], network[cur_indexes[i]][0])
    terminations.append(False)

first_step_times = {}

while True:
    for i in range(0,len(cur_indexes)):
        if terminations[i]:
            continue
        cur_indexes[i],terminations[i] = navigate(cur_indexes[i],steps,network,indications,end_node_labels[i])
        if terminations[i]:
            first_step_times[network[start_indexes[i]][0]] = steps+1
    steps += 1
    if terminations.count(True) == len(terminations):
        break
#print(first_step_times)

values = list(first_step_times.values())
print("termination steps ",values)

# calcola minimo comune multiplo
from functools import reduce
from math import gcd
def mcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

print(mcm(values))
