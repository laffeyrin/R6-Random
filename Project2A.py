import random

print("Welcome to R6 Randomizor")
print("Are you playing on Defender or Attackers?")

side = input("Enter 'Defender' or 'Attacker': ")

while side.capitalize() not in ['Defender', 'Attacker']:
    print("Invalid input. Please enter 'Defender' or 'Attacker'.")
    side = input("Enter 'Defender' or 'Attacker': ")

print(f"You are playing on {side.capitalize()}.")

if side.capitalize() == 'Defender':
    print("You will be playing as a defender. You will be given a random defender role.")
else:
    print("You will be playing as an attacker. You will be given a random attacker role.")

num_operators = int(input("Enter the number of operators you want to randomize: "))

defender_roles = ["Ash", "Thermite", "Twitch", "Montagne", "Rook", "Doc", "Mute", "Smoke", "Castle", "Pulse", "Thatcher", "Frost", "Vigil"]
attacker_roles = ["Fuze", "Glaz", "Buck", "Blackbeard", "Capitao", "Hibana", "Echo", "Ying", "Lesion", "Zofia", "Nomad", "Gridlock", "Nokk"]

def randomize_operators(num_operators, roles):
    if num_operators > len(roles):
        print("Error: You are trying to randomize more operators than are available.")
        return []
    random_operators = random.sample(roles, num_operators)
    return random_operators

if side.capitalize() == 'Defender':
    defender_operators = randomize_operators(num_operators, defender_roles)
    attacker_operators = randomize_operators(num_operators, attacker_roles)
else:
    attacker_operators = randomize_operators(num_operators, attacker_roles)
    defender_operators = randomize_operators(num_operators, defender_roles)

if defender_operators and attacker_operators:
    print(f"Your random defender operators are: {', '.join(defender_operators)}")
    print(f"Your random attacker operators are: {', '.join(attacker_operators)}")