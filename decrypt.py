# import Fernet and MultiFernet modules
from cryptography.fernet import Fernet, MultiFernet
import base64
# key generation
key1 = Fernet(b"ET6ZW0oCmQKeRlcOASPCcKhvzyYUOrkZyDHf0ky7qL4=")
key2 = Fernet(b"0XwCEUAoKYWkeTFAiL43gsFT3vZRUE4QUjvALet2ESs=c")
 
# the MultiFernet takes a list of Fernet instances
f = MultiFernet([key1, key2])
 
 
# decryption of ciphertext to plaintext
d = f.decrypt(b"gAAAAABin3XB6_msaZTcAnTQ1JwRokcqiDFBXhi_BLP9rwY-DEUsPmGMXSBIn2CSDKDHlwduv8YvIPaqeOzpDZ62NDp3oOYeR_APr0Fk0hWDb00dV1nBQpY3lFMhpO4-kYkGYHmNfBWd")
 
#display the plaintext
print(d.decode())
 
