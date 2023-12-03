def replace_overlaps_manual(input_string):
    # Sostituisci manualmente le combinazioni di overlap desiderate
    replacements = {
        "twone": "twoone",
        "eightwo": "eighttwo",
        "threeight": "threeeight",
        "fiveight": "fiveeight",
        "sevenine": "sevennine",
        "oneight": "oneeight"
        # Aggiungi altre combinazioni come necessario
    }

    for original, replacement in replacements.items():
        input_string = input_string.replace(original, replacement)

    return input_string

# Esempio di utilizzo
with open("input.txt", "r") as f, open("output.txt", "w") as output_file:
    for line in f:
        result = replace_overlaps_manual(line.strip())
        print("Original:", line.strip())
        print("Modified:", result)
        print()
        output_file.write(result + "\n")
