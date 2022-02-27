print("***********Welcome to the the tennis match predictor***********")


def rate(a, b):
    a = int(a)
    b = int(b)
    return round((b/a)*100, 1)


def display(data):
    for i in range(0, 6):
        print(data[i])


try:
    print("Player1 TextFile: ", end=" ")
    f1 = open(input(), "r")
    player1 = f1.read()
    data1 = player1.split("\n")
    data1[0] = "Tennis Player 1: "+data1[0]
    p1_games = (data1[1].split(":"))[1]
    p1_win = (data1[2].split(":"))[1]
    p1_lost = (data1[3].split(":"))[1]
    p1_winrate = rate(p1_games, p1_win)
    p1_lostrate = rate(p1_games, p1_lost)
    data1.append("Win Rate: " + str(p1_winrate))
    data1.append("Lost Rate: " + str(p1_lostrate))

    print("VS")

    print("Player2 TextFile: ", end=" ")
    f2 = open(input(), "r")
    player2 = f2.read()
    data2 = player2.split("\n")
    data2[0] = "Tennis Player 2: " + data2[0]
    p2_games = (data2[1].split(":"))[1]
    p2_win = (data2[2].split(":"))[1]
    p2_lost = (data2[3].split(":"))[1]
    p2_winrate = rate(p2_games, p2_win)
    p2_lostrate = rate(p2_games, p2_lost)
    data2.append("Win Rate: " + str(p2_winrate))
    data2.append("Lost Rate: " + str(p2_lostrate))

    display(data1)
    display(data2)

    if p1_winrate > p2_winrate:
        print(data1[0]+" will most likely win the match")
    else:
        print(data2[0]+" will most likely win the match")

except Exception:
    print("file name or file format is incorrect")
