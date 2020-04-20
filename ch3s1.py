freq_dict = {"a":	8.167,	 
"b":	1.492,	
"c":	2.202,	
"d":	4.253,	
"e":	12.702,	
"f":	2.228,	
"g":	2.015,
"h":	6.094,	
"i":	6.966,	
"j":	0.153,	
"k":	1.292,	
"l":	4.025,	
"m":	2.406,	
"n":	6.749,	
"o":	7.507,	
"p":	1.929,	
"q":	0.095,	
"r":	5.987,	
"s":	6.327,	
"t":	9.356,	
"u":	2.758,	
"v":	0.978,	
"w":	2.560,	
"x":	0.150,	
"y":	1.994,	
"z":	0.077,}

def single_byte_xor(text , c):
    result = ""
    for i in text:
        result += chr(ord(i)^c)
    return result

def single_xor_crack(ciphertext , result_count = 2):
    scoredict = {}

    max = 0
    ind = -1
    for i in range(256):
        total = 0
        xored_text = single_byte_xor(ciphertext , i)
        for c in xored_text:
            total += freq_dict.get(c , 0)
        scoredict[total] = xored_text + ":" + str(i)
        if(total > max):
            max = total
            ind = i

    ctr = 0
    for total in sorted(scoredict , reverse=True):
        if(ctr >= result_count):
            break
        print(total , scoredict[total])
        ctr += 1

    return ind

def main():
    hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    ciphertext = hex_string.decode("hex")
    single_xor_crack(ciphertext)    
    
if __name__== "__main__" :
    main()


