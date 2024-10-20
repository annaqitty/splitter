def split_lines_to_files(input_filename, delimiter):
    part1 = []
    part2 = []

    # Read the content of the input file
    with open(input_filename, 'r') as file:
        for line in file:
            # Split each line by the specified delimiter
            parts = line.strip().split(delimiter)
            if len(parts) > 0:
                part1.append(parts[0].strip())  # First part
                if len(parts) > 1:
                    # If there's more than one part, modify the second part
                    part2.append(parts[1].strip() + " - end part detected")
                else:
                    part2.append("")  # If no second part, add an empty string

    # Write the first part to a file
    with open('part1.txt', 'w') as file1:
        for item in part1:
            file1.write(item + '\n')
    print('Created part1.txt')

    # Write the second part to a file
    with open('part2.txt', 'w') as file2:
        for item in part2:
            file2.write(item + '\n')
    print('Created part2.txt')

def main():
    input_filename = input("Enter the input filename: ")
    delimiter = input("Enter the delimiter to split by (e.g., ':'): ")
    split_lines_to_files(input_filename, delimiter)

if __name__ == "__main__":
    main()
