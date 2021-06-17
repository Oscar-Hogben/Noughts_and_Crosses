
# shoppingList = [
#     "cheese",
#     "bacon",
#     "orange",
#     "god"
# ]

# print(shoppingList[1])

# shoppingList.append("chickens")

# print(shoppingList)

# itemRemove = input("What item would you like to remove?: ")

# shoppingList.remove(itemRemove)

# print(shoppingList)


# Check for a draw,

emptySpace = "-"

grid = [
    [emptySpace, emptySpace, emptySpace],
    [emptySpace, emptySpace, emptySpace],
    [emptySpace, emptySpace, emptySpace]
]

def printGrid():
    print()
    print(grid[0][0], grid[0][1], grid[0][2])
    print(grid[1][0], grid[1][1], grid[1][2])
    print(grid[2][0], grid[2][1], grid[2][2])
    print()

def checkWin():
    # Row 1
    if grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2] and grid[0][0] != emptySpace:
        return grid[0][0]
    # Row 2
    elif grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2] and grid[1][0] != emptySpace:
        return grid[1][0]
    # Row 3
    elif grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2] and grid[2][0] != emptySpace:
        return grid[2][0]
    # Diagonal left top to right bottom
    elif grid[0][0] == grid[1][1] and grid[0][1] == grid[2][2] and grid[0][0] != emptySpace:
        return grid[0][0]
    # Diagonal right top to left bottom
    elif grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[0][2] != emptySpace:
        return grid[0][2]
    # Colomn 3
    elif grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2] and grid[0][2] != emptySpace:
        return grid[0][2]
    # Colomn 2
    elif grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1] and grid[0][1] != emptySpace:
        return grid[0][1]
    # Colomn 1
    elif grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0] and grid[0][0] != emptySpace:
        return grid[0][0]
    
    # No one has won
    return False



crossGo = False

while True:
    crossGo = not crossGo

    invalidInput = True

    while invalidInput:

        col = int(input("What column would you like your piece in?: "))
        row = int(input("What row would you like your piece in?: "))

        if grid[row-1][col-1] != emptySpace:
            print("That space is already taken!")

        else:
            invalidInput = False
    

    if crossGo: 
        grid[row-1][col-1] = "X"
    else:
        grid[row-1][col-1] = "O"

    win = checkWin()

    printGrid()

    if win:
        print(win, "is the winner!")
        break

