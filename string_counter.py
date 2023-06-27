import json

s = 'hi my name is navid and i want to test this string this code shows you how many letters and words you type i dont know what i write but i should write somthing and how are you what are you doing what happend yesterday i hope you like me.'
lst_s = s.split()
len_all_words = len(lst_s)
d_letter = {}
d_word = {}
d = {}
len_all_letters = 0

for i in lst_s :
    # count every word in s
    if i not in d_word :
        d_word.update( {i : 1} )
    else :
        d_word[i] += 1


    for j in i :
        # count every letter in s
        len_all_letters += 1
        
        if j not in d_letter :
            d_letter.update( {j : 1} )
        else :
            d_letter[j] += 1

# print(d_word)
# print(d_letter)

d = {
    'all words' : len_all_words,
    'all letters' : len_all_letters,
    'd_letter' : d_letter,
    'd_word' : d_word
}


with open('D:\python_projects\Python\Training\string_counter\string_counter.json' , 'w') as f :
    json.dump(d , f , indent=4 , sort_keys=True)
    print('string_counter.json created')