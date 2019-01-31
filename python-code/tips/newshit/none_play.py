
# None  it's like null in java
# no value (absence of a value)

# avoid passing empty string 


print(type(None))
'''<class 'NoneType'>
Process finished with exit code 0
'''


def email(subject, content, to, cc, bcc):
    print(f"{subject}, {content}, {to},  {cc}, {bcc}")


def smart_email(subject, content, to, cc = None, bcc = None):
    print(f"{subject}, {content}, {to},  {cc}, {bcc}")


# TypeError: email() missing 2 required positional arguments: 'cc' and 'bcc'
# email("subject", "great work", "test@gmail.com")

smart_email("subject", "great work", "test@gmail.com")
'''
subject, great work, test@gmail.com,  None, None
'''

# or we can call
email("subject", "great work", "test@gmail.com", None, None)
# subject, great work, test@gmail.com,  None, None



var = "123"

if var is None:
    print("Do Something")
else:
    print("Not do")