# Given 2D list calculate the sum of diagonal elements.

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 

def diagonalSum(matrice):
    sum = 0
    for i in range(len(matrice)):
        sum += matrice[i][i]
    return sum
 
print(diagonalSum(myList2D)) # 15