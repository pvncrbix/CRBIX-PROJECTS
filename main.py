class InvalidEmailException(Exception):
    def _init_(self, message):
        super()._init_(message)
def validate_email(email):
    if '@' not in email:
        raise InvalidEmailException("Invalid email ID: '@' symbol is missing.")
try:
    email_id = input("Enter your email ID: ")
    validate_email(email_id)
    print("Email ID is valid.")
except InvalidEmailException as e:
    print(e)
