# Spelling A name using *
# Loop using For and If method is used
#Name to be used "Lay"

#Fixing the range of Columbs and Rows using i and j
Letter_L = [[" " for i in range (6)] for j in range (6)]
Letter_A = [[" " for i in range (6)] for j in range (6)]
Letter_Y = [[" " for i in range (6)] for j in range (6)]

# For L
for row in range (6):
    for col in range (5):
        if (col == 0) or (row == 5 or col == 0):
           Letter_L [row][col] = "*"

# For A
for row in range (6):
    for col in range (6):
     if (col == 0 and row > 0) or (col == 1 and row == 0) or (col == 1 and row == 3) or (col == 2 and row > 0):   
            Letter_A [row][col] = "*"

# For Y
for row in range (6):
    for col in range (6):
         if (col==2 and row>1) or (row==col and col<2) or (row==0 and col==4) or (row==1 and col==3):
            Letter_Y [row][col] = "*"

#fusing the letter to create the visual "LAY"
for j in range (6):
    for i in range (6):
        print(Letter_L[j][i], end = " ")
    print (end = "  ")
    for i in range (6):
        print (Letter_A[j][i], end = " ")
    print (end = "  ")
    for i in range (6):
        print (Letter_Y[j][i], end = " ")
    print (end = "  ")
    print ()