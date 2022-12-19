from random import shuffle

print(('🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂬🂮' + '🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾🂼') * 3)
print('''
    |       \|  \                 |  \                                |  \      
    | ▓▓▓▓▓▓▓\ ▓▓ ______   _______| ▓▓   __       __  ______   _______| ▓▓   __ 
    | ▓▓__/ ▓▓ ▓▓|      \ /       \ ▓▓  /  \     |  \|      \ /       \ ▓▓  /  \\
    | ▓▓    ▓▓ ▓▓ \▓▓▓▓▓▓\  ▓▓▓▓▓▓▓ ▓▓_/  ▓▓      \▓▓ \▓▓▓▓▓▓\  ▓▓▓▓▓▓▓ ▓▓_/  ▓▓
    | ▓▓▓▓▓▓▓\ ▓▓/      ▓▓ ▓▓     | ▓▓   ▓▓      |  \/      ▓▓ ▓▓     | ▓▓   ▓▓ 
    | ▓▓__/ ▓▓ ▓▓  ▓▓▓▓▓▓▓ ▓▓_____| ▓▓▓▓▓▓\      | ▓▓  ▓▓▓▓▓▓▓ ▓▓_____| ▓▓▓▓▓▓\ 
    | ▓▓    ▓▓ ▓▓\▓▓    ▓▓\▓▓     \ ▓▓  \▓▓\     | ▓▓\▓▓    ▓▓\▓▓     \ ▓▓  \▓▓\\
    \▓▓▓▓▓▓▓ \▓▓ \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓\▓▓   \▓▓__    | ▓▓ \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓\▓▓   \▓▓
                            Welcome to     |  \__/ ▓▓                     
                                            \▓▓    ▓▓                           
                                            \▓▓▓▓▓▓                  
    ''')
print(('🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎🃌' + '🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞🃜') * 3)

# Asks the player how much money you want to start the game with. This is for the betting system.
user_money = int(input('How much money would you like to start off with?'))

