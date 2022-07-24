# pylint: disable=no-value-for-parameter
"""Commnd Line to create users"""

import re
import sys
from typing import List

from src.database.querys import UserQuerys

regex = re.compile(
    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
)


def is_valid(email):
    verify_email = re.fullmatch(regex, email)
    if verify_email:
        print('Valid email')
    else:
        print('Invalid email')


def create_user(user_data: List):
    """Create new user with command line.
    exemple:
    python utils.py acesso@krypta.com admiriano
    """
    user_data.__delitem__(0)
    if is_valid(user_data[1]) is False:
        pass   # pylint: disable=multiple-statements
    UserQuerys.create(*user_data)
    print('usurio criado com sucesso')


if __name__ == '__main__':
    sys.exit(create_user(sys.argv))
