def get_value_at_index(input_value):
    array = [10, 20, 30, 40, 50]  # Your array of values

    if input_value < 0 or input_value >= len(array):
        return -1
    else:
        return array[input_value]

# Prompt the user for input
user_input = int(input("Enter an index: "))
result = get_value_at_index(user_input)

if result == -1:
    print("Index out of bounds. Returning -1.")
else:
    print(f"Value at index {user_input}: {result}")
