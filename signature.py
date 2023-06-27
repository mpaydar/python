def signature(n):
    lex_order={}
    letters=[]
    for l in range(len(n)):
        letter=n[l]
        lex_order[letter]=l
    k=lex_order.keys()
    for letter in k:
        letters.append(letter)
    for l in range(len(letters)):
        next=l+1
        for next_letter in range(next,len(letters)):
            if letters[next_letter] < letters[l]:
                temp=letters[l]
                letters[l]=letters[next_letter]
                letters[next_letter]=temp
    print(letters)

signature("kbda")