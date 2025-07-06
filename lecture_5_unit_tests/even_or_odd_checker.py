# even or odd checker - Lecture 5 unit tests

# function to check wether a number is even or odd
def is_even(num):
 
    if num % 2 == 0:
        return "even number" 
    else:
        return "odd number" 

# main function
def main():
    print("welcome to even or odd checker")
    try:
        num = int(input("what's the number: "))
    except ValueError:
        print("please provide a number")  
    
    result = is_even(num)
    print(f"It's an  {result}")    

if __name__ == "__main__":
    main()