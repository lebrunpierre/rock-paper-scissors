import game_utils
import random


def play_game():
    '''
    Plays the game and prints the results to the user
    :return:
    '''
    print('Welcome to "Rock Paper Scissors!')

    computer_choice = random.choice(list(asciiart.dict_rock_paper_scissors))

    # Makes sure players choice is valid
    player_choice = asciiart.check_user_input()

    # Prints out Ascii art for both player and computer
    print(f'Your choice: \n {asciiart.dict_rock_paper_scissors[player_choice]}')
    print(f'Computer choice: \n {asciiart.dict_rock_paper_scissors[computer_choice]}')

    # prints out the Winner
    print(asciiart.is_the_player_the_winner(player_choice, computer_choice))


# Continues to play the game
while True:
    play_game()
