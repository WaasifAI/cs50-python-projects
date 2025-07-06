# Simple Pattern Generator - Lecture 2: Loops

# function for star pyramid generator
def star_pyramid(rows):
    print("\n Star Pyramid ")
    for i in range(rows):
        spaces = " " * (rows - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

# function to genarate number pyramid 
def number_pyramid(rows):
    print("\n Number Pyramid ")
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)

        # Numbers going up: 1 to i
        up = ""
        for j in range(1, i + 1):
            up += str(j)

        # Numbers going down: i-1 to 1
        down = ""
        for j in range(i - 1, 0, -1):
            down += str(j)

        print(spaces + up + down)


def main():
    print(" Pattern Generator ")

    rows = int(input("Enter number of rows: "))
    print("1. Star Pyramid")
    print("2. Number Pyramid")
    choice = input("Choose pattern (1 or 2): ")

    if choice == "1":
        star_pyramid(rows)
    elif choice == "2":
        number_pyramid(rows)
    else:
        print("Invalid choice. Please choose 1 or 2.")




if __name__ == "__main__":
    main()
