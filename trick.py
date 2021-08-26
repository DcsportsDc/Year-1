import random as rd

b = rd.randrange(1, 11)
a = rd.randrange(1, 11)

def blackjack(a, b) : 
    print(a, b)
    blackjack(a, b)
