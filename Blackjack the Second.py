import random as rd
from typing import Generator

card_1 = rd.randrange(1,11)
card_2 = rd.randrange(1,11)
card_3 = rd.randrange(1,11)
card_4 = rd.randrange(1,11)
card_5 = rd.randrange(1,11)

first_move = card_1 + card_2
second_move = card_1 + card_2 + card_3
third_move = card_1 + card_2 + card_3 + card_4
fourth_move = card_1 + card_2 + card_3 + card_4 + card_5

def blackjack() :
    print('{} + {}'.format(card_1, card_2))
    print(first_move)
    input("Do you wanna draw another card? Y/N\n")   

    while first_move < 21:
        if "Y":
            result_2()
            return
        elif "N":
            print("You Won!")
            restart()
            break
    else:
        print("Why?")
    while first_move > 21:
        print("You Lost!")
        break
    while first_move == 21:
        print("BlackJack!")
        break
##################
def restart():
    input("Do you wanna play again? Y/N\n")   
    if "Y"  :
        blackjack()
    elif "N" :
        print("Acceptation is where it starts.")
##################
def result_2() :
    print('{} + {} + {}'.format(card_1, card_2, card_3))
    print(second_move)
    input("Do you wanna draw another card? Y/N\n")   
    while second_move < 21:
        if "Y" :    
            result_3()
            return
        elif "N" :
            print("You Won!")
            restart()
            break
    while second_move > 21:
        print("You Lost!")
        restart()
        break
    while second_move == 21:
        print("BlackJack!")
        restart()
        break
##################
def result_3() :
    print('{} + {} + {} + {}'.format(card_1, card_2, card_3, card_4))
    print(third_move)
    input("Do you wanna draw another card? Y/N\n")   
    while third_move < 21:
        if "Y" :  
            result_4()
            return
        elif "N" :
            print("You Won!")
            restart()
            break
    while third_move > 21:
        print("You Lost!")
        restart()
        break
    while third_move == 21:
        print("BlackJack!")
        restart()
        break
##################
def result_4() :
    print('{} + {} + {} + {} + {}'.format(card_1, card_2, card_3, card_4, card_5))
    print(fourth_move)
    while fourth_move == 21:
        print("BlackJack!")
        break
    while fourth_move <= 21:
        print("You Won!")
        restart()
        break
    while fourth_move >= 21:
        print("You Lost!")
        restart()
        break
##################
blackjack()







