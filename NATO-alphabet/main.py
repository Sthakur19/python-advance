
import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')

new_dict = { row.letter: row.code for (index, row) in data.iterrows()}

enter_word = input("Enter the word : ").upper()

new_list = [ new_dict[word] for word in enter_word]

print(new_list)
