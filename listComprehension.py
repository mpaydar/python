
n=[2,3,4,5,6,7,8,9,10]

def prime_check(prime_array):
    prime_dic={}
    for p in range(len(prime_array)):
        current_number=prime_array[p]
        for x in range(1,current_number+1):
            if current_number % x == 0 and (x!=current_number) and x!=1:
                del prime_dic[current_number]
                break
            else:
                prime_dic[current_number]="prime"
    print(prime_dic)





# prime_check(n)







