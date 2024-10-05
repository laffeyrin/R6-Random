from defender import Defender
from attacker import Attacker

def main():
    side = input("Enter 'Defender' or 'Attacker': ")
    while side.capitalize() not in ['Defender', 'Attacker']:
        print("Invalid input. Please enter 'Defender' or 'Attacker'.")
        side = input("Enter 'Defender' or 'Attacker': ")
    print(f"You are playing on {side.capitalize()}.")
    
    num_operators = int(input("Enter the number of operators you want to randomize: "))
    
    if side.capitalize() == 'Defender':
        defender = Defender()
        defender_operators = defender.randomize_operators(num_operators)
        print(f"Your defender operators are: {', '.join(defender_operators)}")
    else:
        attacker = Attacker()
        attacker_operators = attacker.randomize_operators(num_operators)
        print(f"Your random attacker operators are: {', '.join(attacker_operators)}")

if __name__ == "__main__":
    main()