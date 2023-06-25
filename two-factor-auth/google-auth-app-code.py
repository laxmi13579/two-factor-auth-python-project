import pyotp 

key = "thisismysecretekey"


totp = pyotp.TOTP(key)


input_code = input("Enter google Auth Code:")

print(totp.verify(input_code))


