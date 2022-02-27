# You are given a list which contains some numbers. You have to print a list of next palindromes only if the number is greater than 10 otherwise you will print that number.
#
# Input:
#
# [1, 6, 87, 43]
#
# Output:
#
# [1, 6, 88, 44]

def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    size = int(input("Enter the size of your list\n"))
    num_list = []
    for i in range(size):
        num_list.append(int(input("Enter the number of the list\n")))
    # print("You have entered" , num_list)
    print(f"You have entered {num_list}")

    # list comprehension: always returns a list
    print(f"Output List{[num_list[i] if num_list[i] < 10 else next_palindrome(num_list[i]) for i in range(size)]}")

                    #or

    # new_list = []
    # for element in num_list:
    #     if element >10:
    #         n = next_palindrome(element)
    #         new_list.append(n)
    #
    #     else:
    #         new_list.append(element)
    # print(f"Output List: {new_list}")


