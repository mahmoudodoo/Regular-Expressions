
import re

# Example of metacharacters: Matching any single character except newline
print(re.findall('.', 'hello world'))

# Example of special sequences: Matching any digit
print(re.findall('\d', '2 apples, 12 oranges'))

# Example of character sets: Matching any vowel
print(re.findall('[aeiou]', 'hello world'))
