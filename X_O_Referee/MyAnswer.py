def checkio(game_result):
    #creates a list of vertical columns as strings
    vert_game_result = []
    for i in range(0,3):
        column = ''.join([x[i] for x in game_result])
        vert_game_result.append(column)

    #adds strings that represent the diagonal columns
    vert_game_result.append(''.join([x[i] for i in range(0,3) for x in game_result if  game_result.index(x) == i]))
    vert_game_result.append(''.join([x[i] for i in range(0,3) for x in game_result if game_result.index(x) + i == 2]))

    #for i in range(0,2) for x in game_result
    #adds the strings representing veritcal and diagonal squares to the game results
    game_result[3:3] = vert_game_result

    #if any of the strings in the array come out as the same and is not representing three empty tiles return that character
    winner = [x for x in game_result if x == len(x) * x[0] and x[0] != "."]
    if len(winner) > 0:
        return winner[0][0]
    return "D"
