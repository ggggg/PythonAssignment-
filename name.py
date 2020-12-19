# get the string
print('Enter your name:')
string = input()
# all the vowels
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
# reverse the string and output results
print('In reverse:', str.join('', list(reversed(string))))
# count all the vowels
print('Number of vowels:', len(list(filter(vowels.__contains__, string))))
