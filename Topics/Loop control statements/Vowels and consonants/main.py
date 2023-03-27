vowels = 'aeiou'

for char in input():
    if char.isalpha() is False:
        break
    if char in vowels:
        print('vowel')
    else:
        print('consonant')
