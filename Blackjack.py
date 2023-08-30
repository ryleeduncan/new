import random

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    
    for card in hand:
        if card == "A":
            num_aces += 1
            value += 11
        elif card in ["K", "Q", "J"]:
            value += 10
        else:
            value += int(card)
    
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    
    return value

# Function to display the current game state
def display_game_state(player_hand, dealer_hand, player_value, dealer_value, game_over=False):
    print("\n--- Player Hand ---")
    print(" ".join(player_hand), "   Value:", player_value)
    
    print("\n--- Dealer Hand ---")
    if game_over:
        print(" ".join(dealer_hand), "   Value:", dealer_value)
    else:
        print(dealer_hand[0], " ?")
    
# Main game loop
def blackjack_game():
    while True:
        print("\nWelcome to Blackjack!")
        
        # Initialize deck and hands
        deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 4
        random.shuffle(deck)
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]
        
        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)
        
        display_game_state(player_hand, dealer_hand, player_value, dealer_value)
        
        # Player's turn
        while player_value < 21:
            action = input("\nDo you want to 'hit' or 'stand'? ").lower()
            if action == "hit":
                player_hand.append(deck.pop())
                player_value = calculate_hand_value(player_hand)
                display_game_state(player_hand, dealer_hand, player_value, dealer_value)
            elif action == "stand":
                break
        
        # Dealer's turn
        while dealer_value < 17:
            dealer_hand.append(deck.pop())
            dealer_value = calculate_hand_value(dealer_hand)
        
        # Display final game state
        display_game_state(player_hand, dealer_hand, player_value, dealer_value, game_over=True)
        
        # Determine the winner
        if player_value > 21:
            print("\nPlayer busts! Dealer wins.")
        elif dealer_value > 21:
            print("\nDealer busts! Player wins.")
        elif player_value > dealer_value:
            print("\nPlayer wins!")
        elif player_value < dealer_value:
            print("\nDealer wins!")
        else:
            print("\nIt's a tie!")
        
        play_again = input("\nDo you want to play again? (yes/no) ").lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break

# Start the game
blackjack_game()
