import random

class Attacker:
    def __init__(self):
        print("You will be playing as an attacker. You will be generating random attackers.")
        self.roles = ["Ace", "Amaru", "Ash", "Blackbeard", "Blitz", "Brava", "Buck", "Capitao", "Deimos", "Dokkaebi", "Finka", "Flores", "Fuze", "Glaz", "Gridlock", "Grim", "Hibana", "Iana", "IQ", "Jackal", "Kali", "Lion", "Maverick", "Montagne", "Nomad", "Nokk", "Osa", "Ram", "Sens", "Sledge", "Striker", "Thatcher", "Thermite", "Twitch", "Ying", "Zero", "Zofia"]

    def randomize_operators(self, num_operators):
        if num_operators > len(self.roles):
            print("Error: You are trying to randomize more operators than are available.")
            return []
        random_operators = random.sample(self.roles, num_operators)
        return random_operators