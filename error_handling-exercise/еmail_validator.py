import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustOneSymbolOnlyError(Exception):
    pass


domains = [".com", ".bg", ".org", ".net"]

valid_domain = r"\.[a-z]+"

email = input()

while email != "End":
    try:
        if email.count("@") > 1:
            raise MustOneSymbolOnlyError("Email must have only one @!")

        if len(email.split("@")[0]) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")

        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")

        if re.findall(valid_domain, email)[0] not in domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    except IndexError:
        print("Invalid email")

    else:
        print("Email is valid")

    email = input()
