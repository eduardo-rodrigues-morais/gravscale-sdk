from enum import Enum


class EnumAuthenticationPrintableAttributes(str, Enum):
    CLIENT_ID = "Client ID"
    EMAIL = "E-mail"
    PASSWORD = "Password"
