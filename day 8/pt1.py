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

def find_index_of(label,network):
    index=0
    for node in network:
        if node[0] == label:
            return index
        index+=1

def navigate(network, indications):
    steps = 0
    index = find_index_of("AAA",network)
    while True:
        indication = indications[steps%len(indications)]
        
        if indication == "L":
            current_node = network[index][1][0]
        else:
            current_node = network[index][1][1]
        index = find_index_of(current_node,network)
        steps += 1
        if current_node == "ZZZ":
            break
    return steps
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

from plot import plot_nicely, plot_default

#plot_nicely(network)
print(navigate(network, indications))