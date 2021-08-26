#blackjack
import random

result_1 = random.randrange(1,11)
result_2 = random.randrange(1,11)
result_3 = random.randrange(1,11)
result_4 = random.randrange(1,11)
result_5 = random.randrange(1,11)
card_1 = [result_1]
card_2 = [result_2]
card_3 = [result_3]
card_4 = [result_4]
card_5 = [result_5]
win_condition_1 = sum(card_1 + card_2)
win_condition_2 = sum(card_1 + card_2 + card_3)
win_condition_3 = sum(card_1 + card_2 + card_3 + card_4)
win_condition_4 = sum(card_1 + card_2 + card_3 + card_4 + card_5)
loss_condition1 = sum(card_1 + card_2)
loss_condition2 = sum(card_1 + card_2 + card_3)
loss_condition3 = sum(card_1 + card_2 + card_3 + card_4)
loss_condition4 = sum(card_1 + card_2 + card_3 + card_4 + card_5)
response = input("Do you wanna draw another card? P/D\n")
output1 = print('{} {} {} {} {} '.format(card_1, "+", card_2, "=", loss_condition1))
output2 = print('{} {} {} {} {} {} {}'.format(card_1, "+", card_2, "+", card_3, "=", loss_condition2))
output3 = print('{} {} {} {} {} {} {} {} {}'.format(card_1, "+", card_2, "+", card_3, "+", card_4, "=" , loss_condition3))
output4 = print('{} {} {} {} {} {} {} {} {} {} {}'.format(card_1, "+", card_2, "+", card_3, "+", card_4, "+", card_5, "=", loss_condition4))
def play():

    while loss_condition1 <= 21 :
        output1
        response    
        
        if response == "D" :
            

            if win_condition_2 == 21:
                print("Winner Winner!")
                input("Wanna play again? Y/N\n")
            if "Y" :   
                play()             
            if "N" :
                break
                
            if loss_condition2 >= 21:
                print ("You Lost!")
                input("Wanna play again? Y/N\n")
                if "Y" :
                    play()
                if "N" :
                    break
            output2
            response
            if response == "D" :
                
            
                if win_condition_3 == 21:
                    print("Winner Winner!")
                    input("Wanna play again? Y/N\n")
                if "Y" :
                    play()       
                if "N" :
                    break

            if loss_condition3 >= 21:
                print ("You Lost!")
                input("Wanna play again? Y/N\n")
                if "Y" :
                    play()
                if "N" :
                    break

            output3
            response    
            if response == "D" :
                
                
                if win_condition_4 == 21:
                    print("Winner Winner!")
                    input("Wanna play again? Y/N\n")
                if "Y" :
                    play()    
                if "N" :
                    break

            if loss_condition4 >= 21:
                print ("You Lost!")
                input("Wanna play again? Y/N\n")
                if "Y" :
                    play()
                if "N" :
                    break
        else :
            print("Error")
play()

