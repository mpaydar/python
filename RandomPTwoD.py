
import random

columns = int(input("Enter number of rows (n): "))
rows = int(input("Enter number of columns (m): "))
n3 = int(input("Enter second number (m): "))
x=columns*rows

if n3>x:
    my_list=[[0 for col in range(columns)] for r in range(rows)]
    for row in range(rows):
        for column in range(columns):
            current_element=my_list[row][column]
            rand_num = random.randrange(1, n3)
            print(rand_num)
            if rand_num not in my_list[row]:
                while (rand_num in my_list[row]):
                    rand_num=random.randrange(1,n3)
                    current_element = my_list[row][column]
            else:
                while (rand_num in my_list[row]):
                    rand_num = random.randrange(1, n3)
                    current_element = my_list[row][column]
            my_list[row][column]=rand_num
    print(my_list)
