import random


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

        # init player
        if mode == "computer":
            self.player = ComputerPlayer(columns)
        else:
            self.player = HumanPlayer(columns)

        # init sky and aliens


    def show(self):
        """
        prints the game
        """
        for r in self.sky:
            print(r)

    def init_sky(self):
        """
        Initialize the sky with empty fields
        """
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append("_")
            self.sky.append(row)

    @staticmethod
    def get_species(probability):
        # -----------------------------
        #            TEAM 1
        # -----------------------------
        """
        Returns either a StrongAlien or a WeakAlien.
        Hint: Use random.random to create a random value between 0 and 1
        :param probability: The probability to create a WeakAlien
        :return: the generated alien
        """
        pass

    def init_aliens(self, nr_aliens, probability):
        # -----------------------------
        #            TEAM 1
        # -----------------------------
        """
        Initializes the aliens and places them randomly at the top row of the play field
        :param nr_aliens: The number of aliens to be generated
        :param probability: The probability to create a WeakAlien
        """
        pass

    def play(self):
        # -----------------------------
        #            TEAM 3
        # -----------------------------
        """
        This is implementing the main game loop
        """
        while True:
            # first check if aliens remain, if not, humans won

            # Next, let the player shoot

            # create a deep copy of the sky to work with


            # loop through self.sky and check for every alien you find
            #   is it hit by a shot
            #   elif it reached the ground, if so, the aliens won
            #   else move it one row downwards

            # set the tmp play filed back to the real one
            self.sky = tmp
            # show the play filed
            self.show()
            print("--------------")

    def aliens_remain(self):
        # -----------------------------
        #            TEAM 3
        # -----------------------------
        """
        Checks if some aliens remain at the sky
        :return: True if there are aliens left, False otherwise
        """
        pass


if __name__ == '__main__':
    game = Game()
    game.show()
    print()
    game.play()