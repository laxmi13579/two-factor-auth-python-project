import pyotp 
import time
import random

# key should be hardcoded, not pyotp.random_base32()
key = "base32secret3232"
# it will give same 6-digit code every time for the index.
hotp = pyotp.HOTP(key)

num = random.randrange(100)

# generate OTP for the given index
print(hotp.at(num))

'''
# example 
print(hotp.at(0)) 260182
print(hotp.at(0)) 260182
print(hotp.at(2)) 795760
'''

input_code = input("inter the Two-Factor Auth Code:")

# validate the OTP
print(hotp.verify(input_code, num))


