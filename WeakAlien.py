# -----------------------------
#            TEAM 1
# -----------------------------
from Alien import Alien
class WeakAlien(Alien):
    """
    A weak alien gets -2 on its armor when hit by a shot
    """
    def __str__(self):
        return f"WA{self.armor}"

    def got_hit(self):
        self.armor -=2
        if self.armor == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    alien = WeakAlien()
    print(alien.__str__())
    print(alien.got_hit())
    print(alien.__str__())