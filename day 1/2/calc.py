word_to_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
sum=0
with open('output.txt', 'r') as file:
    for input_line in file:
        numbers = []
        i = 0
        word_did_match=False
        while i < len(input_line):
            if input_line[i].isdigit():
                numbers.append(int(input_line[i]))
                i += 1
            else:
                matched_word = None
                for word, digit in word_to_digit.items():
                    if input_line[i:i+len(word)] == word:
                        matched_word = word
                        word_did_match=True
                        break
                
                if matched_word is not None:
                    numbers.append(word_to_digit[matched_word])
                    i += len(matched_word)
                else:
                    i += 1

        print(numbers)
        sum+=numbers[0]*10
        sum+=numbers[-1]

print(sum)
