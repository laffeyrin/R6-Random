'''
import random

print("Welcome to R6 Randomizor")
print("Are you playing on Defender or Attacker?")

side = input("Enter 'Defender' or 'Attacker': ")

while side.capitalize() not in ['Defender', 'Attacker']:
    print("Invalid input. Please enter 'Defender' or 'Attacker'.")
    side = input("Enter 'Defender' or 'Attacker': ")

print(f"You are playing on {side.capitalize()}.")

if side.capitalize() == 'Defender':
    print("You will be playing as a defender. You will be generating random defenders.")
else:
    print("You will be playing as an attacker. You will be generating random attackers.")

num_operators = int(input("Enter the number of operators you want to randomize: "))

defender_roles = ["Alibi", "Aruni", "Azami", "Bandit", "Castle", "Caveira", "Clash", "Doc", "Echo", "Ela", "Fenrir", "Frost", "Goyo", "Jager", "Kaid", "Kapkan", "Lesion", "Maestro", "Melusi", "Mira", "Mozzie", "Mute", "Oryx", "Pulse", "Sentry", "Rook", "Skopos", "Smoke", "Solis", "Tachanka", "Thorn", "Thunderbird", "Tubarao", "Valkyrie", "Vigil", "Wamai", "Warden"]
attacker_roles = ["Ace", "Amaru", "Ash", "Blackbeard", "Blitz", "Brava", "Buck", "Capitao", "Deimos", "Dokkaebi", "Finka", "Flores", "Fuze", "Glaz", "Gridlock", "Grim", "Hibana", "Iana", "IQ", "Jackal", "Kali", "Lion", "Maverick", "Montagne", "Nomad", "Nokk", "Osa", "Ram", "Sens", "Sledge", "Striker", "Thatcher", "Thermite", "Twitch", "Ying", "Zero", "Zofia"]

def randomize_operators(num_operators, roles):
    if num_operators > len(roles):
        print("Error: You are trying to randomize more operators than are available.")
        return []
    random_operators = random.sample(roles, num_operators)
    return random_operators

if side.capitalize() == 'Defender':
    defender_operators = randomize_operators(num_operators, defender_roles)
    print(f"Your defender operators are: {', '.join(defender_operators)}")

else:
    attacker_operators = randomize_operators(num_operators, attacker_roles)
    print(f"Your random attacker operators are: {', '.join(attacker_operators)}")
'''
print("This was the original master code before it was broken down.")