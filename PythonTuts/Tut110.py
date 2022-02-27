def computerPay(h, r):
    def computerPay1(h1, r1):
        h2 = h1 - 40
        r2 = r1 * 1.5
        g2 = h2 * r2
        g1 = 40 * r1
        g = g1 + g2
        return g

    def computerPay2(h1, r1):
        g2 = 0
        g1 = h1 * r1
        g = g1 + g2
        return g

    if h > 40:
        p1 = computerPay1(h, r)
        print(p1)
    else:
        p2 = computerPay2(h, r)
        print(p2)


hrs = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
computerPay(hrs, rate)
