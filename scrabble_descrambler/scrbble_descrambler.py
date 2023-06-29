import signature

def read_file():
    file_letters = []
    with open("wordlist.txt", 'r') as file:
        for line in file:
            line=line.rstrip("\n")
            file_letters.append(line)

    return file_letters


def convert_letter(lt):
    string_word = ""
    for word in lt:
        for l in word:
            string_word += l
    return string_word


def generate_tuple_list(word_list):
    signature_tuples = []
    s = []
    for i in range(len(word_list)):
        lex_order = signature.signature(word_list[i])
        lex_string=convert_letter(lex_order)
        signature_tuples.append((lex_string,word_list[i]))
    return signature_tuples

def directory_populating(tuple_list):
    word_directory={}
    for tuples in tuple_list:
        if tuples[0] not in word_directory:
            word_directory[tuples[0]]=[tuples[1]]
        else:
            word_directory[tuples[0]].append(tuples[1])
    return word_directory



original_voc = read_file()
tuples = generate_tuple_list(original_voc)
print(tuples[2][0])      # signature element of the tuple    (0=signature,1=actual_word)
d=directory_populating(tuples)
print(d)
