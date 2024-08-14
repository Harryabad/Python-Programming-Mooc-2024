# Write your solution here
def who_won(gameboard: list):

    player_one_spaces = 0
    player_two_spaces = 0

    for row in gameboard:
        for value in row:

            if value == 1:
                player_one_spaces += 1
            elif value == 2:
                player_two_spaces += 1
    

    #print(player_one_spaces)
    #print(player_two_spaces)
    if player_one_spaces > player_two_spaces:
        return 1
    elif player_two_spaces > player_one_spaces:
        return 2
    elif player_one_spaces == player_two_spaces:
        return 0
    
if __name__ == "__main__":
    gameboard = [[1, 2, 1], [0, 0, 1], [2, 1, 0]]
    print(who_won(gameboard))