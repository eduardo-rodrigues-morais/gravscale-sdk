from enum import Enum


class EnumNetworkPrintableAttributes(str, Enum):
    CLIENT_ID = "Client ID"
    VPC_NAME = "VPC name"
    ADDRESS = "Address"
    PUBLIC_ADDRESS = "Public Address"
