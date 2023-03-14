# -----------------------------
#            TEAM 2
# -----------------------------
from abc import ABC, abstractmethod
class Player(ABC):
    """
    Abstract Player class
    """
    def __init__(self, cols):
        """
        Constructor
        :param cols: the available columns of the play field
        """
        self.cols = cols

    @abstractmethod
    def shoot(self):
        """
        Abstract method to shoot at a selected column
        :return: the column to shoot at
        """
        pass

if __name__ == '__main__':
    print('abstract class')