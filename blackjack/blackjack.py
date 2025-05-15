import  random
from logo import logo


human = []
computer = []
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    human = []
    computer = []
    while(True):


        choice = input("Type 'deal' to get another card or 'stand' to stop: ")
        if choice.lower() == 'deal':
            n = random.choice(cards)
            human.append(n)
            print(sum(human))
            print("Do you want to draw another card or stand?")

            print("sum of cards", sum(human))
        elif choice.lower()== 'stand':
            while(sum(computer)<17):
                computer.append(random.choice(cards))
                print("Computer choice", sum(computer))
            if sum(human) > 21:
                if 11 in human:
                    i = human.index(11)
                    human[i] = 1
                    if sum(human) > 21:
                        print("You busted. Computer Wins")
                    else:
                        print("You Wins")
            elif sum(computer) > 21:
                print("Computer busted, You Wins")
            elif sum(human) > sum(computer):
                print("You Wins!")
            elif sum(computer) > sum(human):
                print("Computer Wins!")
            elif sum(human) == sum(computer):
                print("It's a draw")
            break

deal_cards()

