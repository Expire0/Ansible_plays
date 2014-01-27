pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    if first in 'aeiou':
        new_word = word[0:]+"ay"
        print new_word
    else:
        new_word = word[1:]+word[0]+"ay"
        print new_word
else:
    print 'You must enter a alpha word, or how am I suppose to translate. I am only a computer'
