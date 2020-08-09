class Password():
    def __init__(self,password):
        self.password = password

    def __str__(self):
        length = len(self.password)
        return length * '*'

    def resolve_password(self):
        return self.password

    def change_password(self, argument):
        self.password = argument
        return self.password

    def check_validity(self, *check_functions):
        for func in check_functions:
            if func(self.password) == False:
                return False
            else:
                return True

def no_shorter_than_8(string):
    return len(string) >= 8

def contains_special_chars(string):
    return not string.isalnum()

def starts_upper_case(string):
    if string[0].isupper():
        return True
    return False

pw1 = Password("Password_1234")
print(pw1)
print(pw1.resolve_password())
print(pw1.check_validity(no_shorter_than_8, contains_special_chars, starts_upper_case))
pw1.change_password("password_1234")
print(pw1.check_validity(starts_upper_case))