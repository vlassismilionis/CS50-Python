def main():
    d = 50

    #Getting coin from user and calculating
    while True:
        print("Amount Due:", d)
        x = int(input("Insert Coin: "))
        if x != 25 and x != 10 and x != 5:
            continue
        else:
            d = d - x
            if d > 0:
                continue
            else:
                print("Change Owed:", abs(d))
                break


main()