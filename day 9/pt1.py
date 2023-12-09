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
    return sum(sequence) == 0

def predict_next_value(sequences):
    total_sum = 0
    for i in range(len(sequences)):
        total_sum += sequences[i][-1]
    return total_sum

def main():
    args = sys.argv
    if len(args) < 2:
        print("Please provide a filename")
        return

    filename = args[1]
    total = 0

    with open(filename, 'r') as file:
        for line in file:
            values = [int(s) for s in line.split()]
            
            sequence = values
            sequences = [sequence.copy()]
            for i in range(1, len(sequence)):
                sub_sequence = create_sub_sequence(sequences[i - 1])
                is_zero = is_zero_sequence(sub_sequence)
                if is_zero:
                    sequences.append(sub_sequence.copy())
                    break
                else:
                    sequences.append(sub_sequence.copy())

            prediction = predict_next_value(sequences)
            total += prediction

    print("Total:", total)

if __name__ == "__main__":
    main()
