import re
from typing import Callable

print('Welcome to Pangrammar!\n\n')

def validate_input(prompt: str, checker: Callable[[str], bool]) -> str:
  user_input = None
  while True:
    user_input = input(prompt)
    if not checker(user_input):
      print('Invalid input.')
    else:
      break
  return user_input


key_letter = validate_input('What is the key letter? ', lambda val: re.search('^[a-zA-Z]$', val) is not None).lower()
print('Got it: ' + key_letter)
other_letters = validate_input('What are the other letters? ', lambda val: re.search('^[a-zA-Z]+$', val) is not None).lower()
print('Got it: ', other_letters)

any_letter = ''.join(sorted(key_letter + other_letters))
regex = f'^[{any_letter}]*{key_letter}[{any_letter}]*$'

sorted_pangram_regex = '^' + ''.join(map(lambda letter: f'{letter}+', any_letter)) + '$'


word_list = open('./wordlist.txt')
for word in word_list:
  word = word.strip()
  if len(word) > 3 and re.match(regex, word):
    if (re.match(sorted_pangram_regex, ''.join(sorted(word)))):
      print('** ' + word)
    else:
      print(word)
