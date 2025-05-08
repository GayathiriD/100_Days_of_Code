from art import logo
print(logo)


def  highest_bidder(bidding):
    highest_bidder = 0
    winner_name = ""
    for bidder in bidding:
        bidder_amount = bidding[bidder]
        if bidder_amount > highest_bidder:
            highest_bidder= bidder_amount
            winner_name = bidder
    print(f"The winner is {winner_name} with a bid of ${highest_bidder}.")        


bid = {}

continue_bidding = True

while continue_bidding:
    name = input("Enter your name:")
    prize= int(input("Enter the prize of the auction :$"))
    bid[name] = prize
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no':")
    if more_bidders.lower() =='no':
        break
    elif more_bidders.lower() =='yes':
        print("\n"*20)
        continue_bidding = True
highest_bidder(bid)   