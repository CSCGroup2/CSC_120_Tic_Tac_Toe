board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

for row in board:
    print(row)

user = True # when true it refers to x, otherwise o
turns = 0

def quit(user_input):
    if user_input.lower() == "q":
       print("Thanks for playing")
       return True
    else: return False

def check_input(user_input):
# check if it's a number
  if not isnum(user_input): return False
  user_input=int(user_input)
# check if it's 1 - 9
  if not bounds(user_input): return False
  return True

def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else: return True

def bounds(user_input):
    if user_input > 9 or user_input < 1:
        print("This number is out of bounds")
        return False
    else: return True

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This position is already taken.")
        return True
    else: return False

def coordinates(user_input):
    row = int(user_input/3)
    col = user_input
    if col > 2: col = int (col %3)
    return(row,col)

def add_to_board(coords,board,active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

def current_user(user):
    if user: return "x"
    else: return "o"


