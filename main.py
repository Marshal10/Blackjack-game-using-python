from art import logo
from random import shuffle, choice
import os

def clear_screen():
    os.system('cls')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
shuffle(cards)

def begin_game():
    while True: 
        start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

        if start_game in ['y', 'n']: 
            break
        else:   
            print("Invalid input, please type 'y' or 'n'")
    clear_screen()        
    yes_start(start_game)

def score(cards):    
    return sum(cards)  

def cards_busted(score):
    return score > 21

def winner(player_cards, computer_cards):    
    if score(computer_cards) > 21:
        print("Computer went over, You win")
    elif score(player_cards) == 21:
        if score(computer_cards) == 21:
            print("Computer got the Blackjack too, You lose")
        else:
            print("Blackjack!!!!!!!!!!, You Won")
    elif 21 >= score(player_cards) > score(computer_cards) >= 0:
        print("You Win")
    elif score(player_cards) == score(computer_cards) <= 21:
        print("It's a draw")
    else:
        print("You Lose")

def ace_value(cards):
    modified_cards = []
    for card in cards:
        if card == 11 and score(cards) > 21:
            modified_cards.append(1)
        else:
            modified_cards.append(card)
    return modified_cards

def black_jack(player_score, computer_score, computer_cards):
    if player_score == 21:
        if computer_score == 21:
            print(f"\tComputer's cards: {computer_cards}, final score: {computer_score}")
            print("Computer got the Blackjack too, You lose")
        else:
            print("Blackjack!!!!!!!!!!, You Won")
            print(f"\tComputer's cards: {computer_cards}, final score: {computer_score}")
            begin_game()

def yes_start(start_game):
    if start_game == 'y':
        print(logo)
        player_cards = []
        computer_cards = []
        for i in range(2):
            player_cards.append(choice(cards))
            computer_cards.append(choice(cards))
        player_cards = ace_value(player_cards)    
        sum_of_player_cards = score(player_cards)
        sum_of_computer_cards = score(computer_cards)
        print(f"\tYour cards: {player_cards}, current score: {sum_of_player_cards}")
        print(f"\tComputer's first card: {computer_cards[0]}")
        black_jack(sum_of_player_cards, sum_of_computer_cards, computer_cards)
        
        while True:
            ask_more_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if ask_more_card == 'y':
                player_cards.append(choice(cards))
                player_cards = ace_value(player_cards)
                sum_of_player_cards = score(player_cards)
                print(f"\tYour cards: {player_cards}, current score: {sum_of_player_cards}")
                print(f"\tComputer's first card: {computer_cards[0]}")
            else:
                while score(computer_cards) < 17:
                    computer_cards.append(choice(cards))
                print(f"\tYour final hand: {player_cards}, final score: {sum_of_player_cards}")
                print(f"\tComputer's final hand: {computer_cards}, final score: {score(computer_cards)}")
                winner(player_cards, computer_cards)
                break
                
            if cards_busted(sum_of_player_cards):
                print(f"\tYour final hand: {player_cards}, final score: {sum_of_player_cards}")
                print(f"\tComputer's final hand: {computer_cards}, final score: {score(computer_cards)}")
                print("You went over. You lose")
                break
        begin_game()
    else:
        exit()

begin_game()
