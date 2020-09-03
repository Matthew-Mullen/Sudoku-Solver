def solver(board):
    empty=find_empty(board)
    # if we have no emptys left that means the job is done and we have filled in the board and validated it
    if not empty:
        return True
    else:
        row,col=empty
    for num in range(1,len(board)+1):
        if validate(board,num,(row,col)):
            board[row][col]=num
            if solver(board):
                return True
            # resets the board
            board[row][col]=0
    return False

                
def validate(board,num,position):
    # num is from our for loop in solver, position is our tuple from find empty
    # need to check each row,col to see if it placing num at our pos breaks the row or col
    
    # check col
    for i in range(len(board)):
        # checks if we find another row in the given col from our position that already has that number
        # then validates that we aren't just marking the number that already exists
        if board[i][position[1]]==num and position[0]!=i:
            return False
    
    # now check row
    for i in range(len(board[0])):
        # similar to above but for cols
        if board[position[0]][i]==num and position[1]!=i:
            return False
        
    # now check the box to make sure it is a valid placement (the 3x3 subgrid)
    x_box=position[1]//3
    y_box=position[0]//3
    # first for loop checks the row of box second one checks the col of box
    for i in range(y_box*3,y_box*3 +3):
        for j in range(x_box*3,x_box*3 +3):
            if board[i][j]==num and position!=(i,j):
                return False
    return True
        
        
def find_empty(board):
    # Finds a row,col in the board that has a 0 (empty spot on board)
    for m in range(len(board)):
        for n in range(len(board[0])):
            if board[m][n]==0:
                return m,n
    return None
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0:
            if i == 0:
                print(" ┎─────────┰─────────┰─────────┒")
            else:
                print(" ┠─────────╂─────────╂─────────┨")

        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" ┃ ", end=" ")

            if j == 8:
                print(board[i][j], " ┃")
            else:
                print(board[i][j], end=" ")

    print(" ┖─────────┸─────────┸─────────┚")





