#Nicholas Larsen file Handling
from time_handling import  find_time
def read_file(filename):
    with open(filename, 'r') as file:
        length = len(file.read().split())
    with open(filename, 'a') as file:
        time = find_time()
        file.write(f'\n{length} words\nUpdated:{time}')
        return length