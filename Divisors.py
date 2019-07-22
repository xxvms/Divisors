user_input = input("Please enter the number: ")

def modulo_test(user_i):
    # creating range of numbers to check user input
    user_range = range(1, int(user_i))

    for element in user_range:
        if (int(user_i) % element) == 0:
           print(element)

modulo_test(user_input)
