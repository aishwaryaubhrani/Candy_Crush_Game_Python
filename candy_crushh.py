import random
import sys

sys.setrecursionlimit(10 ** 6)
score = 0
row_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
col_names = ['0', '1', '2', '3', '4']
colors = ['R', 'G', 'B', 'W', 'BL']
candy_matrix = [['R', 'R', 'R', 'G', 'B'],
                ['G', 'W', 'BL', 'G', 'B'],
                ['W', 'B', 'B', 'BL', 'B'],
                ['B', 'W', 'G', 'B', 'BL'],
                ['W', 'W', 'W', 'R', 'W'],
                ['BL', 'B', 'G', 'G', 'G'],
                ['W', 'R', 'R', 'BL', 'R'],
                ['B', 'W', 'W', 'W', 'G'],
                ['B', 'B', 'B', 'G', 'BL']]


def reshuffle_candies():
    for i in range(0, 9):
        for j in range(0, 5):
            new_color = random.randint(0, 4)
            candy_matrix[i][j] = colors[new_color]

    print_candy_matrix()
    crush_candy()


def print_candy_matrix():
    print(" ", end=" ")
    for k in col_names:
        print(k, end = " ")
    print()
    for i in range(0, 9):
        print(row_names[i], end = " ")
        for j in range(0, 5):
            print(candy_matrix[i][j], end=" ")
        print()
        

def replace_candies(row, col, match):
    if(row == 0):
        for i in range(match):
            new_color = random.randint(0, 4)
            candy_matrix[row][col+i] = colors[new_color]
        print()
        print_candy_matrix()
    else:
        for i in range(match):
            prev_color = candy_matrix[row-1][col+i]
            candy_matrix[row][col+i] = prev_color
            new_color = random.randint(0, 4)
            candy_matrix[row-1][col+i] = colors[new_color]
        print()
        print_candy_matrix()


def crush_candy():
    global score
    for i in range(0, 9):
        for j in range(0, 3):
            match = 1
            for k in range(j+1, 5):
                if(candy_matrix[i][j] == candy_matrix[i][k]):
                    match+=1
                    if(k == 4 and match>=3):
                        replace_candies(i, j, match)
                        score += 1
                        print("Score:", score)


                elif(match>=3):
                    if(match>=3):
                        replace_candies(i, j, match)
                        score += 1
                        print("Score:", score)
                    break

    swap_candies()


def swap_candies():
    print("Press 1 to swap and 2 to reshuffle and 3 to exit")
    choice = int(input())
    if(choice == 1):
        print("Please enter the locations to swap candies?")
        row_num = int(input("Please enter the row num: "))
        col_num1 = int(input("Please enter the col num 1:"))
        col_num2 = int(input("Please enter col num 2:"))

        if(col_num1+1 == col_num2 or col_num2+1 == col_num1):
            candy_matrix[row_num][col_num1], candy_matrix[row_num][col_num2] = candy_matrix[row_num][col_num2], candy_matrix[row_num][col_num1]
            crush_candy()
        else:
            print("Please enter a valid col number")
            return swap_candies()
    elif(choice == 2):
        reshuffle_candies()
    elif(choice == 3):
        exit()
    else:
        print("Please enter a valid choice")
        swap_candies()




    

crush_candy()
