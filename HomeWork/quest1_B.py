#Quest 1-B

def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

def main():
    while True:
        try:
            num = int(input("Enter a number to calculate its factorial: "))
            if num < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                print(f"The factorial of {num} is {factorial(num)}")
            break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()