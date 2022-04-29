

def iswin(user, board):
    if check_row(user, board): return True
    if check_col(user, board): return True
    if check_diag(user, board): return True
    return False

def check_diag(user, booard):
    if board[0][0] == user and board[1][1] == user and board [2][2] == user: return True
    elif board[0][2] == user and board[1][1] and board[2][0] == user: return True
    else: return False

def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row: return True
    return False

def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col: return True
    return False

while turns <9:
    active_user = current_user(user)
    user_input = input("Please enter a position 1 through 9 or enter\"q\" to quit:")
    if quit(user_input): break
    if not check_input(user_input):
        print("Please try again.")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if istaken(coords,board):
      print("Please try again.")
      continue
    add_to_board(coords,board,active_user)
    if iswin(active_user, board):
        print(f"{active_user.upper()} won!")
        break

    turns += 1
    if turns ==9: print ("Tie!")
    user = not user


