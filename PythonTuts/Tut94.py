def per(n, steps=0):
    if len(str(n)) == 1:
        print(n)
        print("TOTAL STEPS " + str(steps))
        return "Done"

    steps += 1
    digits = [int(i) for i in str(n)]

    result = 1
    for j in digits:
        result *= j
    print(result)
    per(result, steps)


per(277777788888899)
