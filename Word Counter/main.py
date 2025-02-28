#Nicholas Larsen, Word Counter

from file_handling import read_file
def main():
    while True:
        file = input('What is the directory of the file you would like the word count of?').strip()
        try:
            open(file, 'r')
        except:
            print("Please enter a valid directory use /, not \\.")
            continue
        length = read_file(file)
        print(f"Word count was {length}.\nWord count and timestamp have been added to the bottom of the file.")
main()