
import time
import random

# Functions
def slow_writing(txt, speed=0.05):
    for c in txt:
        print(c, end="")
        time.sleep(speed)
    print()


# Takes user proposition and computer solution (= price to find) and return :
# 1 if smaller
# 2 if bigger
# 0 if price found
def guide_user(proposition, solution):
    if proposition < solution:
        return 1
    elif proposition > solution:
        return 2
    elif proposition == solution:
        return 0


def main():

    # Variables + Lists - Dictionary Version
    price_of_objects = {"stylo": 5, "grosse BD": 32, "PC Gamer": 1305,
                        "Twingo 3": 10210, "maison à Royat": 400987}

    # Welcome User
    slow_writing("Bienvenue au Juste Prix !")
    time.sleep(1)
    slow_writing("Pour trouver le juste prix, proposez un nombre et vous serrez guidé.")

    # Computer chooses solution - Dictionary Version
    objet = random.choice(list(price_of_objects.keys()))
    slow_writing("Devinez le prix en euros de : " + objet)
    solution = price_of_objects.get(objet)

    # Ask user input
    # Guide user to find right price

    test = 3
    while test != 0:
        try:
            proposition = int(input("Proposez un nombre : "))  # Handling Value Error (Forcing Int)
            test = guide_user(proposition,solution)
            if test == 0:
                slow_writing("Gagné ! Le juste prix de " + objet + " est bien " + str(solution) + " euros.")
            elif test == 1:
                slow_writing("Raté. Le juste prix est plus grand.")
            elif test == 2:
                slow_writing("Raté. Le juste prix est plus petit.")

        except ValueError:
            slow_writing("Attention, vous ne pouvez proposer que des nombres.")


if __name__ == "__main__":
    main()