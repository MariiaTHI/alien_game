import random
import copy
from StrongAlien import StrongAlien
from WeakAlien import WeakAlien
from ComputerPlayer import ComputerPlayer
from HumanPlayer import  HumanPlayer
from Alien import Alien
class Game:
    """
    A random number of aliens is placed at the top row of a play field.
    In each game iteration, a player can shoot at a column.
    If an alien is hit, its armor gets reduced based on the alien type
    If no armor is left, the alien is dead at disappears from the play field
    In each game iteration, all aliens move one row downwards
    If an alien comes to the ground (not the last row, but beyond it), the aliens win!
    If all aliens are shot before reaching the ground, the humans win!
    """

    def __init__(self, rows=10, columns=7, nr_aliens=5, ratio=0.5, mode="computer"):
        # -----------------------------
        #            TEAM 3
        # -----------------------------
        """
        Initializes the member variables, Generates a player based on the mode
        Calls the init_sky and init_aliens methods to init a valid game
        :param rows: Nr. of rows in the play field
        :param columns: Nr. of columns in the play field
        :param nr_aliens: Nr. of aliens to add
        :param ratio: the ratio between weak and strong aliens
        :param mode: the play mode: "computer" for computer player, "human" for human player
        """
        self.rows = rows
        self.columns = columns
        self.nr_aliens = nr_aliens
        self.ratio = ratio
        self.mode = mode
        self.sky = []
        #init sky and aliens
        self.init_sky()
        self.init_aliens(nr_aliens, ratio)
        #init player
        self.player = self.init_player(mode)

    def show(self):
        """
        prints the game
        """
        for r in self.sky:
            print(*r)

    def init_sky(self):
        """
        Initialize the sky with empty fields
        """
        self.sky = [['_' for i in range(self.columns)] for j in range(self.rows)]

    @staticmethod
    def get_species(probability):
        # -----------------------------
        # TEAM 1
        # -----------------------------
        """
        Returns either a StrongAlien or a WeakAlien.
        Hint: Use random.random to create a random value between 0 and 1
        :param probability: The probability to create a WeakAlien
        :return: the generated alien
        """
        if random.random() <= probability:
            return WeakAlien()
        else:
            return StrongAlien()

    def init_aliens(self, nr_aliens, probability):
        # -----------------------------
        # TEAM 1
        # -----------------------------
        """
        Initializes the aliens and places them randomly at the top row of the play field
        :param nr_aliens: The number of aliens to be generated
        :param probability: The probability to create a WeakAlien
        """
        for i in range(nr_aliens):
            alien = self.get_species(probability)
            row = 0
            col = random.randint(0, self.columns - 1)
            self.sky[row][col] = alien

    def init_player(self, mode):
        if mode == "human":
            return HumanPlayer(self.columns)
        elif mode == "computer":
            return ComputerPlayer(self.columns)
        else:
            raise ValueError(f"Invalid game mode: {mode}")

    def aliens_remain(self):
        """
        Checks if some aliens remain at the sky
        :return: True if there are aliens left, False otherwise
        """
        for row in self.sky:
            for item in row:
                if isinstance(item, Alien):
                    return True
        return False

    def play(self):
        """
        This is implementing the main game loop
        """
        while True:
            # first check if aliens remain, if not, humans won
            if not self.aliens_remain():
                return "Humans won!"

            # show the play filed
            self.show()
            print("--------------")

            # Next, let the player shoot
            column = self.player.shoot()
            print(f"you shouted at column {column}")

            # create a deep copy of the sky to work with
            tmp = copy.deepcopy(self.sky)

            # loop through self.sky and check for every alien you find
            # check if the alien is hit
            for i in range(self.rows):
                if isinstance(tmp[i][column], Alien):
                    tmp[i][column].got_hit()
                    print("You hit an alien!")

                    # check if the alien is dead
                    if tmp[i][column].armor <= 0:
                        # remove the dead alien from the sky
                        tmp[i][column] = "_"
                        print('alien is dead')
                    else:
                        # update the armor of the hit alien
                        print('It was a strong Alien')

            # else move it one row downwards
            for i in range(self.rows, 0, -1):
                for j in range(self.columns):
                    if isinstance(tmp[i - 1][j], Alien):
                        tmp[i][j] = tmp[i - 1][j]
                        tmp[i - 1][j] = '_'

            # if the alien reached the ground, the aliens won
            for col in range(self.columns):
                if isinstance(tmp[len(self.sky) - 1][col], Alien):
                    print("Aliens won!")
                    return

            # set the tmp play filed back to the real one
            self.sky = tmp



if __name__ == '__main__':
    game = Game(mode='human')
    game.show()
    print()
    game.play()