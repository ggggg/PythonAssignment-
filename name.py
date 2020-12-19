print('Enter your name:')
string = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
print('In reverse:', str.join('', list(reversed(string))))
print('Number of vowels:', len(list(filter(vowels.__contains__, string))))
