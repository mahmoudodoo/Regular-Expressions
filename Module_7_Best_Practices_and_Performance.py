
import re
import time

# Example: Compiling RegEx pattern
pattern = re.compile(r'\b\w+\b')
text = "This is a test sentence. This sentence is for testing compiled RegEx."
start_time = time.time()
for _ in range(1000):
    re.findall(pattern, text)
print("Compiled pattern time:", time.time() - start_time)

# Example: Avoiding common pitfalls - using non-greedy quantifiers
greedy_pattern = re.compile(r'<.*>')
nongreedy_pattern = re.compile(r'<.*?>')
test_html = "<title>Example Title</title>"
print("Greedy match:", greedy_pattern.findall(test_html))
print("Non-greedy match:", nongreedy_pattern.findall(test_html))
