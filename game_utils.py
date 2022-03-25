# asciiart

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

dict_rock_paper_scissors = {1: rock, 2: paper, 3: scissors}


def is_the_player_the_winner(player, computer):
    '''

    :param player: user input
    :param computer: computer input
    :return: bool

    Evaluates if player wins.
    returns true if thy did false if the did not
    '''

    if player == 1 and computer == 3:
        return "Winner"

    elif player == 2 and computer == 1:
        return "Winner"

    elif player == 3 and computer == 2:
        return "Winner"

    elif player == computer:
        return "Draw"

    else:
        return "lost this round"


def check_user_input(player_choice= 0):
    '''

    :param player_choice: input from player
    :return: new player input

    Will make sure player is choosing predefined values
    '''

    while True:
        if player_choice not in dict_rock_paper_scissors:
            player_choice = int(input("Please choose 1(rock), 2(paper), or 3 (scissors): "))
        else:
            return player_choice