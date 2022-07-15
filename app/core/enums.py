from enum import Enum


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    LIBRARIAN = "LIBRARIAN"
    CUSTOMER = "CUSTOMER"
