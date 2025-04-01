#Nicholas Larsen, Word Counter

from Word_Counter.file_handling import read_file
def counter_main():
    while True:
        file = input('What is the directory of the file you would like the word count of? Enter "e" to exit.\n').strip()
        if file.lower() == 'e':
            return
        try:
            open(file, 'r')
        except:
            print("Please enter a valid directory. Make sure to use /, not \\.")
            continue
        length = read_file(file)
        print(f"Word count was {length}.\nWord count and timestamp have been added to the bottom of the file.")