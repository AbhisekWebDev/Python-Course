import os

def find_winner(bidder_details):
    highest_bid = 0
    winner = ""
    for bidder in bidder_details:
        bidding_price = bidder_details[bidder]
        if bidding_price > highest_bid:
            highest_bid = bidding_price 
            winner = bidder
        
    print(f"The list of bidders are : {bidder_data}")

    print(f"The highest bidder is {winner} & the bid amount is {highest_bid}")

bidder_data = dict({})

end_of_bidding = False

while not end_of_bidding:

    name = input("Enter your name : ")
    bid = int(input("Enter your bid prize : "))

    bidder_data[name] = bid

    other_bidders = input("Are there any other bidders? : type 'Y' for yes & 'N' for no : ").lower()

    if other_bidders == 'n':
        end_of_bidding = True
        find_winner(bidder_data)
    elif other_bidders == 'y':
        os.system('cls')