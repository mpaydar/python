
# Function description:
# Signature function follows an algorithm which sort each list that represent a word in alphabetic order:
# Ascending order The algorithm will compare the current letter l, with all other letters
# on its right side The character comparison is done all in terms of their ASCI code.

# @parameters:
# n: individual word; type: string
def signature(n):
    lex_order = {}      # holding the word n(the word) in this dictionary for the initial design of this function
    letters = []       # holding all the character within the word n
    old_letter = ""   # holding the character which is being compared to all other characters on its right hand side
    for l in range(len(n)):
        letter = n[l]
        lex_order[l] = letter  # indexes are the key ; letters are the key; Example: {0:'A'}
    k = lex_order.values()     # Getting a dictionary object that include only the letters dic_val([A',...])
    for letter in k:           # iterating through the dictionary object and putting the values in the array "letters"
        letters.append(letter)

    # The sorting algorithm
    for l in range(len(letters)):
        next = l + 1
        old_letter += letters[l]
        for next_letter in range(next, len(letters)):
            # Comparison
            if letters[next_letter] < letters[l]:
                temp = letters[l]
                letters[l] = letters[next_letter]
                letters[next_letter] = temp
    # Edge case: if there was no swap , then the combination of all the old letters represent the same word n,
        # hence the same word will be returned
    if old_letter == n:
        return n

    return letters


a = signature("STOP")
print(a)
