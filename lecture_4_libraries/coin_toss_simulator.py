# coin toss simulator - lecture 4 libraries (random)
# function for tossing a coin 
import random
def toss_coin():
    return random.choice(["heads","tails"])

# main function
def main():
    print("welcome to coin toss simulator ")
    #loop to continue the game 
    while True:

        # asking for user's wish
        user_input = str(input("do you want to toss a coin (yes/no)")).strip().lower()


        if user_input == "yes":
            result = toss_coin()
            print(f"it's a {result}")
        elif user_input in ["no", "exit"]:
            print("Thanks for playing goodbye")
            break
        else:
            print("invalid choice")


if __name__ == "__main__":
    main()
