s = 'hi my name is navid and i want to test this string .'
lst_s = s.split()
d_letter = {}
d_word = {}

print(lst_s)

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

print(d_word)
print(d_letter)