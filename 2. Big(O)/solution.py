#  Created by Elshad Karimov on 3/26/20.
#  Copyright © 2020 Elshad Karimov. All rights reserved.

################ Interview Questions #############
#Question1
def foo(array):
    sum = 0                                                 #   -> O(1)
    product = 1                                             #   -> O(1)
    for i in array:                                         #   -> O(n)
        sum += i                                            #   -> O(1)
    for i in array:                                         #   -> O(n)
        product *= i                                        #   -> O(1)
    print("Sum = "+str(sum)+", Product = "+str(product))    #   -> O(1)

ar1 = [1,2,3,4]                                             #   -> O(1)
foo(ar1)                                                    #   ------------->  O(n)


#Question2

def printPairs(array):
    for i in array:                         # -> O(n^2)
        for j in array:                     # -> O(n)
            print(str(i)+","+str(j))        # -> O(1)
                                            # --------------------------> O(n^2)

#Question3
def printUnorderedPairs(array):
    for i in range(0,len(array)):                   # -> O(n^2)
        for j in range(i+1,len(array)):             # -> O(n)
            print(array[i] + "," + array[j])        # -> O(1)
                                                    # -----------------------> O(n^2)




#Question4
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):                                    # -> O(m)
        for j in range(len(arrayB)):                                # -> O(n)
            if arrayA[i] < arrayB[j]:                               # -> O(1)
                print(str(arrayA[i]) + "," + str(arrayB[j]))        # -> O(1)
                                                                    # ----------------------> O(mn)
arrayA = [1,2,3,4,5]
arrayB = [2,6,7,8]



#Question5
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):                                    # -> O(m)
        for j in range(len(arrayB)):                                # -> O(n)
            for k in range(0,100000):                               # -> O(1)
                print(str(arrayA[i]) + "," + str(arrayB[j]))        # -> O(1)
                                                                    # -----------------------> O(mn)
# printUnorderedPairss(arrayA,arrayB)


#Question6
def reverse(array):
    for i in range(0,int(len(array)/2)):        # -> O(n)
        other = len(array)-i-1                  # -> O(1)
        temp = array[i]                         # -> O(1)
        array[i] = array[other]                 # -> O(1)
        array[other] = temp                     # -> O(1)
    print(array)                                # -> O(1)
                                                # -----------------------> O(n)
reverse(arrayA)

