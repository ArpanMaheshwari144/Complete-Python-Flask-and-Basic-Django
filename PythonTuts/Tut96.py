# comparator function for sort
def mixs(num):
    try:
        element = int(num)
        return (0, element, '')
    except ValueError:
        return (1, num, '')


test_list = ['1500', '89', '3', 'forty', 'one', 'two']

print("The original list: " + str(test_list))

# using sort() + comparator
test_list.sort(key=mixs)

print("The sorted list is: " + str(test_list))
