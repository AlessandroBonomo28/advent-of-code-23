import sys

def create_sub_sequence(main_seq):
    sub_sequence = []
    i = 1
    while i < len(main_seq):
        diff = main_seq[i] - main_seq[i - 1]
        sub_sequence.append(diff)
        i += 1
    return sub_sequence

def is_zero_sequence(sequence):
    for i in range(len(sequence)):
        if sequence[i] != 0:
            return False
    return True

def predict_next_value(sequences):
    sum = 0
    for i in range(len(sequences)):
        sum=sequences[i][0] -sum
    return sum



def main():
    args = sys.argv
    if len(args) < 2:
        print("Please provide a filename")
        return

    filename = args[1]
    total = 0

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            main_sequence = [int(x) for x in line.split(" ")]
            sequences = [main_sequence]
            i=1
            while True:
                sub_sequence = create_sub_sequence(sequences[i - 1])
                sequences.append(sub_sequence)
                if is_zero_sequence(sub_sequence):
                    break
                i += 1
            sequences.reverse()
            prediction = predict_next_value(sequences)
            total += prediction

    print("Total:", total)

if __name__ == "__main__":
    main()
