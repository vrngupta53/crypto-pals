def xor(buffer1 , buffer2):
    return format((int(buffer1 , 16) ^ int(buffer2 , 16)) , 'x')

string1 = "1c0111001f010100061a024b53535009181c"
string2 = "686974207468652062756c6c277320657965"
print(xor(string1 , string2))
