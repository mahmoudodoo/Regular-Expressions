
import re

# Using search() to find the first occurrence of "Python" in a string
text = "Python is powerful and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open."
search_result = re.search('Python', text)
print(f"Search result: {search_result.group()}")

# Using match() to check if the string starts with "Python"
match_result = re.match('Python', text)
print(f"Match result: {match_result.group()}")

# Using findall() to find all occurrences of "is" in a string
findall_result = re.findall('is', text)
print(f"Findall result: {findall_result}")