def blackjack():
    # Define a list of suits
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]

    # Define a list of ranks
    cardranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    # Generate a deck of cards as a list of tuples, with each tuple containing a rank and a suit
    deck = [(rank, suit) for rank in cardranks for suit in suits]

    # Shuffle the deck
    shuffle(deck)

    # Define a dictionary to map ranks to numerical values
    rank_values = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

    # Define a function to deal a card to a player
    def deal_card(hand):
        # Draw a card from the deck and append it to the player's hand
        hand.append(deck.pop(0))

    # Define a function to calculate the total value of a player's hand
    def calculate_hand_total(hand):
        # Initialize a variable to store the total value of the hand
        total = 0

        # Iterate over the cards in the hand
        for card in hand:
            # Add the value of the card to the total
            total += rank_values[card[0]]

        # Check if the hand contains an Ace
        if any(card[0] == "Ace" for card in hand):
            # If so, check if adding 10 to the total would not bust the hand (total > 11)
            if total + 10 <= 21:
                # If not, add 10 to the total
                total += 10

        # Return the total value of the hand
        return total

    # Define a function to play a game of Blackjack
    def play_blackjack(user_money):
        user_money  = user_money
        current_bet = 0
        def bet_result(result):
            nonlocal current_bet, user_money
            if current_bet > 0:
                # Result if the player lost, player loses current bet
                if result == 'lost': 
                    input(f'You lost ${current_bet} :(\n')
                    current_bet = 0
                    return user_money, current_bet
                # Result if the player lost, player doubles current bet
                elif result == 'won':
                    current_bet *= 2
                    input(f'You gained ${current_bet}! 💰\n')
                    user_money += current_bet
                    current_bet = 0
                    return user_money, current_bet
                # Result if player and computer has the same total, current bet is returned
                else:
                    user_money += current_bet
                    input(f'The bet has been returned to your wallet.\n')
                    current_bet = 0
                    return user_money, current_bet


        # Deal the player and dealer two cards each
        player_hand = [deck.pop(0), deck.pop(0)]
        dealer_hand = [deck.pop(0), deck.pop(0)]

        # Cleans up the hands to look nicer when printed
        def clean_hand(hand):
            card_image = ''
            if hand is player_hand:
                card_image ='🃏'
            else:
                card_image = '🃟'
            player_hand_str = ', '.join(
                [f'{card[0]} of {card[1]}{card_image}' for card in hand])
            return player_hand_str

        blackjack_bet = 0
        if user_money > 0:    
            # Request the player's bet amount. Try and Except added in the event the player doesn't input a valid number which will result in no bet being placed.
            try:
                blackjack_bet = int(input(
                    f'\nWould you like to place a bet?\nCurrent money: ${user_money}\nEnter the number of the bet you want to place, or enter "0" to play for free.\n[BET]:'))
                print(f'You placed down a bet of ${blackjack_bet}')
                #Checks if the bet is less than or equal to the player's current money
                if int(blackjack_bet) <= user_money:
                    user_money -= int(blackjack_bet) # Hero's money is deducted by the player's bet amount
                    current_bet += int(blackjack_bet) # Current bet amount is updated with the player's bet amount
            except:
                input(f'\nNo bet was placed.')
                pass
        
        def blackjack_results():
            # Calculate the total value of the dealer's hand
            dealer_total = calculate_hand_total(dealer_hand)

            # Print the dealer's hand
            print(
                f'Dealer\'s hand: {clean_hand(dealer_hand)} Total: {dealer_total}')

            # Check if the dealer has 21 (Blackjack)
            if dealer_total == 21:
                if player_blackjack == True:
                    input('Player and Dealer both have 21. Push..')
                else:
                    # If so, end the game and print a message
                    input('Dealer has Blackjack! Dealer wins.')
                    bet_result('lost')
                    return

            # While the dealer's hand is less than 17, hit
            while dealer_total < 17:
                if player_total > 21:
                    break
                # Deal a card to the dealer
                input('Dealer draws a card...press enter to continue...')
                deal_card(dealer_hand)

                # Calculate the total value of the dealer's hand
                dealer_total = calculate_hand_total(dealer_hand)

                # Print the dealer's hand
                print(
                    f'Dealer\'s hand: {clean_hand(dealer_hand)} Total: {dealer_total}')

            # Check if the dealer has busted (total > 21)
            if dealer_total > 21:
                # Check if the player already has 21
                if player_total == 21:
                    input('Dealer has busted. Player has 21.')
                else:
                    input('Dealer has busted! Player wins.')
                bet_result('won')
            elif dealer_total == 21:
                if player_total == 21:
                    input('Player and Dealer both have 21. Push..')
                    bet_result('push')

            print(
                f'Current Player Total: {player_total} 🃏\nCurrent Dealer Total: {dealer_total} 🃟')
            # Compare the player's and dealer's totals
            if player_total > dealer_total:
                if player_total <= 21:
                    # If the player's total is greater and less than or equal to 21, the player wins
                    input('Player wins!')
                    bet_result('won')
            elif player_total < dealer_total:
                if dealer_total <= 21:
                    # If the dealer's total is greater and less than or equal to 21, the dealer wins
                    input('Dealer wins..')
                    bet_result('lost')
            else:
                # If the totals are equal, the game is a push
                input('Push..')
                bet_result('push')
                
        # Calculate the total value of the player's hand
        player_total = calculate_hand_total(player_hand)
        # Print the total value of the player's hand
        print(f'Player\'s hand: {clean_hand(player_hand)} Total: {player_total}')
        player_blackjack = False
        eleven_double_bet = 0
        eleven_ans = ''
        # Check if the player has 21 (Blackjack)
        if player_total == 21:
            # If so, end the game and print a message
            input('PLAYER HAS BLACKJACK! Winnings are doubled. Player wins.')
            bet_result('won')
            player_blackjack = True
            current_bet *= 2
            return player_blackjack, current_bet
        elif player_total == 11:
            eleven_ans = input(f'Player hit a soft 11! Would you like to double down your bet and play one more hand?')
        if eleven_ans.strip().lower() in ('yes', 'y', 'ok', 'kk', 'sure', 'okay', 'yep'):
            double_down = current_bet
            if double_down <= user_money:
                print('You doubled down!')
                eleven_double_bet += 1
                user_money -= double_down
                current_bet += double_down
                # Calculate the total value of the player's hand
                player_total = calculate_hand_total(player_hand)
                # Deals another hand
                deal_card(player_hand)
                # Calculate the total value of the player's hand
                player_total = calculate_hand_total(player_hand)
                # Print the player's hand
                print(
                    f'Player\'s hand: {clean_hand(player_hand)} Total: {player_total}')
                blackjack_results()
            else:
                input(f'You cannot afford to double down!')
        while eleven_double_bet == 0:
            # If player has blackjack, this will break the while loop
            if player_blackjack == True:
                break
            # Get the player's decision
            decision = input(f'\n(You can type ".." or "hit", and "stand" or the enter key to Stand)\nHit or Stand?')

            # Check if the player decided to hit
            if decision.lower() in ('hit', '..', '  '):
                # If so, deal a card to the player
                print('Player draws a card...press enter to continue...')
                deal_card(player_hand)

                # Calculate the total value of the player's hand
                player_total = calculate_hand_total(player_hand)

                # Print the player's hand
                print(f'Player\'s hand: {clean_hand(player_hand)} Total: {player_total}')

                # Check if the player has busted (total > 21)
                if player_total > 21:
                    # If so, end the game and print a message
                    input('Player has busted! Dealer wins.')
                    bet_result('lost')
                    break
            # If the player decided to stand, break out of the loop
            else:
                print('Player stands 👋')
                break
        if eleven_double_bet == 0:
            blackjack_results()
        else:
            pass
        # Play a game of Blackjack
        play_blackjack(user_money)
    # Play a game of Blackjack
    play_blackjack(user_money)
# Play a game of Blackjack it never ends...
blackjack()