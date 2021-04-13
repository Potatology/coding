from string import ascii_letters

wordlist = ['sold', 'dolf', 'bold', 'good']
word = 'gold'


for i in range(len(word)):
    for c in ascii_letters:
        if word[:i] + c + word[i + 1:] in wordlist:
            print(word[:i] + c + word[i + 1:])


