mainBoard = { "7" : " " , "8" : " " , "9" : " " ,
              "4" : " " , "5" : " " , "6" : " " ,
              "1" : " " , "2" : " " , "3" : " " }

location = []

#for loop to indicate that for every move made by the player, the value will change accordingly
for key in mainBoard:
    location.append(key)

#make a function to make the board automatically update after every move
def printBoard(board):
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["1"] + "|" + board["2"] + "|" + board["3"])

def game():

    global mainBoard
    turn = "X"
    count = 0


    for i in range(10):
        printBoard(mainBoard)
        print("Your turn," + turn + ". What's your move?")

        move = input()

        if mainBoard[move] == " ":
            mainBoard[move] = turn
            count += 1
        else:
            print("Invalid move, try another move")
            continue

    #check for the winner after every 5 moves
        if count >= 5:
            if  mainBoard["7"] == mainBoard["8"] == mainBoard["9"] != " ":
                printBoard(mainBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif mainBoard["4"] == mainBoard["5"] == mainBoard["6"] != " ":
                printBoard(mainBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif mainBoard["1"] == mainBoard["2"] == mainBoard["3"] != " ":
                printBoard(mainBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif mainBoard["1"] == mainBoard["4"] == mainBoard["7"] != " ":
                printBoard(mainBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif mainBoard["2"] == mainBoard["5"] == mainBoard["8"] != " ":
                printBoard(mainBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif mainBoard["3"] == mainBoard["6"] == mainBoard["9"] != " ":
                printBoard(mainBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif mainBoard["7"] == mainBoard["5"] == mainBoard["3"] != " ":
                printBoard(mainBoard)
                print("\nGame Over.\n")
                print("****" + turn + "won. ****")
                break
            elif mainBoard["1"] == mainBoard["5"] == mainBoard["9"] != " ":
                printBoard(mainBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        if turn == "X":
            turn = "O"
        else:
            turn = "X"

        if count == 9:
            print("\nGame Over.\n")
            print("Tie.")
            break

        

    restart = input("Do you want to play again? (Y or N): ")
    if restart == "y" or restart == "Y":
        for key in location:
            mainBoard[key] = " "

        game()

if __name__ == "__main__":
    game()