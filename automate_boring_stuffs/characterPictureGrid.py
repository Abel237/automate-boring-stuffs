grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def reformat(griddle):  # I understand this part thanks to /u/-Cubie-
    # I understand the ' for i in range ' portion.
    for i in range(0, len(griddle[0])):
        myStr = ''  # sets my string = '' or null
        for j in range(0, (len(griddle))):
            myStr += griddle[j][i]
        print(myStr)  # I understand this part as well.
