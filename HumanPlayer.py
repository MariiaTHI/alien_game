# -----------------------------
#            TEAM 2
# -----------------------------
from abc import ABC, abstractmethod
from Player import Player
class HumanPlayer(Player):
    """
    A player that is steered by user inputs
    """
    def __init__(self, cols):
        super().__init__(cols)

    def shoot(self):
        """
        Asks the player to shoot at a specific column
        :return:
        """
        while True:
            col = input(f"Please select a column to shoot at (0-{self.cols-1}): ")
            try:
                col = int(col)
                if col < 0 or col >= self.cols:
                    print(f"Column {col} is not valid. Please try again.")
                    continue
                return col
            except ValueError:
                print(f"Input '{col}' is not a valid number. Please try again.")
                continue

if __name__ == '__main__':
    human = HumanPlayer(6)
    print(human.shoot())