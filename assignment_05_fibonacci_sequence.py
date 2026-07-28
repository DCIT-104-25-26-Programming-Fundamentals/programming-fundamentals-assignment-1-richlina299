def print_fibonacci(n):
    if n <= 0:
        print("Error: Number of terms must be greater than 0.")
        return

    a = 0
    b = 1

    print("Fibonacci sequence:", end=" ")

    for i in range(n):
        print(a, end=" ")
        next_num = a + b
        a = b
        b = next_num

    print()


def is_fibonacci(number):
    if number < 0:
        return False

    a = 0
    b = 1

    while a < number:
        next_num = a + b
        a = b
        b = next_num

    return a == number


def main():
    # Part A
    n = int(input("How many terms? "))
    print_fibonacci(n)

    # Part B
    number = int(input("Enter a number to check: "))

    if is_fibonacci(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


# Run the program
main()
