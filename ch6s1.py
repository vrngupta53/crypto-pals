from ch3s1 import single_xor_crack
from ch5s1 import multi_byte_xor

def hamming_dist(buffer1 , buffer2):
    total = 0
    for i in range(len(buffer1)):
        total += bin(ord(buffer1[i])^ord(buffer2[i])).count("1")
    return total

def main():
    f = open("ch6s1data.txt")
    b64text = f.read()
    ciphertext = b64text.decode("base64")
    score_dict = {}
    # print(hamming_dist("wokka wokka!!!\n" , "this is a test\n"))
    for KEY_SIZE in range(2,100):
        hamming_score = 0
        for i in range(4):
            hamming_score += hamming_dist(ciphertext[i*KEY_SIZE:(i+1)*KEY_SIZE], ciphertext[(i+1)*KEY_SIZE:(i+2)*KEY_SIZE])
        normalized_hamming_score = hamming_score/KEY_SIZE
        score_dict[KEY_SIZE] = normalized_hamming_score
    
    sorted_dict = sorted(score_dict, key=score_dict.get)
    for i in range(4):
        opt_size = sorted_dict[i]
        key = ""
        for j in range(opt_size):
            key += chr(single_xor_crack(ciphertext[j::opt_size], 0))
        print(i)
        print(multi_byte_xor(ciphertext, key))
        print(key)

if __name__=="__main__":
    main()