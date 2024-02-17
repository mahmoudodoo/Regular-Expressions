
import re

# Example: Basic pattern matching using search()
# Search for the word 'RegEx' in a given string
sample_text = "Learning how to use Regular Expressions (RegEx) can significantly improve your data processing capabilities."
match = re.search('RegEx', sample_text)
if match:
    print("Found:", match.group())
else:
    print("No match found.")
