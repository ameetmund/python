# Decorators
# Decorators are used highly in python. They are quite useful for number of
# use cases.

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def validation(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return validation


@authenticated
def message_friends(user):
    print('message has been sent')

print(type(message_friends))
message_friends(user1)