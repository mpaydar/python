import signature
import pickle
import os
word_directory = {}


def read_file():
    file_letters = []
    with open("wordlist.txt", 'r') as file:
        for line in file:
            line = line.rstrip("\n")
            file_letters.append(line)

    return file_letters


def serializing(word_dictionary):
    x2=word_directory
    with open("dictionary.pkl", "wb") as file:
        pickle.dump(word_dictionary, file)


def deserializing():
    with open("dictionary.pkl", "rb") as file:
        return pickle.load(file)


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
        lex_string = convert_letter(lex_order)
        signature_tuples.append((lex_string, word_list[i]))
    return signature_tuples


def directory_populating(tuple_list):
    # word_directory = {}
    for tuples in tuple_list:
        if tuples[0] not in word_directory:
            word_directory[tuples[0]] = [tuples[1]]
        else:
            word_directory[tuples[0]].append(tuples[1])
    return word_directory


def filter_dictionary(words_director):
    word_signature = words_director.items()  # each item is (signature,values)
    temp_list = []
    filtered_list = []
    print("Number of words before filter: ", len(word_signature))
    for words_tuple_index in word_signature:
        temp_list.append(words_tuple_index)
    for index in range(len(temp_list)):
        if len(temp_list[index][0]) == 6:
            filtered_list.append(temp_list[index])
    print("Number of words after filter: ", len(filtered_list))
    # print(temp_list[0:11])
    # print(filtered_list[0:11])
    return filtered_list


def generate_dictionary(word_list):
    filtered = dict()
    for w_index in range(len(word_list)):
        filtered[word_list[w_index][0]] = word_list[w_index][1]

    return filtered


def directory_lookup(user_input,filtered_words):
    return filtered_words[user_input]

def controller():
    if os.path.exists("dictionary.pkl"):
        # Load the pickled data from "dictionary.pkl"
        filtered_list = deserializing()
        result=generate_dictionary(filtered_list)
        user_input = input("Enter six letters (without any space) to see all the words containing these letters: ")
        user_input_lexOrder = signature.signature(user_input)

        user_input_lexOrder = convert_letter(user_input_lexOrder)
        user_respond = directory_lookup(user_input_lexOrder,result)
        print("Here's the list of possible words you may use with the 6 letters you have provided: ", user_respond)


    else:
        original_voc = read_file()
        tuples = generate_tuple_list(original_voc)
        # print(tuples[2][0])  # signature element of the tuple    (0=signature,1=actual_word)
        noFiltered_directory = directory_populating(tuples)
        filtered_tuples = filter_dictionary(noFiltered_directory)
        filtered_dictionary = generate_dictionary(filtered_tuples)
        print(filtered_dictionary)
        user_input = input("Enter six letters (without any space) to see all the words containing these letters: ")
        user_input_lexOrder = signature.signature(user_input)
        # print(type(user_input_lexOrder))

        user_input_lexOrder = convert_letter(user_input_lexOrder)
        user_respond = directory_lookup(user_input_lexOrder,filtered_dictionary)
        print("Here's the list of possible words you may use with the 6 letters you have provided: ", user_respond)

controller()