#Type conversion
from datetime import date

birth_year = int(input('What year you were born: '))

current_year = date.today().year

age = current_year - birth_year

print(f'You are {age} years old')


# Password checker
print("Password checker")
user_name = "Mark"
user_pwd = input(f"Hey {user_name} please enter your password: ")
pwd_length = len(user_pwd)
secret_pwd = '*' * pwd_length
print(f'Hey {user_name} your password {secret_pwd} is of {pwd_length} characters in length')

