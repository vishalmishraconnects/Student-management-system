# word_count.py

def count_words(input_file, output_file):
    """Count the number of words in a text file and write the count to a new file"""
    try:
        with open(input_file, 'r') as f:
            text = f.read()
            words = text.split()
            word_count = len(words)
            print(f"Word count: {word_count}")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return

    try:
        with open(output_file, 'w') as f:
            f.write(f"Word count: {word_count}\n")
            print(f"Word count written to '{output_file}'")
    except IOError:
        print(f"Error: Unable to write to file '{output_file}'")

def main():
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")
    count_words(input_file, output_file)

if __name__ == '__main__':
    main()
