from scapy.all import *
# import Fernet and MultiFernet modules
from cryptography.fernet import Fernet, MultiFernet
# key generation
key1 = Fernet(b"ET6ZW0oCmQKeRlcOASPCcKhvzyYUOrkZyDHf0ky7qL4=")
key2 = Fernet(b"0XwCEUAoKYWkeTFAiL43gsFT3vZRUE4QUjvALet2ESs=c")
 
# the MultiFernet takes a list of Fernet instances
f = MultiFernet([key1, key2])

def decryption(packet):
    #print(packet[Raw].load)
    # decryption of ciphertext to plaintext
    d = f.decrypt(packet[Raw].load)
    
    # display the plaintext
    print(d.decode())


#print(get_if_list())
sniff(filter="udp port 8888", prn=decryption, iface="\\Device\\NPF_Loopback")

