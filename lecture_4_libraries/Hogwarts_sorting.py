#importing a library called random
import random
#function for sorting of houses in hogwarts school
def sorting():
    while True:
        name = str(input("what's your name: "))
        house = random.choice(["Gryffindor", "ravenclaw", "hufflepuff", "slytherin"])
        print(f"{name} you belongs to....  {house}")
        print(f"your sorting is completed {name} of house {house}")
#main function
def main():
    sorting()

#calling of main function
if __name__ == "__main__":
    main()