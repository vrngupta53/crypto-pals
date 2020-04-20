from Crypto.Cipher import AES

def main():
    f = open("ch7s1data.txt")
    b64text = f.read()
    ciphertext = b64text.decode("base64")
    key = "YELLOW SUBMARINE"
    AESobj = AES.new(key, AES.MODE_ECB)
    print(AESobj.decrypt(ciphertext))

if(__name__ == "__main__"):
    main()