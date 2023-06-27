import json

s = 'hi my name is navid and i want to test this string .'
lst_s = s.split()
d_letter = {}
d_word = {}
d = {}

for i in lst_s :
    # count every word in s
    if i not in d_word :
        d_word.update( {i : 1} )
    else :
        d_word[i] += 1


    for j in i :
        # count every letter in s
        if j not in d_letter :
            d_letter.update( {j : 1} )
        else :
            d_letter[j] += 1

# print(d_word)
# print(d_letter)

with open('D:\python_projects\Python\Training\string_counter\string_counter.json' , 'w') as f :
    json.dump(d_word , f , indent=2 , sort_keys=True)
    json.dump(d_letter , f , indent=2)
    print('string_counter.json created')