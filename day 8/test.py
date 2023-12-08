
l = [11653, 12737, 14363, 15989, 18157, 21409]

small = 11653
big = 21409

def trova_moltiplicatori(n,a,b):
    moltiplicatori =[]
    big = max(a,b)
    small = min(a,b)
    big_multiplier = 1
    tries = n
    while True:
        small_multiplier = (big_multiplier*big)/small

        if small_multiplier.is_integer():
            #print(f" { small_multiplier } * {small} = {big_multiplier} * {big} = {big_multiplier*big}")
            #print("")
            moltiplicatori.append((small_multiplier,big_multiplier))
            tries -=1
            if tries == 0:
                break
        big_multiplier+=1 
    return moltiplicatori

"""big_multiplier = 1
for i in range(0,len(l)-1):
    m = trova_moltiplicatori(5,l[i],big)
    print(f"{l[i]} e {big} hanno come moltiplicatori:  {m}")"""



tmp = -1
small_mul = 1
prev_big_mul = None
i=0
while i < len(l)-1:
    big_mul = 1
    while True:
        if small_mul*79*l[i] == big_mul*21409:
            break
        big_mul +=1
    #print(big_mul)
    if prev_big_mul != None and big_mul != prev_big_mul:
        small_mul +=1
        i = 0
        #print("Retry with small_mul = ", small_mul)
    else:
        i+=1
    prev_big_mul = big_mul

print(f"small_mul = {small_mul} big_mul = {big_mul}")
    
