import pyotp 
import qrcode

key = "thisismysecretekey"

uri = pyotp.totp.TOTP(key).provisioning_uri(name='laxmi@gmail.com', issuer_name='password')

print(uri)

qrcode.make(uri).save("totp.png")