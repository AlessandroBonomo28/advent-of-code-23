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
    if current_node_label == end_node_label:
        return -1
    else:
        return index
    
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

starting_indexes = find_index_of_starting_nodes(network)
steps = 0
index = starting_indexes[0]
end_node_label = network[index][0].replace("A","Z")
while True:
    index = navigate(index,steps,network,indications,end_node_label)
    steps += 1
    if index == -1:
        break
print(steps)