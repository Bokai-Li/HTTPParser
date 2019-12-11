import re
absoluteFilePath = re.compile('[\w./]')
word = input()

matches = absoluteFilePath.search(word)

print(matches)
