import pyotp
import time


# it will generate 32 digit text eg. PWKRMVWVXDHUS6QPVI6366TKZHSHUUJP
key = pyotp.random_base32()

# hardcoded key
# key = 'myNameIsLaxmiKumarYadav'

totp = pyotp.TOTP(key)

print(totp.now())

input_code = input("inter the Two-Factor Auth Code:")

print("Enter the code n 30 sec!!")

print(totp.verify(input_code))

