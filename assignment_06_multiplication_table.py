def print_table(number):
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")


def print_tables_up_to(n):
    if n <= 0:
        print("Error: Number must be greater than 0.")
        return

    for i in range(1, n + 1):
        print_table(i)
        print("-" * 27)


def main():
    # Part A
    number = int(input("Enter a number: "))

    if number <= 0:
        print("Error: Number must be greater than 0.")
        return

    print_table(number)

    # Part B
    n = int(input("\nEnter a number N: "))

    if n <= 0:
        print("Error: Number must be greater than 0.")
        return

    print_tables_up_to(n)


# Run the program
main()
