import random

class Defender:
    def __init__(self):
        print("You will be playing as a defender. You will be generating random defenders.")
        self.roles = ["Alibi", "Aruni", "Azami", "Bandit", "Castle", "Caveira", "Clash", "Doc", "Echo", "Ela", "Fenrir", "Frost", "Goyo", "Jager", "Kaid", "Kapkan", "Lesion", "Maestro", "Melusi", "Mira", "Mozzie", "Mute", "Oryx", "Pulse", "Sentry", "Rook", "Skopos", "Smoke", "Solis", "Tachanka", "Thorn", "Thunderbird", "Tubarao", "Valkyrie", "Vigil", "Wamai", "Warden"]

    def randomize_operators(self, num_operators):
        if num_operators > len(self.roles):
            print("Error: You are trying to randomize more operators than are available.")
            return []
        random_operators = random.sample(self.roles, num_operators)
        return random_operators