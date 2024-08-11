from random import randrange

board = [[str(i+j) for i in range(1,4)] for j in range(0,9,3)]
player = "X"

#Mostrar board de juego
def display_board(board):
    for i in range(len(board)):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   "+"   |   ".join((board[i]))+"   |")
        print("|       |       |       |")
    else:
        print("+-------+-------+-------+")
        
#validar cambos vacios
def make_list_of_free_fields(board):
    emptyfields = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != "X" and board[i][j] != "O":
                emptyfields.append(board[i][j])
    return emptyfields

#Funcion de ingreso de movimiento 
def enter_move():
    global player
    move = ""
    fields = make_list_of_free_fields(board)
    if player == "X":
        while move not in fields:
            move = str(randrange(1,10))
        for i in range(len(board)):
            try:
                field = board[i].index(move) 
                board[i][field] = "X"
            except:
                continue
        player = "O"
    else:
        while True:
            move = input("Ingrese el numero donde quiere hacer su movimiento: ")
            if move not in fields:
                print("Ingrese un movimiento valido")
            else:
                break
        for i in range(len(board)):
            try:
                field = board[i].index(move) 
                board[i][field] = "O"
            except:
                continue
        player = "X"
        
        
#funcion para definir ganador
def victory_for():
    victory = False
    #validar filas
    for i in range(len(board)):
        first = board[i][0]
        for j in range(len(board[i])):
            if all(first == element for element in board[i]):
                victory = True
                return victory     
    #validar columnas
    for i in range(len(board)):
        columns=[]
        first = board[i][i]
        for j in range(len(board[i])):
            columns.append(board[j][i])
        if all(first == element for element in columns):
            victory = True
            return victory 
    #validar diagonales
    diagonal=[]
    for i in range(len(board)):
        first = board[i][i]
        diagonal.append(board[i][i])
    if all(first == element for element in diagonal):
        victory = True
        return victory 
    diagonal = []
    first = board[2][0]
    for i in range(len(board[i])-1,-1,-1):
        for j in range((len(board[i])-1)-i,len(board[i])-i,1):
            diagonal.append(board[j][i])
    if all(first == element for element in diagonal):
        victory = True
        return victory 
          
#ciclo del juego   
while True:
    while player == "X":
        enter_move()
        display_board(board)
    winner = victory_for()
    if winner:
        print("Machine wins")
        break
    
    while player == "O":
        enter_move()
        display_board(board)
    winner = victory_for()
    if winner:
        print("You win")
        break