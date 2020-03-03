import string
import random
import os


FILENAME = 'tickets.txt'
NUM_TICKETS = 1_000

def generate_ticket():
    return ''.join(
            [
                random.choice(string.digits) 
                for _ in range(6)
            ]
        )

def main():
    with open(FILENAME, 'w') as file_result:
        for _ in range(NUM_TICKETS):
            file_result.write(generate_ticket()+'\n')

if __name__ == '__main__':
    main()
