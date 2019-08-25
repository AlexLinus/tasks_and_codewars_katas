def validSolution(board):
    result_list = []
    result = True

    #for lines
    for line in board:
        if len(set(line)) == 9:
            result_list.append('True')
        else:
            result_list.append('False')
    #for rows
    for line in list(zip(*board)):
        if len(set(line)) == 9:
            result_list.append('True')
        else:
            result_list.append('False')
    first_part_lines, second_part_lines, third_part_lines = board[:3], board[3:6], board[6:]

    def block_validator(block):
        first_part = third_part = second_part = []
        first_part.extend(block[0][:3])
        first_part.extend(block[1][:3])
        first_part.extend(block[2][:3])
        second_part.extend(block[0][3:6])
        second_part.extend(block[1][3:6])
        second_part.extend(block[2][3:6])
        third_part.extend(block[0][6:])
        third_part.extend(block[1][6:])
        third_part.extend(block[2][6:])

        if len(set(first_part)) and len(set(second_part)) and len(set(third_part)) == 9:
            return 'True'
        else:
            return 'False'

    result_list.append(block_validator(first_part_lines))
    result_list.append(block_validator(second_part_lines))
    result_list.append(block_validator(third_part_lines))

    if 'False' not in result_list:
        result = True
    else:
        result = False
    return result



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #assert checkio(4) == 1
    assert validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                      [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]) == True

    assert validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                      [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                      [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                      [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                      [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                      [3, 0, 0, 4, 8, 1, 1, 7, 9]]) == False