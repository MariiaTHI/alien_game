# -----------------------------
#            TEAM 1
# -----------------------------
from Alien import Alien

class StrongAlien(Alien):
    """
    A strong alien gets -1 on its armor when hit by a shot
    """
    def __str__(self):
        return f"SA{self.armor}"
    def got_hit(self):
        self.armor -= 1
        if self.armor <= 0:
            return True
        else:
            return False

if __name__ == '__main__':
    alien = StrongAlien()
    print(alien.__str__())
    print(alien.got_hit())
    print(alien.__str__())
    print(alien.got_hit())
    print(alien.__str__())