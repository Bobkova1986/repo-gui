import re


valid_mail = re.compile(r'(?P<username>[a-z0-9]+[\._]?[a-z0-9])@(?P<domain>\w+[.]\w{2,3})$', re.IGNORECASE)


def check(email):
    if not re.search(valid_mail, email):
        raise ValueError(f'wrong email address: {email}')

    print(valid_mail.match(email).groupdict())


try:
    check("sacT_p@mail.ru")
except ValueError as er:
    print(er)