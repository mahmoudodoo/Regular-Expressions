
import re

# Example: Email address validation
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = ["username@example.com", "wrong-email.com", "another.valid.email@example.org"]
print("Valid emails:")
for email in emails:
    if re.fullmatch(email_pattern, email):
        print(f"- {email}")

# Example: Extracting dates from text
date_pattern = r'\b\d{2}/\d{2}/\d{4}\b'
text_with_dates = "Important dates are 05/12/2022 and 23/11/2023."
print("Extracted dates:", re.findall(date_pattern, text_with_dates))

# Example: Replacing multiple spaces with a single space
text_with_spaces = "This    sentence  contains   multiple spaces."
cleaned_text = re.sub('\s+', ' ', text_with_spaces)
print("Cleaned text:", cleaned_text)
