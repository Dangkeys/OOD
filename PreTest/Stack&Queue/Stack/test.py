word = '-512'
print(word.isdigit() or (word[0] == '-' and word[1:].isdigit()))