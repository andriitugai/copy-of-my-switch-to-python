import math
import random

class SnakeLadders(object):

    field_size = 100

    def __init__(self, num_players=2):
        self.player_positions = [0] * num_players
        self.turn_pointer = 0
        self.portals = self.__class__._generate_portals()
        self.status = True

    @classmethod
    def _generate_portals(cls):
        '''Generate ladders and snakes for the game with size of field_size.
        Number of ladders and number of snakes has been choosen as sqrt(size)'''

        # snake heads, tales and ends of ladders cannot be the same
        num = int(math.sqrt(cls.field_size)) # number of snakes and number of ladders
        ends = random.sample(range(2, cls.field_size), 4*num) # you cannot throw 2 dices in sum less than 2

        snakes_lst = [(r1,r2) if r1>r2 else (r2,r1) for r1, r2 in zip(ends[:num], ends[num:2*num])]
        ladders_lst = [(r1,r2) if r1<r2 else (r2,r1) for r1, r2 in zip(ends[2*num:3*num], ends[3*num:])]

        portals = { k:v for k,v in snakes_lst+ladders_lst }
        return portals

    def play(self, dice1, dice2):

        if not self.status:
            print("Game over!")
            return

        new_pos = self.player_positions[self.turn_pointer] + dice1 + dice2
        size = self.__class__.field_size

        if new_pos == size:
            print(f'Player {self.turn_pointer+1} Wins!')
            self.status = False
            return
        elif new_pos > size:
            new_pos = 2*size - new_pos

        # Snakes and ladders business:
        if new_pos in self.portals:
            after_portal_pos = self.portals[new_pos]
            print("Ladder!" if after_portal_pos > new_pos else "Snake!")
            new_pos = after_portal_pos

        self.player_positions[self.turn_pointer] = new_pos

        print(f'Player {self.turn_pointer+1} is on square {new_pos}')
        if dice1 == dice2:
            print(f'Player {self.turn_pointer+1} moves again!')
        else:
            self.turn_pointer = (self.turn_pointer+1)% len(self.player_positions)
            print(f'Player {self.turn_pointer+1} moves.')

        return

def dice():
    return random.randint(1,6)

def main():

    game = SnakeLadders(5)
    while game.status:
        dices = dice(), dice()
        print(dices)
        game.play(*dices)

    game.play(6,3)


if __name__ == '__main__':
    main()

