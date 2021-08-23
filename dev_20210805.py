# Regex
# Password validation using regex

import re

pattern = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')


print(pattern.fullmatch(input("Enter your password: ")))