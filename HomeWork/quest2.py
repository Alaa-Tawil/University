# Quest 2

def bin_to_dec(binary_str):
    decimal_number = 0
    try:
        for digit in binary_str:
            if digit not in ('0', '1'):
                raise ValueError("Non-binary digit found")
            decimal_number = decimal_number * 2 + int(digit)
        return decimal_number
    except ValueError:
        print("Please type a valid binary number")
        return None

def main():
    while True:
        binary_str = input("Type a binary number: ")
        decimal_number = bin_to_dec(binary_str)
        
        if decimal_number is not None:
            print(f"Your binary number is: {binary_str} and in decimal is: {decimal_number}")
            break

if __name__ == "__main__":
    main()

