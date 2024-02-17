
import re

# Lookahead assertion example
lookahead_example = re.findall('Jack(?= Sprat)', 'Jack Sprat could eat no fat')
print(f"Lookahead match: {lookahead_example}")

# Lookbehind assertion example
lookbehind_example = re.findall('(?<=Jack )Sprat', 'Jack Sprat could eat no fat')
print(f"Lookbehind match: {lookbehind_example}")

# Backreference example
backreference_example = re.search('(\w+) \1', 'the the').group()
print(f"Backreference match: {backreference_example}")

# Named group and flag example
named_group_example = re.search('(?i)(?P<word>jack) (?P<word2>sprat)', 'Jack Sprat could eat no fat').groupdict()
print(f"Named group match: {named_group_example}")
