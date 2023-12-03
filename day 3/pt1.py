symbols = ["$", "#", "*", "+","%","@","=","-","&","/"]

visited = {}

lines = []
line_count=0

def get_prev_line(current_line):
    if current_line == 0:
        return None
    else:
        return lines[current_line - 1]

def get_next_line(current_line):
    if current_line == len(lines) - 1:
        return None
    else:
        return lines[current_line + 1]


def extract_number(index_char,line,line_count):
    global visited
    min_index = index_char
    if index_char >= len(line):
        return None
    if not line[index_char].isdigit():
        return None

    number=""
    for i in range(index_char,len(line)):
        if line[i].isdigit():
            min_index = min(min_index,i)
            number+=line[i]
        else:
            break

    # reverse for
    for i in range(index_char-1,-1,-1):
        if line[i].isdigit():
            min_index = min(min_index,i)
            number=line[i]+number
        else:
            break
    if number=="":
        return None
    if (line_count,min_index) in visited:
        return None
    visited[(line_count,min_index)] = 1
    return int(number)

with open('input.txt', 'r') as file:
    for line in file:
        lines.append(line.strip())


#num = extract_number(3,".467..114..")
#print("num: " + str(num))

def get_adjacent_numbers(current_line,symbol_index):
    global lines
    
    prev_line = get_prev_line(current_line)
    next_line = get_next_line(current_line)

    # left and right check
    left_number = extract_number(symbol_index-1,lines[current_line],current_line)
    right_number = extract_number(symbol_index+1,lines[current_line],current_line)


    # top right and top left check
    top_left_number=None
    top_right_number=None
    top_number=None
    if prev_line is not None:
        top_left_number = extract_number(symbol_index-1,prev_line,current_line-1)
        top_right_number = extract_number(symbol_index+1,prev_line,current_line-1)
        top_number = extract_number(symbol_index,prev_line,current_line-1)

    # bottom right and bottom left check
    bottom_number=None
    bottom_left_number=None
    bottom_right_number=None

    if next_line is not None:
        bottom_left_number = extract_number(symbol_index-1,next_line,current_line+1)
        bottom_right_number = extract_number(symbol_index+1,next_line,current_line+1)
        bottom_number = extract_number(symbol_index,next_line,current_line+1)

    #print("left_number: " + str(left_number))
    #print("right_number: " + str(right_number))
    #print("top_left_number: " + str(top_left_number))
    #print("top_right_number: " + str(top_right_number))
    #print("bottom_left_number: " + str(bottom_left_number))
    #print("bottom_right_number: " + str(bottom_right_number))
    numbers = [left_number,right_number,top_left_number,top_right_number,top_number,bottom_number,bottom_left_number,bottom_right_number]
    return numbers

#get_adjacent_numbers(len(lines)-2,3)


sum_adj = 0
for line in lines:
    index = 0
    for char in line:
        if char in symbols:
            adjacent_numbers = get_adjacent_numbers(line_count,index)
            for number in adjacent_numbers:
                if number is not None:
                    sum_adj+=number
        index += 1
    line_count+=1


#print(visited)

from colorama import Fore, Style


line_count=0

for line in lines:
    index = 0
    for char in line:
        if (line_count,index) in visited:
            print(Fore.RED + char + Style.RESET_ALL,end="")
        else:
            print(char,end="")
        index+=1

    print("")
    line_count+=1

print("sum of adjactent numbers is",sum_adj)
