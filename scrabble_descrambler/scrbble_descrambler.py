import signature


def read_file():
    file_letters = []
    with open("wordlist.txt", 'r') as file:
        for line in file:
            file_letters.append(line)

    string_result=signature.convert_letter(file_letters)
    return string_result


def generate_tuple_list(word_list):
    signature_tuples = []
    for i in word_list:
        s = signature.signature(i)
        signature_tuples.append((s, i))
    print(signature_tuples)
    return signature_tuples


def output_tuples(tuples):
    for i in tuples:
        print(i)
        print("")
    print(i[1])


w = read_file()

tuples = generate_tuple_list(w)
print(tuples[0])