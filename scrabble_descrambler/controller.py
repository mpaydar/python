import scrbble_descrambler as sc
import os


def controller():
    if os.path.exists("dictionary.pkl"):
        # Load the pickled data from "dictionary.pkl"
        filtered_list = sc.deserializing()
        user_input = input("Enter six letters (without any space) to see all the words containing these letters: ")
        user_input_lexOrder = sc.signature.signature(user_input)

        user_input_lexOrder = sc.convert_letter(user_input_lexOrder)
        user_respond = sc.directory_lookup(user_input_lexOrder)
        print("Here's the list of possible words you may use with the 6 letters you have provided: ", user_respond)


    else:
        original_voc = sc.read_file()
        tuples = sc.generate_tuple_list(original_voc)
        # print(tuples[2][0])  # signature element of the tuple    (0=signature,1=actual_word)
        noFiltered_directory = sc.directory_populating(tuples)
        filtered_tuples = sc.filter_dictionary(noFiltered_directory)
        filtered_dictionary = sc.generate_dictionary(filtered_tuples)

        # print(filtered_dictionary)
        user_input = input("Enter six letters (without any space) to see all the words containing these letters: ")
        user_input_lexOrder = sc.signature.signature(user_input)
        # print(type(user_input_lexOrder))

        user_input_lexOrder = sc.convert_letter(user_input_lexOrder)
        user_respond = sc.directory_lookup(user_input_lexOrder)
        print("Here's the list of possible words you may use with the 6 letters you have provided: ", user_respond)
