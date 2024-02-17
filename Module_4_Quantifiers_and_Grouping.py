
import re

# Example of quantifiers
greedy_match = re.findall('a+', 'caaandy')
print(f"Greedy match: {greedy_match}")

lazy_match = re.findall('a+?', 'caaandy')
print(f"Lazy match: {lazy_match}")

# Example of grouping
group_match = re.search('(ca)+', 'cacaca candy').group()
print(f"Group match: {group_match}")
