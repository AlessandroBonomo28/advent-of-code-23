"""
Time:      7  15   30
Distance:  9  40  200
"""
import time
def parse_line(line):
    header,body = line.split(':')
    header = header.strip()
    body = body.strip()
    numbers = []
    num = ""
    reading=False
    count=0
    for c in body:
        if c.isdigit():
            reading=True
            num += c
        elif reading:
            numbers.append(int(num))
            num=""
            reading=False
        if count==len(body)-1 and reading:
            numbers.append(int(num))
        count+=1
    return numbers


times = []
distances = []
with open("input.txt") as f:
    index = 0
    for line in f:
        parsed = parse_line(line)
        if index == 0:
            times = parsed
        else:
            distances = parsed
        index+=1

#print("Times: ", times)
#print("Distances: ", distances)
start = time.time()
mul = 1
for i in range(len(times)):
    print("Time: ", times[i], "Distance: ", distances[i])
    ways = 0
    for hold in range(1,times[i]):
        v = hold
        #print("Hold: ", hold, "Velocity: ", v)
        t = times[i]-hold
        s = v*t
        if s > distances[i]:
            ways += 1
            #print("Hold: ", hold, "Velocity: ", v, "Time: ", t, "Distance: ", s)
    #print("Ways: ", ways)
    mul *= ways
print(mul)

execution_time = time.time() - start
# format hms
execution_time = time.strftime("%H:%M:%S", time.gmtime(execution_time))
print("Time: ", execution_time)