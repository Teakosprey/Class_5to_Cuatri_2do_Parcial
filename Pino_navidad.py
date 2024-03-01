def print_tree(size):
    if size < 6:
        print("The size must be bigger than 6.")
        return

    for i in range(1, size + 1):
        space = " " * (size - i)
        asterik = "*" * (2 * i - 1)
        print(space + asterik)

    # Tronco del árbol
    base = " " * (size - 1) + "|"
    for _ in range(size // 3):
        print(base)


def main():
    try:
        size = int(input("Insert tree size (min 6): "))
        print_tree(size)
    except ValueError:
        print("Insert a valid number.")
        
        
main()