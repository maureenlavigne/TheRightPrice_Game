
import time

# Functions
def slow_writing(txt, speed=0.05):
    for c in txt:
        print(c, end="")
        time.sleep(speed)
    print()


def guide_user(proposition, solution):
    if proposition < solution:
        slow_writing("Raté. Le juste prix est plus grand.")
        return False

    elif proposition > solution:
        slow_writing("Raté. Le juste prix est plus petit.")
        return False
    elif proposition == solution:
        slow_writing("Gagné ! Le juste prix est bien " + str(solution) + " euros.")
        return True

def main():
    # Welcome User
    slow_writing("Bienvenue au Juste Prix !")
    time.sleep(1)
    slow_writing("Pour trouver le juste prix, proposez un nombre et vous serrez guidé.")

    # Computer chooses solution (easy version : only one solution)
    solution = 12500

    # Ask user input
    # Guide user to find right price
    solution_found = False
    while not solution_found:
        try:
            proposition = int(input("Proposez un nombre : ")) # Handling Value Error (Forcing Int)
            solution_found = guide_user(proposition,solution)
        except ValueError:
            slow_writing("Attention, vous ne pouvez proposer que des nombres.")

if __name__ == "__main__":
    main()