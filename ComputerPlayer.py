# -----------------------------
#            TEAM 2
# -----------------------------
import random
import Player

class ComputerPlayer(Player):
    """
    A player that is steered automatically by the computer
    """

    def __init__(self, cols):
        """
        Constructor which is initializing a memory
        The memory remembers how often the player already shot at each column
        :param cols:
        """
        # Init memory and set 0 for all columns
        super().__init__(cols)
        self.memory = [0] * cols

    def shoot(self):
        """
        Shoots smartly at a specific column
        :return:
        """

        # smartly select a column where it was not already shot 2 times at before
        valid_cols = [i for i in range(len(self.memory)) if self.memory[i] < 2]
        col = random.choice(valid_cols)
        # remember that it was shot at this column one more time in the memory
        self.memory[col] += 1
        # return the value
        return col


