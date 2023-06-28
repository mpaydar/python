def signature(n):
    lex_order={}
    letters=[]
    old_letter=""
    for l in range(len(n)):
        letter=n[l]
        lex_order[l]=letter
    k=lex_order.values()
    for letter in k:
        letters.append(letter)
    for l in range(len(letters)):
        next=l+1
        old_letter+=letters[l]
        for next_letter in range(next,len(letters)):
            if letters[next_letter] < letters[l]:
                temp=letters[l]
                letters[l]=letters[next_letter]
                letters[next_letter]=temp
    if old_letter == n:
        return n

    return letters

def convert_letter(lt):
    container=[]
    string_word = ""
    for word in lt:
        for l in word:
            string_word+=l
        container.append(string_word)
        string_word=""
    return container







# a=signature("STOP")
# b=convert_letter(a)
# print(b)