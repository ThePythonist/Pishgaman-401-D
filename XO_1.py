board = [ i for i in range(1,10) ]
table = '''
         {} | {} | {}
        -----------
         {} | {} | {}
        -----------
         {} | {} | {}
         '''.format(
    board[0],
    board[1],
    board[2],
    board[3],
    board[4],
    board[5],
    board[6],
    board[7],
    board[8],
)
print(table)

for i in range(9):
    choice = int(input("Enter any home : "))
    board[choice-1] = "X"
    table = '''
         {} | {} | {}
        -----------
         {} | {} | {}
        -----------
         {} | {} | {}
         '''.format(
    board[0],
    board[1],
    board[2],
    board[3],
    board[4],
    board[5],
    board[6],
    board[7],
    board[8],
    )
    print(table)
