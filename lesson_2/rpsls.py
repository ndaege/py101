import random

valid_choices = {
    'r':'rock', 
    'p':'paper', 
    'sc':'scissors', 
    'l':'lizard', 
    'sp':'spock'
}

def display_choices():
    choice_list = []
    for key, value in valid_choices.items():
        choice_list.append(f'"{key}" for {value}')
    
    return choice_list

def prompt(message):
    print(f'==> {message}')
    
def determine_winner(player, computer):
    if ((player == 'sc' and computer == 'p') or 
        (player == 'p'and computer == 'r') or
        (player == 'r' and computer == 'l') or
        (player == 'l' and computer == 'sp') or 
        (player == 'sp' and computer == 'sc') or
        (player == 'sc' and computer == 'l') or 
        (player == 'l' and computer == 'p') or 
        (player == 'p' and computer == 'sp') or
        (player == 'sp' and computer == 'r') or 
        (player == 'r' and computer == 'sc')):
        return "player"
    elif ((computer == 'sc' and player == 'p') or
        (computer == 'p'and player == 'r') or
        (computer == 'r' and player == 'l') or
        (computer == 'l' and player == 'sp') or 
        (computer == 'sp' and player == 'sc') or
        (computer == 'sc' and player == 'l') or 
        (computer == 'l' and player == 'p') or 
        (computer == 'p' and player == 'sp') or
        (computer == 'sp' and player == 'r') or 
        (computer == 'r' and player == 'sc')):
        return "computer"
    
def display_winner(winner):
    if winner == "player":
        prompt('You win!')
    elif winner == "computer":
        prompt('Computer wins!')
    else:
        prompt("It's a draw!")
        
def count_wins(winner):  
    global player_wins
    global computer_wins
    if winner == "player":
        player_wins += 1
    elif winner == "computer":
        computer_wins += 1
    else:
        pass
    
    if player_wins == 3:
        prompt("You won 3 rounds, you win the game.")
    elif computer_wins == 3:
        prompt("The computer won 3 rounds, you lose the game.")
             
player_wins = 0
computer_wins = 0            
while True:
    prompt(f'Choose one: {", ".join(display_choices())}')
    # ask user for input and perform input validation 
    choice = input()

    while choice not in valid_choices.keys():
        prompt("That's not a valid choice")
        choice = input()
        
    computer_choice = random.choice(list(valid_choices.keys()))
    
    the_winner = determine_winner(choice, computer_choice)
    
    display_winner(the_winner)

    prompt(f'You chose {valid_choices[choice]}, computer chose {valid_choices[computer_choice]}')
    
    if count_wins(the_winner):
        break
    
    prompt('Do you want to play again? (y/n)?')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        
        prompt('Please enter "y" or "n".')
        answer = input().lower()
    
    if answer[0] == 'n':
        break