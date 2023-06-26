def get_row(x,i):
    result_list=list()
    desire_row=i
    for row in range(len(x[i])):
        if row == desire_row:
            for col in range(len(x[i])):
                result_list.append(x[row][col])
                # print(x[row][col])
            # result_list[index]=i
    return result_list
r=get_row([[1,2,3],[4,5,6],[7,8,9]],1)
print(r)

def get_column(x,i):
    result_list=list()
    desire_column=i
    for row in range(len(x)):
        result_list.append(x[row][desire_column])
    return result_list
r=get_column([[1,2,3],[4,5,6],[7,8,9]],1)
print(r)
