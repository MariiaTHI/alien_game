# -----------------------------
#            TEAM 1
# -----------------------------
class StrongAlien(Alien):
    """
    A strong alien gets -1 on its armor when hit by a shot
    """
    def got_hit(self):
        if self.armor <= 0:
            return True
        else:
            return False