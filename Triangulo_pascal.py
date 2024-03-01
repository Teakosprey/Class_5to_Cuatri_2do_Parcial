def calculate_previous_row(previous_row):
    new_row = [1]
    for i in range(len(previous_row) - 1):
        new_row.append(previous_row[i] + previous_row[i + 1])
    new_row.append(1)
    return new_row

def generate_pascal_triangle(num_rows):
    pascal_triangle = [[1]]
    for _ in range(num_rows - 1):
        next_row = calculate_previous_row(pascal_triangle[-1])
        pascal_triangle.append(next_row)
    return pascal_triangle

def print_pascal_triangle(num_rows):
    pascal_triangle = generate_pascal_triangle(num_rows)
    for row in pascal_triangle:
        print(" ".join(map(str, row)))

def main():
    try:
        rows = int(input("Insert the quantity of rows: "))
        if rows < 1:
            print("The rows quantity must be major than 1.")
            return
        print_pascal_triangle(rows)
    except ValueError:
        print("Insert a valid number.")

main()
