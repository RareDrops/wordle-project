"""
This program checks for a string input of a user and checks it against the word list in the game "wordle" if it matches any word described in the input.
Two optional flags can be used such as _ if the letter(indicated by gray background) is unknown and * after a letter to indicate it's a correct positioned letter(inddicated by a green background).
Otherwise just enter the word as normal.
"""
with open("data.txt",'r') as word_data:
    word_data = word_data.read()
    word_list_unrefined = word_data.split(',')
    word_list_refined = (word[1:-1] for word in word_list_unrefined)


valid_entries = []
correct_position_index_list = []
correct_position_letter_list = []
user_input = str(input("Enter your guessed letters so far(Use _ for unknown letters, use * after the letter if the letter is in the correct position): "))
letters_to_exclude = str(input("Enter letters  to exclude(nospace): "))
index = user_input.find("*")
while index != -1:
    correct_position_index_list.append(index-1) #append the character before "*"
    correct_position_letter_list.append(user_input[index-1])
    user_input = user_input[:index] + user_input[index+1:] #removing "*"
    index = user_input.find("*")

#checking for words with correct position
if correct_position_letter_list != []:
    for word in word_list_refined:
        if all((index, letters) in enumerate(word) for (index, letters) in zip(correct_position_index_list,correct_position_letter_list)):
            valid_entries.append(word)

#ignoring the _ on the input
user_input = user_input.replace('_',"")

#checking for words in no correct position
if correct_position_letter_list ==  []:
    for word in word_list_refined:
        if all(letters in word for letters in user_input):
            valid_entries.append(word)
else:
    #to be fixed
    for word_index in range(len(valid_entries)-1,-1,-1):
        word = valid_entries[word_index]
        if all(letter in word for letter in user_input):
            pass
        else:
            valid_entries.pop(word_index)

#checking for excluded/used letters
for word_index in range(len(valid_entries)-1,-1,-1):
    word = valid_entries[word_index]
    for letter  in word:
        if letter in letters_to_exclude:
            valid_entries.pop(word_index)
            break

print(valid_entries)
        


    


