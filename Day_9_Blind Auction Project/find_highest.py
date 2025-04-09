def find_highest_bid(bidders):
    #way 3
    a =0
    winner =""
    for i in bidders:
        if bidders[i] > a:
            a = bidders[i]
            winner = i
    print(f'The highest bid is ${a} and the winner is {winner}')

    # way 1
    # a = 0
    # for i in bidders:
    #     if a < bidders[i]:
    #         a= bidders[i]
    # for i in bidders:
    #     if a == bidders[i]:
    #         print(f"The winner is {i}")

    # way2
    # print(f"The highest bit is by {max(bidders, key =bidders.get)}")