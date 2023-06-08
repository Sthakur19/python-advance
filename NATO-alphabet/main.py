
import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

new_dict = { row.letter: row.code for (index, row) in data.iterrows()}



def generate_phonetic():
    enter_word = input("Enter the word : ").upper()
    try:
        new_list = [ new_dict[word] for word in enter_word]
    except KeyError:
        print('Its not alphabet')
        generate_phonetic()
    else:
        print(new_list)
    
generate_phonetic()