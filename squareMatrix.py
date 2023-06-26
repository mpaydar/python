
# The function returns a list containing the ith row in the matrix
def get_row(x, i):
    # x: the 2d array; i: the ith row in the matrix
    result_list = list()
    desire_row = i
    for row in range(len(x[i])):
        if row == desire_row:
            for col in range(len(x[i])):
                result_list.append(x[row][col])
    return result_list


r = get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
print("The ith-row include the following integers: ",r)
print("-------------------------------------------------")

# The function returns a list containing the ith row in the matrix
def get_column(x, i):
    # x: the 2d array; i: the ith row in the matrix
    result_list = list()
    desire_column = i
    for row in range(len(x)):
        result_list.append(x[row][desire_column])
    return result_list


r = get_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
print("The ith-column include the following integers: ",r)
print("----------------------------------------------")

# Getting the sum of numbers that lie on the main diagonal
def diagonal_sum(x):
    diag_sum = 0    # sum variable
    temp_list=list()  # a temporary list to aggregate the numbers on the diagonal(just for inspection purpose)
    for row in range(len(x)):
        for col in range(len(x)):
            if row == col: # crucial condition; for a 3X3 matrix diagonal coordinates are 0,0;1,1;2,2; hence the column and row are equals
                diag_sum = x[row][col]+diag_sum
                temp_list.append(x[row][col])
    return diag_sum,temp_list


sum,dia_elements=diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])   #unpacking

print("Numbers on the main diagonal: ", end=" ")
[print(dia_elements[i],end=" ") for i in range(len(dia_elements))]
print("")
print("Top Left to Lower Right summation :",sum)
print("----------------------------------------------")

def diagonal_sumRL(x):
    diag_sum=0
    temp_list=list()
    temp_start=len(x)-1
    for row in range(len(x)):
        for col in range(0,1):
            # print(x[row][temp_start])
            diag_sum=diag_sum+x[row][temp_start]
            temp_list.append(x[row][temp_start])
            temp_start=temp_start-1

            break
    return diag_sum,temp_list

sum,diag_elem=diagonal_sumRL([[1, 2, 3], [4, 5, 6], [7, 8, 9]])   #unpacking
print("Numbers on the alternate diagonal(Top right to bottom left): ", end=" ")
[print(diag_elem[i], end=" ") for i in range(len(diag_elem))]
print("")
print("Top Right to lower left summation: ",sum)